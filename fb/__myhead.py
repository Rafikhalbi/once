def headers(ua):
    header = {'Host': 'mbasic.facebook.com','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','dnt': '1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    return header
    
def headers_login(ua):
    header = {'Host': 'mbasic.facebook.com','content-length': '165','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','origin': 'https://mbasic.facebook.com','dnt': '1','upgrade-insecure-requests': '1','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
    return header
    
def payloads(lsd, jazoest, m_ts, li, email, password):
    return {
        "lsd": lsd,
        "jazoest": jazoest,
        "m_ts": m_ts,
        "li": li,
        "try_number": "0",
        "unrecognized_tries": "0",
        "email": email,
        "pass": password,
        "login": "Masuk",
        "bi_xrwh": "0"
     }

url = "https://mbasic.facebook.com"
url_login = "https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8"