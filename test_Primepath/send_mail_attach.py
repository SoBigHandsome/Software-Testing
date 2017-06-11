# encoding=utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtpserver = 'smtp.163.com'
# 发送邮箱用户/密码
user = 'a20121012133@163.com'
password = 'kjzzxj'
# 发送邮箱
sender = 'a20121012133@163.com'
# 接收邮箱
receiver = '18303974@qq.com'
# 发送邮件主题
subject = '功能自动化测试报告翟晓军'

# 发送的附件
sendfile = open('report-Testprime2017-06-04 15-35-26-result.html', 'rb').read()

# 创建一个带附件的实例
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = Header(subject, 'utf-8')                         # 定义邮件标题
# 需要添加这两个赋值
msgRoot['From'] = sender
msgRoot['To'] = receiver

# 邮件正文内容
msgRoot.attach(MIMEText('你好这是我的报告!', 'plain', 'utf-8'))

# 构造附件
att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="report-Testprime2017-06-04 15-35-26-result.html"'
msgRoot.attach(att)

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()