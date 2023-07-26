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
	url2 = url.scheme + '://' + url.netloc + '/terminals/1'
	headers = {'User-Agent': get_ua()}
	try:
		res = requests.get(url1,timeout=15,verify=False)
		if res.status_code==200 and "files" in res.text:
			# print ("\033[32m[+]%s\033[0m" %url1)
			res2 = requests.get(url2,timeout=15,verify=False)
			if res.status_code==200:
				print("\033[32m[+]%s\033[0m" %url2)
		else:
			pass
		# list1 = version.split('.') #version格式为1.x.1 用split切割成数组
		# if int(list1[1]) <= 10:#取中间为与10比较 小于等于10为true
		# 	try:
		# 		res3 = requests.get(url2,timeout=15,verify=False)
		# 		if re.search(r'web-submit',res3.text,re.I):
		# 			poc = re.findall(r'"web-submit":(.*?)}', res3.text)[0]
		# 			if poc == "false":
		# 				print ("\033[31m[-]%s    version:%s  Target is Not vuln\033[0m" %(url1,version))
		# 			else:
		# 				print ("\033[32m[+]%s    version:%s  Target is vuln!\033[0m" %(url1,version))
		# 		else:
		# 			print ("\033[32m[+]%s    version:%s  Target is vuln!\033[0m" %(url1,version))
		# 	except Exception as e:
		# 		print ("[-]%s    version:%s  Target is Not vuln" %(url1,version))
		# t.write("%s %s\n" %(url,flag))
	except Exception as e:
		print("[-]%s is timeout" %url1)


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
	   ___                   _           ______  _____  _____ 
	  |_  |                 | |          | ___ \/  __ \|  ___|
	    | |_   _ _ __  _   _| |_ ___ _ __| |_/ /| /  \/| |__  
	    | | | | | '_ \| | | | __/ _ \ '__|    / | |    |  __| 
	/\__/ / |_| | |_) | |_| | ||  __/ |  | |\ \ | \__/\| |___ 
	\____/ \__,_| .__/ \__, |\__\___|_|  \_| \_| \____/\____/ 
	            | |     __/ |       ______                    
	            |_|    |___/       |______|                   
	            
                              Jupyter_RCE_poc By m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='Jupyter_RCE_poc By m2')
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