# ThinkCMF_getshell 框架上的任意内容包含漏洞

远程攻击者在无需任何权限情况下，通过构造特定的请求包即可在远程服务器上执行任意代码。

## python usage:
python3 ThinkCMF_getshell_exp.py -u http://127.0.0.1:1111 单个url测试

python3 ThinkCMF_getshell_exp.py -f url.txt 批量检测

## 修复方法
将 
`HomebaseController.class.php` 和 `AdminbaseController.class.php` 类中 `display` 和 `fetch` 函数的修饰符改为 `protected`

## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。
