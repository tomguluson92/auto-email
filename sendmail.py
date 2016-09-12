# coding: utf-8

import time
import smtplib
import ConfigParser
from email.message import Message
from email.header import Header
from email.mime.text import MIMEText
import email
import sys
import os
import ast


class SendMail:

    def __init__(self, debug_level=0, mail_type='test'):
        self.mail_type = mail_type
        username = 'da-monitor@appchina.com'
        password = 'yyh94great!'
        directory = os.environ.get('MassQueryPath')
        self._default_config_path = directory + '/myemail/sendmail.cfg'
        self._smtp = smtplib.SMTP('smtp.partner.outlook.cn:587')
        #self._smtp = smtplib.SMTP('localhost')
        self._smtp.set_debuglevel(debug_level)
        self._smtp.ehlo()
        self._smtp.starttls()
        self._smtp.login(username, password)
        self._config_notification = False
        self.__set_default_config()

    def __set_default_config(self):
        config = ConfigParser.ConfigParser()
        config.read(self._default_config_path)
        self.set_config(config)

    def set_config(self, config):
        self._config_from_addr = config.get(self.mail_type, 'address')
        self._config_from_name = config.get(self.mail_type, 'name')
        self.subject = config.get(self.mail_type, 'subject')
        print self.subject
        self.toAddrs = ast.literal_eval(config.get(self.mail_type, 'mail_target'))

    def set_notification(self, boolvar):
        self._config_notification = boolvar

    def send_html(self, date, msgHtml, notify=False, charset='utf-8'):
        _from_addr = self._config_from_addr
        #_from_addr = "weizhigang@appchina.com"
        _from_name = self._config_from_name
        _msg = MIMEText(msgHtml, 'html', charset)
        _msg['Message-ID'] = email.utils.make_msgid()
        _msg['User-Agent'] = 'python smtplib v1.0'
        _msg['Date'] = email.utils.formatdate(time.time(), True)
        _msg['From'] = email.utils.formataddr(
            (str(Header(_from_name, charset)), _from_addr))
        _msg['Subject'] = Header(self.subject+'('+date+')', charset)

        if notify or self._config_notification:
            _msg['Disposition-Notification-To'] = email.utils.formataddr(
                (False, _from_addr))

        _toAddrs = []
        for toAddr in self.toAddrs:
            _toAddrs.append(email.utils.formataddr((False, toAddr)))
        _msg['To'] = ','.join(_toAddrs)

        print _from_addr
        self._smtp.sendmail(_from_addr, _toAddrs, _msg.as_string())
        self._smtp.quit()
        return
