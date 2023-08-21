from bs4 import BeautifulSoup
import requests



headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

def Judge_Cdn(domain):
    pass

def Domain_Icp(domain):
    url="https://api.wer.plus/api/icpb?t="
    url=url+domain
    re = requests.get(url, headers=headers)
    data=re.json()
    returndomain=""
    for key,values in data['data'][0].items():
        print(key+":"+values)
        returndomain=returndomain+key+":"+values+"\n"
    return returndomain



