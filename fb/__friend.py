import requests
import re
from bs4 import BeautifulSoup as parser

acc = []

url = "https://mbasic.facebook.com"

def get_friend(urlf, cookies):
    global acc
    req = requests.get(urlf, cookies={"cookie": cookies})
    for friend in re.findall(r'style="vertical-align: middle"><a class=".." href="(.*?)">(.*?)</a',str(req.text)):
                    if ( "/profile.php" in friend[0] ):
                        uid = re.search(r'\/profile.php\?id\=([0-9]*)',str(friend[0]))[1]
                        name = friend[1].lower()
                        acc.append(uid+"/"+name)
                    else:
                        uid = re.search(r'\/(.*?)\?',str(friend[0]))[1]
                        name = friend[1].lower()
                        acc.append(uid+"/"+name)
                    print(f"*=> Please Wait {len(acc)} !", end="\r")
    if ( "Lihat Teman Lain" in req.text ):
            parsing = parser(req.text, "html.parser").find("a", string="Lihat Teman Lain")["href"]
            get_friend(url+parsing,cookies)
    elif ( "Tidak Ada Teman Untuk Ditampilkan" in req.text ):
        exit("!=> Friend Not Public !!")
    return acc