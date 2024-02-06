from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def insert_img(driver, filename):
    func_path = os.path.dirname(__file__)

    base_dir = os.path.dirname(func_path)

    base_dir = str(base_dir).replace('\\', '/')

    base = base_dir.split('/Website')[0]
    filepath = base + '/Website/test_report/screenshot/' + filename

    driver.get_screenshot_as_file(filepath)


def send_email(latest_report):
    f = open(latest_report, 'rb')
    email_content = f.read()
    f.close()

    smtpserver = 'smtp.163.com'
    user = 'cyunlei9@163.com'
    password = 'a18330130802'
    sender = 'cyunlei9@163.com'
    receives = ['cyunlei1@163.com', 'cyunlei3@163.com']
    subject = 'web  selenium 自动化实战'
    msg = MIMEText(email_content,'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)
    print('start send email ....')
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()


def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print('the latest report is ' + lists[-1])
    file = os.path.join(report_dir, lists[-1])
    return file


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver, 'sougou1.png')
    driver.quit()
