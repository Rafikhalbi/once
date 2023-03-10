import re


def sort_payload(html, name):
    try:
        sort = re.search(r'name="{}" value="(.*?)"'.format(name), str(html))[1]
    except: pass
    return sort