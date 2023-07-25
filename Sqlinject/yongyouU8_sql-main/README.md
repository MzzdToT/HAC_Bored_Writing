# yongyouU8_sql

用友 U8 OA test.jsp文件S1参数存在SQL注入漏洞


## 漏洞影响

用友 U8 OA

## 工具利用

python3 U8oatest.jsp_sql.py -u http://127.0.0.1:1111 单个url测试

python3 U8oatest.jsp_sql.py -f url.txt 批量验证

![poc](./poc.png)

## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。

