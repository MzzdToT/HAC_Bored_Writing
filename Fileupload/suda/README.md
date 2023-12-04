# 速达软件 DesignReportSave.jsp 文件上传
速达软件全系产品存在任意文件上传漏洞，未经身份认证的攻击者可以通过此漏洞上传恶意后门文件，获取服务器权限

## 工具利用

python3 suda_fileupload.py -u http://127.0.0.1:8082 单个url测试

python3 suda_fileupload.py -f url.txt 批量检测

![exp](./poc.jpg)


## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。
