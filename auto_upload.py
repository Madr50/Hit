import os
import requests
from telethon import TelegramClient, events
from github import Github

# ==========================================
# الإعدادات الخاصة بك (جاهزة 100%)
# ==========================================
API_ID = 24044141          
API_HASH = '3de21516f69614b183a96dbf1846aae5'
CHANNEL_ID = -1002967179524 # آيدي قناة H o t m a i l

GITHUB_TOKEN = 'Ghp_vKDVKQhbWUtqqHVbAljub9bPfHri090zVNEL' # التوكن تبعك
REPO_NAME = 'Madr50/Hit'

# العداد يبدأ من الملف الأخير اللي وصلته (مثلا 2000)
file_counter = 2000

# عشان ما نرفع نفس الملف مرتين
uploaded_files = set()

client = TelegramClient('my_session', API_ID, API_HASH)
gh = Github(GITHUB_TOKEN)
repo = gh.get_repo(REPO_NAME)

def get_gofile_direct_link(gofile_url):
    try:
        # استخراج الـ ID الخاص بالملف من رابط gofile
        content_id = gofile_url.split('/')[-1]
        api_url = f"https://api.gofile.io/contents/{content_id}?wt=4fd6sg8f8s6"
        
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(api_url, headers=headers).json()
        
        if res.get('status') == 'ok':
            # البحث عن رابط التحميل المباشر داخل محتوى الجوفايل
            children = res['data']['contents']
            for child_id, child_info in children.items():
                if 'link' in child_info:
                    return child_info['link']
    except Exception as e:
        print(f"❌ خطأ في استخراج رابط Gofile: {e}")
    return None

async def process_message(event):
    """
    بتعالج رسالة واحدة (قديمة أو جديدة).
    بترفع الملف لـ GitHub لو لقت زر GoFile.
    """
    global file_counter
    
    # فحص إذا البوست يحتوي على أزرار تفاعلية
    if event.buttons:
        for row in event.buttons:
            for button in row:
                # البحث عن الزر اللي فيه رابط
                if button.url and "gofile.io" in button.url:
                    
                    # ✅ تخطي لو الرابط نفسه تم رفعه قبل
                    if button.url in uploaded_files:
                        print(f"⏭️ تم تخطي (مُرفع سابقاً): {button.url}")
                        continue
                    
                    print(f"🔗 لقيت رابط GoFile: {button.url}")
                    
                    # 1. جلب الرابط المباشر للتحميل من جوفايل
                    direct_link = get_gofile_direct_link(button.url)
                    
                    if direct_link:
                        print(f"⬇️ جاري تحميل الملف...")
                        try:
                            file_res = requests.get(direct_link, timeout=120)
                            file_res.raise_for_status()
                        except Exception as e:
                            print(f"❌ فشل التحميل: {e}")
                            continue
                        
                        file_name = f"hot{file_counter}.txt"
                        
                        # 2. حفظ الملف مؤقتاً
                        with open(file_name, 'wb') as f:
                            f.write(file_res.content)
                            
                        # 3. قراءة المحتوى ورفعه على GitHub
                        try:
                            with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                                
                            repo.create_file(file_name, f"Auto upload {file_name}", content)
                            print(f"✅ تم رفع {file_name} بنجاح إلى GitHub!")
                            
                            # سجل الرابط عشان ما يتكرر
                            uploaded_files.add(button.url)
                            
                            # 4. زيادة العداد للملف التالي
                            file_counter += 1
                            
                        except Exception as e:
                            print(f"❌ خطأ برفع الملف لـ GitHub: {e}")
                        finally:
                            # 5. تنظيف الجهاز وحذف الملف المحلي
                            if os.path.exists(file_name):
                                os.remove(file_name)
                    else:
                        print("⚠️ ما قدرت أطلع رابط التحميل المباشر من صفحة Gofile")

async def download_old_messages():
    """
    بتجيب كل الرسايل القديمة من القناة وتعالجها.
    """
    print("📜 جاري جلب الرسايل القديمة من القناة...")
    msg_count = 0
    
    # limit=None يعني كل الرسايل الموجودة بالقناة
    # لو القناة كبيرة جداً ممكن تستبدلها برقم مثل limit=5000
    async for message in client.iter_messages(CHANNEL_ID, limit=None):
        if message.buttons:
            await process_message(message)
            msg_count += 1
    
    print(f"🏁 خلصنا من {msg_count} رسالة قديمة. الآن بننتقل للمراقبة الحية...")

@client.on(events.NewMessage(chats=CHANNEL_ID))
async def download_new_combos(event):
    """
    المراقبة الحية للرسايل الجديدة.
    """
    await process_message(event)

# ==========================================
# التشغيل
# ==========================================
print("🤖 البوت شغال الآن...")

client.start()

# شغل جلب القديم أولاً (بشكل متزامن مع await)
client.loop.run_until_complete(download_old_messages())

# بعد ما يخلص القديم، يضل شغال على المراقبة الحية
print("👁️ الآن قاعد يراقب القناة للرسايل الجديدة... بتقدر تروح ترتاح!")
client.run_until_disconnected()
