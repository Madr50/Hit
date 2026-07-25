import os
import requests
from telethon import TelegramClient, events
from github import Github

# ==========================================
# الإعدادات الخاصة بك (جاهزة)
# ==========================================
API_ID = 24044141          
API_HASH = '3de21516f69614b183a96dbf1846aae5'
CHANNEL_ID = -1002967179524 # آيدي قناة H o t m a i l

GITHUB_TOKEN = 'توكن_قيت_هب_تبعك' # بس غير هاي!
REPO_NAME = 'Madr50/Hit'

# العداد يبدأ من الملف الأخير اللي وصلته (مثلا 2000)
file_counter = 2000

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

@client.on(events.NewMessage(chats=CHANNEL_ID))
async def download_new_combos(event):
    global file_counter
    
    # فحص إذا البوست يحتوي على أزرار تفاعلية
    if event.buttons:
        for row in event.buttons:
            for button in row:
                # البحث عن الزر اللي فيه رابط
                if button.url and "gofile.io" in button.url:
                    print(f"🔗 لقيت رابط GoFile جديد: {button.url}")
                    
                    # 1. جلب الرابط المباشر للتحميل من جوفايل
                    direct_link = get_gofile_direct_link(button.url)
                    
                    if direct_link:
                        print(f"⬇️ جاري تحميل الملف...")
                        file_res = requests.get(direct_link)
                        
                        file_name = f"hot{file_counter}.txt"
                        
                        # 2. حفظ الملف مؤقتاً
                        with open(file_name, 'wb') as f:
                            f.write(file_res.content)
                            
                        # 3. قراءة المحتوى ورفعه على GitHub
                        with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            
                        repo.create_file(file_name, f"Auto upload {file_name}", content)
                        print(f"✅ تم رفع {file_name} بنجاح إلى GitHub!")
                        
                        # 4. تنظيف الجهاز وحذف الملف المحلي
                        os.remove(file_name)
                        
                        # 5. زيادة العداد للملف التالي
                        file_counter += 1
                    else:
                        print("⚠️ ما قدرت أطلع رابط التحميل المباشر من صفحة Gofile")

print("🤖 البوت شغال الآن وقاعد يراقب القناة سكيّتي... ارتاح والسيستم شغال!")
client.start()
client.run_until_disconnected()

