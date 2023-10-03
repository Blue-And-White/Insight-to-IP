#  Insight into IP是一款用于迅速根据ip地址，域名信息，方便蓝队在溯源过程中获取相关信息的工具
#  支持调用fofa获取更详细的信息，在初始化结束后，会生成配置文件您可以在配置文件中指定你的apikey
#  更多功能接口，更加方便的信息有待后续完善，欢迎提出您宝贵的意见
#  -i 指定ip地址
#  -d 指定域名
#  -j 开启判断功能，目前支持存活判断，端口判断，以及cdn检测
#  -o 输出文件
#  Version:0.2
#  Author:B1uewhit4


from bs4 import BeautifulSoup
import requests
import os
import ipinfo
import domain
import judgeinfo
import argparse
import yaml
import re
import time


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
filecontent=''
def Config_Start():
	if not os.path.exists("config.yaml"):
		print("首次运行需要执行初始化流程，您可以配置您的接口秘钥在config.yaml中,您可以根据您的需求配置APIKey")
		ConfigInfo = {"version":"0.2","fofa":{"key":"","mail":""},"port_scan":{"port":"80,1433,5003,3306,3389,6369,8000,8080,8024","timeout":"10"}}
		with open('config.yaml','w',encoding="utf-8") as f:
			yaml.dump(ConfigInfo,f)
		return None,None,"80,5003,8000,8080,8024","10"
	else:
		with open('config.yaml','r') as f:
			ConfigData = yaml.load(f,Loader=yaml.FullLoader)
		fofamail = ConfigData.get('fofa')['mail']
		fofakey= ConfigData.get('fofa')['key']
		port = ConfigData.get('port_scan')['port']
		timeout = ConfigData.get('port_scan')['timeout']
		if fofakey and fofamail and port and timeout:
			return fofamail,fofakey,port,timeout
		else:
			return None,None,port,timeout



if __name__=="__main__":
	fofamail,fofakey,port_scan,timeout=Config_Start()
	parser=argparse.ArgumentParser()
	parser.description='Please enter a ip address or domain according to your requirement'
	parser.add_argument("-i",help="Specify an IP address to obtain its bound domain name and information",dest="ip")
	parser.add_argument("-d",help="Obtain information based on the specified domain name",dest="domain")
	parser.add_argument("-j", help="Judge information", dest="judge",default="1")
	parser.add_argument("-o", help="Output the collection results to a file", dest="output", default=" ")
	args=parser.parse_args()
	if args.ip:
		ipbaseinfo=ipinfo.Ip_Info(args.ip)
		ipdomain=ipinfo.Ip_For_Domain(args.ip)
		filecontent=filecontent+ipbaseinfo+"\n"+ipdomain+"\n"
		if fofamail and fofakey:
			fafainfo=ipinfo.Fofa_Api_Ip(fofamail,fofakey,args.ip)
			filecontent = filecontent+fafainfo
	if args.domain:
		domainicp=domain.Domain_Icp(args.domain)
		filecontent=filecontent+domainicp
	if args.judge:
		if args.domain:
			cdninfo= judgeinfo.Judge_Cdn(args.domain)
			httpstatus= judgeinfo.Judge_alive(args.domain)
			filecontent=filecontent+cdninfo+"\n"+httpstatus
		if args.ip:
			portinfo=judgeinfo.Judge_port(args.ip,port_scan,timeout)
			filecontent=filecontent+portinfo
	if args.output:
		filename=args.output
		f=open(filename+".txt","w")
		f.write(filecontent)
		f.close()


	print("[+] Information has been collected!\n")
