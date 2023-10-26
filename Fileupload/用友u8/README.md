# 用友U8-Cloud upload任意文件上传漏洞
upload.jsp存在任意文件上传漏洞，攻击者可通过该漏洞上传木马，控制服务器

## 工具利用

python3 U8_cloud_upload.py -u http://127.0.0.1:8082 单个url测试

python3 U8_cloud_upload.py -f url.txt 批量检测

扫描结束会自动保存webshell到vuln.txt

![exp](./poc.png)


## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。
