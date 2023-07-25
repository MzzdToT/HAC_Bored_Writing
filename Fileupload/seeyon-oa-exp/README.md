## 漏洞概述

由于致远OA旧版本某些接口存在未授权访问，以及部分函数存在过滤不足，攻击者通过构造恶意请求，可在无需登录的情况下上传恶意脚本文件，从而控制服务器。致远OA官方已针对该漏洞提供补丁。

  致远OA是一套办公协同软件。

## 漏洞编号

CNTA-2021-0002

## 漏洞影响范围

致远 OA V8.0

致远 OA V7.1、V7.1SP1

致远 OA V7.0、V7.0SP1、V7.0SP2、V7.0SP3

致远 OA V6.0、V6.1SP1、V6.1SP2

致远 OA V5.x

## 漏洞综合评级

严重

## 安全建议

致远OA官方已发布补丁完成漏洞修复：

[http://service.seeyon.com/patchtools/tp.html#/patchList?type=%E5%AE%89%E5%85%A8%E8%A1%A5%E4%B8%81&id=1](http://service.seeyon.com/patchtools/tp.html#/patchList?type=安全补丁&id=1)

## 工具利用

python3 seeyou_uploadexp.py -u http://127.0.0.1:1111 单个url测试

python3 seeyou_uploadexp.py -f url.txt 批量检测


## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。



