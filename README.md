# auto-email
a easier and settable email-sender with multiple lines 
这个project是把定时任务发送任务的格式从附件的逗号分隔符文件转为HTML格式的正文输出
原因是：有的表格不是很大，用附件的形式一是不直观，二是如果每日收到附件数量太多，容易乱掉。
三是有的数据报表不适合做成dashboard

下面介绍一下原理：

step1：先分析脚本  sendreport.sh
#Generate new report
/usr/bin/python $MassQueryPath/demos/gen_${report_type}_report.py ${report_date}

这里,report_type、report_date分别是$1和$2，即sendreport.sh 后面跟的参数。这个语句表示执行demos文件夹下的gen_${report_type}_report.py
在本文件夹中，我没有分文件夹，而是只举出一个例子来说明。
step2: 打开gen_${report_type}_report.py
