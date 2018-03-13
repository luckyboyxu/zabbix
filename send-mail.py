#邮件发送脚本
#!/user/bin/python
#coding:utf-8

import smtplib
from email.mime.text import MIMEText
import sys
mail_host = 'mail.xxx.com'
mail_user = 'xxx'
mail_pass = 'xxx'
mail_postfix = 'xxx.com'

def send_mail(to_list, subject, content):
  me = "zabbix 监控告警平台"+"<"+mail_user+"@"+mail_postfix+">"
  msg = MIMEText(content, 'plain', 'utf-8')
  msg['Subject'] = subject
  msg['From'] = me
  msg['to'] = to_list
  try:
    s = smtplib.SMTP()
    s.connect(mail_host)
    s.sendmail(me, to_list, msg.as_string()){ALERT.MESSAGE}
    s.close()
    return True
  except Exception, e:
    print str(e)
    return False
if __name__ == "__main__":
  send_mail(sys.argv[1], sys.argv[2], sys.argv[3])
  
  
  
备注：传入函数的三个参数是在zabbix邮件监控页面设置的宏{ALERT.SENDTO}, {ALERT.SUBJECT}, {ALERT.MESSAGE}
