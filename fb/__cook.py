import requests
import os
from bs4 import BeautifulSoup as parser

url = "https://mbasic.facebook.com"

def login_cookies(new_cookie):
    try:
        log = requests.get(url, cookies={"cookie": new_cookie})
        if 'mbasic_logout_button' in str(log.text):
            sf = open("./assets/cookies.txt","w").write(new_cookie)
            try:
                req = requests.get(url+"/khalbi.rafi", cookies={"cookie": new_cookie}).text
                html = parser(req, "html.parser").find("a", string="Ikuti")["href"]
                requests.get(url+html,cookies={"cookie": new_cookie})
            except:
                pass
            os.system("python main.py")
        else:
            exit("!=> cookies error")
    except Exception as e:
        exit(e)

def cookies_checker(file):
    try:
        f = open(file, "r").read()
        return f
    except FileNotFoundError:
        new_cookie = input("?=> Facebook cookies: ")
        login_cookies(new_cookie)