# _*_ coding: utf-8 _*_

__author__ = 'GDH'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from mybasic import GenReport
from application import GetDownloadRedirectData

class GenDownloadRedirectReport(GenReport.GenReport):

    def __init__(self, opt):
        super(GenDownloadRedirectReport, self).__init__(opt, 'bannercategory')

    def gen_report(self):
        data = GetDownloadRedirectData.DownloadRedirectData(self.date)
        html = self.data2html(data.get_download_redirect_data(), 'bannercategory.tpl')
        self.html2file(html)



if __name__ == '__main__':
    obj = GenDownloadRedirectReport(sys.argv)

    print obj.gen_report()