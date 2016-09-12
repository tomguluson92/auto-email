#!/bin/env python
# encoding: utf8

import sys
from datetime import datetime, timedelta
from myemail.sendmail import SendMail


def main():
    report_type = sys.argv[1] or 'test'
    report_date = None if len(sys.argv) != 3 else sys.argv[2]
    print report_date
    if report_date is None:
        tmp_date = datetime.now() - timedelta(days=1)
    else:
        tmp_date = datetime.strptime(report_date, "%Y%m%d")

    stdin = sys.stdin
    content = ''
    cur_date = tmp_date.strftime('%Y-%m-%d')
    print cur_date
    for i in stdin:
        content += i
    m = SendMail(mail_type=report_type)
    m.send_html(cur_date, content)


if __name__ == '__main__':
    main()
