# _*_ coding: utf-8 _*_

__author__ = 'GDH'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from mybasic import GenReport
from application import GetDownloadRedirectData
#GenReport、GetDownloadRedirectData是两个类：其中，GenReport是生成报告(HTML格式)， GetDownloadRedirectData是获取数据源。
class GenDownloadRedirectReport(GenReport.GenReport):

    def __init__(self, opt):
        super(GenDownloadRedirectReport, self).__init__(opt, 'bannercategory')
    
    #bannercategory.tpl是模板
    def gen_report(self):
        data = GetDownloadRedirectData.DownloadRedirectData(self.date)
        html = self.data2html(data.get_download_redirect_data(), 'bannercategory.tpl')
        self.html2file(html)



if __name__ == '__main__':
    obj = GenDownloadRedirectReport(sys.argv)

    print obj.gen_report()
