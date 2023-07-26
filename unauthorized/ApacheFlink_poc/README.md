# Apache Flink的任意Jar包上传导致远程代码执行的漏洞

攻击者可上传恶意jar包反弹shell

## 影响范围

<= 1.10.1

## 工具利用

python3 ApacheFlink_poc.py -u http://127.0.0.1:1111 单个url测试

python3 ApacheFlink_poc.py -f url.txt 批量检测

## 修复建议

建议用户关注Apache Flink官网，及时获取该漏洞最新补丁。临时解决建议 设置IP白名单只允许信任的IP访问控制台并添加访问认证。

## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。
