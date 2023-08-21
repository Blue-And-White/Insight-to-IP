from bs4 import BeautifulSoup
import requests
import base64


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}


def Ip_Info(ip):    #输出ip的基本信息
	ip138="https://www.ip138.com/iplookup.php?ip="
	ip138url=ip138+ip
	re=requests.get(ip138url,headers=headers)
	soup = BeautifulSoup(re.text, 'html.parser')
	ip138result = soup.select('tbody')  # 直接定位到返回结果处，在网页中对应的标签tbody，具体可以参见网页源代码
	for i in ip138result:  # 这里的操作是将i格式化为tag的类型方便后续操作,select出来的结果为bs4.result类型的不好操作
		pass
	IpInfo = i.text
	IpInfo.replace("\n", "\\n")  # 格式化输出
	print(IpInfo)
	return IpInfo

def Ip_For_Domain(ip):   #查找ip下面绑定的域名
	ip138="https://site.ip138.com/"
	ip138url=ip138+ip
	re=requests.get(ip138url,headers=headers)
	soup=BeautifulSoup(re.text,'html.parser')
	ip138result=soup.select('#list')  #直接定位到返回结果处，在网页中对应的标签id为List，具体可以参见网页源代码
	for i in ip138result:  			#这里的操作是将i格式化为tag的类型方便后续操作,select出来的结果为bs4.result类型的不好操作
		pass
	BindDomain=i.text
	BindDomain.replace("\n","\\n")  #格式化输出
	print(BindDomain)
	return BindDomain

def Fofa_Api_Ip(fofamail,fofakey,ip):
	fofa_api=r"https://fofa.info/api/v1/search/all?email={}&key={}&qbase64={}"
	re=requests.get(fofa_api.format(fofamail,fofakey,base64.b64encode(ip.encode('utf-8')).decode()))
	fofa_ip_info= re.json()['results']
	returninfo=''
	for i in fofa_ip_info:
		print(i)
		returninfo=returninfo+str(i)+"\n"
	return returninfo
