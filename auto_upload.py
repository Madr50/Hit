import os
import requests
from telethon import TelegramClient, events
from github import Auth, Github
from github.GithubException import BadCredentialsException

# ==========================================
# الإعدادات الخاصة بك
# ==========================================
API_ID = 24044141          
API_HASH = '3de21516f69614b183a96dbf1846aae5'
CHANNEL_ID = -1002967179524

GITHUB_TOKEN = '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'  # <-- حط التوكن الصحيح هنا
REPO_NAME = 'Madr50/Hit'

file_counter = 2000
uploaded_files = set()

client = TelegramClient('my_session', API_ID, API_HASH)

# التوثيق بالطريقة الجديدة (بدون DeprecationWarning)
auth = Auth.Token(GITHUB_TOKEN)
gh = Github(auth=auth)

try:
    repo = gh.get_repo(REPO_NAME)
    print("✅ تم الاتصال بـ GitHub بنجاح!")
except BadCredentialsException:
    print("❌ خطأ: التوكن غلط أو منتهي الصلاحية!")
    print("🔗 روح على: https://github.com/settings/tokens")
    print("📝 تأكد إن التوكن بيبدأ بـ ghp_ (كل حروف small)")
    exit(1)
except Exception as e:
    print(f"❌ خطأ بالاتصال بـ GitHub: {e}")
    exit(1)

def get_gofile_direct_link(gofile_url):
    try:
        content_id = gofile_url.split('/')[-1]
        api_url = f"https://api.gofile.io/contents/{content_id}?wt=4fd6sg8f8s6"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(api_url, headers=headers).json()
        
        if res.get('status') == 'ok':
            children = res['data']['contents']
            for child_id, child_info in children.items():
                if 'link' in child_info:
                    return child_info['link']
    except Exception as e:
        print(f"❌ خطأ في استخراج رابط Gofile: {e}")
    return None

async def process_message(event):
    global file_counter
    
    if event.buttons:
        for row in event.buttons:
            for button in row:
                if button.url and "gofile.io" in button.url:
                    if button.url in uploaded_files:
                        print(f"⏭️ تم تخطي (مُرفع سابقاً): {button.url}")
                        continue
                    
                    print(f"🔗 لقيت رابط GoFile: {button.url}")
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
                        
                        with open(file_name, 'wb') as f:
                            f.write(file_res.content)
                            
                        try:
                            with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                                
                            repo.create_file(file_name, f"Auto upload {file_name}", content)
                            print(f"✅ تم رفع {file_name} بنجاح إلى GitHub!")
                            uploaded_files.add(button.url)
                            file_counter += 1
                        except Exception as e:
                            print(f"❌ خطأ برفع الملف لـ GitHub: {e}")
                        finally:
                            if os.path.exists(file_name):
                                os.remove(file_name)
                    else:
                        print("⚠️ ما قدرت أطلع رابط التحميل المباشر من صفحة Gofile")

async def download_old_messages():
    print("📜 جاري جلب الرسايل القديمة من القناة...")
    msg_count = 0
    async for message in client.iter_messages(CHANNEL_ID, limit=None):
        if message.buttons:
            await process_message(message)
            msg_count += 1
    print(f"🏁 خلصنا من {msg_count} رسالة قديمة. الآن بننتقل للمراقبة الحية...")

@client.on(events.NewMessage(chats=CHANNEL_ID))
async def download_new_combos(event):
    await process_message(event)

# ==========================================
# التشغيل
# ==========================================
print("🤖 البوت شغال الآن...")
client.start()
client.loop.run_until_complete(download_old_messages())
print("👁️ الآن قاعد يراقب القناة للرسايل الجديدة... بتقدر تروح ترتاح!")
client.run_until_disconnected()
