# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 08:54:36 2017

@author: Yangzj
"""

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
from bs4 import BeautifulSoup
import requests 

html = requests.get('https://gupiao.baidu.com/stock/sh000001.html?from=aladingpc').content
soup = BeautifulSoup(html, 'lxml')
data=soup.select('._close ')[0].get_text().strip()

print(data);

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '317493138@qq.com' #input('From: ')
password = 'hjedkjoxfivrcaij'#input('Password: ')
to_addr = '317493138@qq.com'#input('To: ')
smtp_server = 'smtp.qq.com'#input('SMTP server: ')

msg = MIMEText(data, 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP_SSL("smtp.qq.com", 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
