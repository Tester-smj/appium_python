#coding = utf-8
from email.mime.text import MIMEText
from email.header import Header
import smtplib


def send_mail(file_new):
    '''发送测试报告，需要配置你的邮箱账号'''
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From']= 'mengjie.shi@zhongke100.com'
    msg['To']= 'mengjie.shi@zhongke100.com'
    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    smtp.login("811504083@qq.com", "112345454")
    smtp.sendmail("shimj@intuntrip.com","shimj@intuntrip.com",msg.as_string())
    smtp.quit()
    print('email has send out!')