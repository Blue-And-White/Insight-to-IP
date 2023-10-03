#判断信息是否滞后，以及域名等是否存活
#请注意这部分，为了减少工具的量级，我并没有集成其他工具来帮助判断，大多数都是基于外部接口，实现其实可以利用ajax去实现，为了更加方便，这里我们换成selenium
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

def Judge_Cdn(url):  #这里利用CDN判断的方法多地ping可以看是不是域名解析到多个ip来进行交叉分析
    itdog='https://www.itdog.cn/tcping/'+url
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(itdog)
    browser.find_element(By.XPATH,'//*[@id="screenshots"]/div/div/div/div[3]/div/div/div/div[1]/button[1]').click()
    sleep(5)
    cdn_text = browser.find_element(By.XPATH, '//*[@id="screenshots"]/div/div/div/div[6]/div/div/div[2]/ul').text
    cdn_text="域名："+url+" 的cdn判断情况为\n"+cdn_text
    print(cdn_text)
    browser.quit()
    return cdn_text

def Judge_alive(url): #有的ip或者域名已经挂掉了，但是依旧被显示出来，或者云服务器主机早就转手了，所以这里是通过模拟访问情况来进行判断是否存活
    url="http://"+url
    re=requests.get(url,headers=headers)
    status=url+'http响应为:'+str(re.status_code)
    print(status)
    return status


def Judge_port(ip,port_scan,timeout): #判断ip端口开放情况，方便我们判断其信息是否存在滞后性，请注意该方法调用的是外部接口，端口监测规则可以在config.yaml中修改，默认为"80,5003，8000,8080,8024",timeout为设定等待时间，注意端口越多时间应该越长
    wlphp_portscan='http://duankou.wlphp.com/'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(wlphp_portscan)
    browser.find_element(By.XPATH, '//*[@id="ip_input"]').send_keys(ip)
    browser.find_element(By.XPATH, '//*[@id="port_input"]').send_keys(port_scan)
    browser.find_element(By.XPATH, '//*[@id="scan_btn"]').click()
    sleep(int(timeout))
    port_info = browser.find_element(By.XPATH, '//*[@id="showTable"]').text
    port_info = ip+"端口开放信息为：\n"+port_info
    print(port_info)
    browser.quit()
    return port_info

