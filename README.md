# auto-email Python2.7
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
以我上传的gen_bannercategory-report.py为例
其代码如下：
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from mybasic import GenReport
from application import Data

class GenDownloadRedirectReport(GenReport.GenReport):

    def __init__(self, opt):
        super(GenDownloadRedirectReport, self).__init__(opt, 'bannercategory')

    def gen_report(self):
        data = Data.DownloadRedirectData(self.date)
        html = self.data2html(data.get_download_redirect_data(), 'bannercategory.tpl')
        self.html2file(html)
  这里，引入两个类：GenReport 和 Data
  其中，GenReport是生成报告(HTML格式)， Data是获取数据源。
  data2html是把从数据库得到的数据转换为HTML格式。Data是连接数据库得到数据，这个不在此放了。用户可以根据所使用的不同的数据库进行连接并且取得所需要的数据。html2file是把html变成一个叫bannercategory_report.html(在/demos/report/目录下)。
  其中具体代码参考GenReport
  
  ps：GenDownloadRedirectReport的opt参数就是${report_date}
  
  
  
  step3：打开send_report.py
  
  接下来，sendreport.sh的脚本要执行的任务是:
if [ -f $report ]; then
     cat $report | python $MassQueryPath/demos/send_report.py ${report_type} ${report_date}
else
     cat log | mail -s "no $report" 123@abc.com
fi

从$report的标准输出作为send_report.py的接受。这里$report就是由step2生成的bannercategory_report.html

send_report.py
和它所引用的sendmail.py都是不太难以理解的了。可以根据用户需要自行修改。


联系方式:qq314913739  tomguluson高
