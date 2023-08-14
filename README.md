# HAC_Bored_Writing

各种未授权、RCE、文件上传、sql注入、信息泄露漏洞批量扫描poc、exp,跟踪最新漏洞实时更新,目前是把之前写的整合在一起,后续新增会在最下边加一个时间线，想看最新的poc、exp可以根据时间线来选择

## 2023

- [Panabit sy_addmount.php_rce](./RCE/Panabit)
- [任我行 CRM SmsDataList sql注入](./Sqlinject/任我行crm)
- [PigCMS action_flashUpload文件上传](./Fileupload/PigCMS)
- [用友GRP-U8 info.log信息泄露](./unauthorized/用友GRP-U8)
- [锐捷交换机 WEB 管理系统 EXCU_SHELL 信息泄露](./unauthorized/锐捷交换机WEB管理系统EXCU_SHELL)
- [大华智慧园区user_getUserInfoByUserName.action密码读取](./unauthorized/大华智慧园区密码读取)
- [大华智慧园区综合管理平台searchJson_sql注入](./Sqlinject/大华智慧园区综合管理平台searchJson)
- [绿盟 SAS堡垒机 Exec 远程命令执行漏洞](./RCE/lvmeng-SAS-Exec_RCE)
- [锐捷 NBR 路由器 fileupload.php文件上传](./Fileupload/Ruijie-NBR)
- [蓝凌oa custom.jsp文件读取](./FileRead/lanling_fileread)
- [深信服 应用交付管理系统 login_rce](./RCE/sangfor-login-rce)
- [通达oa CVE-2023-4166 sql注入](./Sqlinject/CVE-2023-4166)
- [泛微e-cology QVD-2023-5012 sql注入](./Sqlinject/QVD-2023-5012)
- [泛微e-Office CVE-2023-2648 任意文件上传](./Fileupload/cve-2023-2648)
- [用友NC Cloud jsinvoke_upload_rce](./RCE/Yongyou_NC_Cloud_upload_rce)
- [金蝶云星空_Unserialize_rce](./RCE/Kingdee_erp_Unserialize_rce)
- [Chamilo_CVE-2023-34960_RCE](./RCE/Chamilo__CVE-2023-34960_RCE)
- [畅捷通T+ QVD-2023-13612 sql注入](./Sqlinject/QVD-2023-13612)
- [H3C iMC_CVE-2023-34928_RCE](./RCE/CVE-2023-34928)
- [nginxWebUI_RCE](./RCE/nginxWebUI_rce)
- [用友时空KSOA /com.sksoft.bill.ImageUpload文件上传](./Fileupload/KSOA_upload)
- [Openfire CVE-2023-32315 未授权添加用户](./unauthorized/CVE-2023-32315)
- [jmreport/qurestSql CVE-2023-1454 sql注入](./Sqlinject/CVE-2023-1454)


## 2022

- [金山 V8 终端安全系统文件下载](./FileRead/jinshanv8_fileread)
- [CmsEasy sql注入](./Sqlinject/CmsEasy_sql)
- [用友U8-OA致远A6 getSessionList jsp信息泄露](./unauthorized/getSessionList_scan)
- [Doccms keyword sql注入](./Sqlinject/Doccms-sql-injection)
- [蓝海卓越计费管理系统 RCE](./RCE/lanhai_rce)


## 2021

- [ShopXO CNVD-2021-15822文件读取](./FileRead/CNVD-2021-15822)
- [Jellyfin CVE-2021-21402文件读取](./FileRead/CVE-2021-21402Jellyfin任意文件读)
- [FLIR-AX8 CNVD-2021-39018/download.php文件读取](./FileRead/FLIR-AX8_fileread)
- [Apache_solr任意文件读取](./FileRead/Apache_solr_fileread)
- [druid CVE-2021-34045未授权](./unauthorized/CVE-2021-34045)
- [会捷通云视讯 /fileDownload文件读取](./FileRead/会捷通云视讯任意文件读取)
- [Grafana CVE-2021-43798文件读取](./FileRead/Grafana_fileread)
- [泛微E-Office CNVD-2021-49104文件上传](./Fileupload/CNVD-2021-49104)
- [致远oaCNVD-2021-01627文件上传](./Fileupload/seeyon-oa-exp)
- [智慧校园管理系统 注册页面文件上传](./Fileupload/zhihuixiaoyuan_upload)
- [狮子鱼cms wxapp.php文件上传](./Fileupload/shiziyu_upload)
- [用友oa U8 test.jsp sql注入](./Sqlinject/yongyouU8_sql-main)


## 更早之前

- [Hadoop_未授权访问反弹shell](./unauthorized/hadoop_getshell)
- [银澎云计算 好视通视频会议系统CNVD-2020-62437](./FileRead/CNVD-2020-62437)
- [零视技术(上海)有限公司H5S CONSOLE CNVD-2020-67113未授权访问](./unauthorized/CNVD-2020-67113)
- [红帆OA iOffice.net udfmr.asmx sql注入](./Sqlinject/iOffice_sqlscan)
- [ZeroShell CVE-2019-12725RCE](./RCE/CVE-2019-12725)
- [源天OA GetDataAction sql注入](./Sqlinject/yuantian_sql)
- [Jupyter Notebook terminals未授权访问](./unauthorized/Jupyter-Notebook)
- [ApacheFlink_未授权访问上传jar包getshell](./unauthorized/ApacheFlink_poc)
- [ThinkCMF 文件包含getshell](./Fileupload/ThinkCMF_getshell_exp)


## 文件读取

任意文件读取，可读取服务器文件内容

#### 蓝凌oa

- [蓝凌oa custom.jsp文件读取](./FileRead/lanling_fileread)

#### 会捷通云视讯

- [会捷通云视讯 /fileDownload文件读取](./FileRead/会捷通云视讯任意文件读取)

#### FLIR-AX8

- [FLIR-AX8 CNVD-2021-39018/download.php文件读取](./FileRead/FLIR-AX8_fileread)

#### Jellyfin

- [Jellyfin CVE-2021-21402文件读取](./FileRead/CVE-2021-21402Jellyfin任意文件读)

#### Apache_solr

- [Apache_solr任意文件读取](./FileRead/Apache_solr_fileread)

#### ShopXO

- [ShopXO CNVD-2021-15822文件读取](./FileRead/CNVD-2021-15822)

#### Grafana

- [Grafana CVE-2021-43798文件读取](./FileRead/Grafana_fileread)

#### 金山v8

- [金山 V8 终端安全系统文件下载](./FileRead/jinshanv8_fileread)

#### 银澎云计算 好视通视频会议系统

- [银澎云计算 好视通视频会议系统CNVD-2020-62437](./FileRead/CNVD-2020-62437)

## 文件上传

可上传webshell，获取服务器权限

#### PigCMS

- [PigCMS action_flashUpload文件上传](./Fileupload/PigCMS)

#### 锐捷

- [锐捷 NBR 路由器 fileupload.php文件上传](./Fileupload/Ruijie-NBR)

#### 致远oa

- [seeyon /autoinstall.do.css/..;/ajax.do文件上传](./Fileupload/seeyon-oa-exp)

#### 用友时空KSOA

- [用友时空KSOA /com.sksoft.bill.ImageUpload文件上传](./Fileupload/KSOA_upload)

#### 泛微

- [泛微E-Office CNVD-2021-49104文件上传](./Fileupload/CNVD-2021-49104)
- [泛微e-Office CVE-2023-2648 任意文件上传](./Fileupload/cve-2023-2648)


#### 智慧校园管理系统

- [智慧校园管理系统 注册页面文件上传](./Fileupload/zhihuixiaoyuan_upload)

#### ThinkCMF

- [ThinkCMF 文件包含getshell](./Fileupload/ThinkCMF_getshell_exp)

## sql注入

通过SQL注入漏洞构造SQL注入语句，对服务器端返回特定的错误信息来获取有利用价值的信息，甚至可篡改数据库中的内容并进行提权

#### 任我行

- [任我行 CRM SmsDataList sql注入](./Sqlinject/任我行crm)

#### 大华智慧园区综合管理平台

- [大华智慧园区综合管理平台searchJson_sql注入](./Sqlinject/大华智慧园区综合管理平台searchJson)

#### 通达oa

- [通达oa CVE-2023-4166 sql注入](./Sqlinject/CVE-2023-4166)

#### 畅捷通T+

- [畅捷通T+ QVD-2023-13612 sql注入](./Sqlinject/QVD-2023-13612)

#### CmsEasy

- [CmsEasy sql注入](./Sqlinject/CmsEasy_sql)

#### Jeecg-Boot

- [jmreport/qurestSql CVE-2023-1454 sql注入](./Sqlinject/CVE-2023-1454)

#### Doccms

- [Doccms keyword sql注入](./Sqlinject/Doccms-sql-injection)

#### 红帆OA

- [红帆OA iOffice.net udfmr.asmx sql注入](./Sqlinject/iOffice_sqlscan)

#### 泛微

- [泛微e-cology QVD-2023-5012 sql注入](./Sqlinject/QVD-2023-5012)

#### 狮子鱼cms

- [狮子鱼cms wxapp.php文件上传](./Fileupload/shiziyu_upload)

#### 源天OA

- [源天OA GetDataAction sql注入](./Sqlinject/yuantian_sql)

#### 用友oa U8

- [用友oa U8 test.jsp sql注入](./Sqlinject/yongyouU8_sql-main)

## RCE命令执行

攻击者可以执行任意系统命令

#### Panabit

- [Panabit sy_addmount.php_rce](./RCE/Panabit)

#### 绿盟

- [绿盟 SAS堡垒机 Exec 远程命令执行漏洞](./RCE/lvmeng-SAS-Exec_RCE)

#### 深信服

- [深信服 应用交付管理系统 login_rce](./RCE/sangfor-login-rce)

#### 用友NC Cloud

- [用友NC Cloud jsinvoke_upload_rce](./RCE/Yongyou_NC_Cloud_upload_rce)

#### 金蝶云星空

- [金蝶云星空_Unserialize_rce](./RCE/Kingdee_erp_Unserialize_rce)

#### 学习管理系统Chamilo

- [Chamilo_CVE-2023-34960_RCE](./RCE/Chamilo__CVE-2023-34960_RCE)

#### H3C

- [H3C iMC_CVE-2023-34928_RCE](./RCE/CVE-2023-34928)

#### nginxWebUI

- [nginxWebUI_RCE](./RCE/nginxWebUI_rce)

#### 蓝海卓越计费管理系统

- [蓝海卓越计费管理系统 RCE](./RCE/lanhai_rce)

#### ZeroShell

- [ZeroShell CVE-2019-12725RCE](./RCE/CVE-2019-12725)

#### 浪潮

- [浪潮ClusterEngineV4.0 CVE-2020-21224 RCE](./RCE/CVE-2020-21224)

#### TamronOS IPTV系统

- [TamronOS IPTV系统 RCE](./RCE/TamronOS-IPTV-RCE)

## 未授权访问

未授权就可访问指定资源

#### 大华智慧园区

- [大华智慧园区user_getUserInfoByUserName.action密码读取](./unauthorized/大华智慧园区密码读取)

#### 锐捷

- [锐捷交换机 WEB 管理系统 EXCU_SHELL 信息泄露](./unauthorized/锐捷交换机WEB管理系统EXCU_SHELL)

#### 用友

- [用友GRP-U8 info.log信息泄露](./unauthorized/用友GRP-U8)

#### H5S CONSOLE

- [零视技术(上海)有限公司H5S CONSOLE CNVD-2020-67113未授权访问](./unauthorized/CNVD-2020-67113)

#### druid

- [druid CVE-2021-34045未授权](./unauthorized/CVE-2021-34045)

**致远oa**

- [致远oa webmail.do文件泄露敏感信息](./unauthorized/seeyou_webmail.do_scan)
- [用友U8-OA致远A6 getSessionList jsp信息泄露](./unauthorized/getSessionList_scan)

**华夏erp**

- [华夏erp getAllList敏感信息泄露](./unauthorized/huaxia_erp_scan)

**Jupyter-Notebook**

- [Jupyter Notebook terminals未授权访问](./unauthorized/Jupyter-Notebook)

#### ApacheFlink

- [ApacheFlink_未授权访问上传jar包getshell](./unauthorized/ApacheFlink_poc)

#### Hadoop

- [Hadoop_未授权访问反弹shell](./unauthorized/hadoop_getshell)

#### Openfire

- [Openfire CVE-2023-32315 未授权添加用户](./unauthorized/CVE-2023-32315)


## 免责声明

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。



