import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
from random import randint
import redis
from util.code import code as response_code
import json


class SendEmail:
    def __init__(self, recipient_email):
        """
        :param recipient_email: 接收者邮箱
        :param subject: 邮件主题
        :param body: 邮件内容
        """
        # self.sender_email = 'cyunlei9@163com'
        # self.sender_password = 'VZBTYBTLILDCBAEM'
        # aB18330130802!
        self.sender_email = 'LYKJYXGSCN@yeah.net'
        self.sender_password = 'YUEFGPZDWUAMLYUC'
        self.recipient_email = recipient_email
        self.X = '雷云科技'
        self.redis_host = 'localhost'
        self.redis_port = 6379
        self.redis_db = 0
        self.r = redis.Redis(host=self.redis_host, port=self.redis_port, db=self.redis_db)
        self.at_time = round(time.time())
        self.server = smtplib.SMTP('smtp.yeah.net')
        # self.server = smtplib.SMTP('smtp.163.com')

    def login_email(self):
        # 连接到 SMTP 服务器
        try:
            self.server.starttls()
            self.server.login(self.sender_email, self.sender_password)
        except Exception as e:
            return json.dumps(
                {'code': response_code.SYSTEM_ERROR, 'msg': response_code.SYSTEM_ERROR_MSG, 'error': e},
                ensure_ascii=False)
        # 登录邮箱

    def send_email(self):
        self.login_email()

        try:
            u_code = self.get_code(self.recipient_email)
            if u_code:
                self.email_code(u_code)
            else:
                self.email_code(self.set_code(self.recipient_email))
        except Exception as e:
            return json.dumps(
                {'code': response_code.SYSTEM_ERROR, 'msg': response_code.SYSTEM_ERROR_MSG.join(': {}').format(e)},
                ensure_ascii=False)
        else:
            return json.dumps({'code': response_code.SUCCESS_CODE, 'msg': response_code.MSG}, ensure_ascii=False)
        finally:
            self.close_email()

    def close_email(self):
        # 关闭链接
        self.server.close()

    def email_code(self, code):
        title = '{} 是您的验证码'.format(code)
        content = '您的验证码是：{}，请不要把验证码泄露给其他人,5分钟内有效！。如非本人操作，可不用理会！'.format(code)
        # 创建MIMEText对象，分别指定HTML内容、类型（文本或html）、字符编码
        # 创建 MIMEText 对象
        msg = MIMEText(content)
        msg['Subject'] = title
        msg['From'] = formataddr((self.X, self.sender_email))
        msg['To'] = self.recipient_email
        # msg['X-Sender']=self.X
        # 发送邮件
        try:
            self.server.send_message(msg)
        except Exception as e:
            return json.dumps(
                {'code': response_code.SYSTEM_ERROR, 'msg': response_code.SYSTEM_ERROR_MSG},
                ensure_ascii=False)
        else:
            return json.dumps({'code': response_code.SUCCESS_CODE, 'msg': response_code.MSG}, ensure_ascii=False)

    def set_code(self, email):
        randoms_int = randint(100000, 999999)
        v_time = self.at_time + (30 * 60)
        vt = str(randoms_int) + '.' + str(v_time)
        self.r.set(email, vt)
        self.r.expireat(email, int(v_time))
        self.r.close()
        return randoms_int

    def get_code(self, email):
        ut = self.r.get(email)
        self.r.close()
        if ut:
            ut = str(ut).split('.')
            u_code = int(ut[0].strip("b'"))
            u_time = int(ut[1].strip("'"))
            if u_time > self.at_time:
                return u_code  # 有效
            else:
                return False
        else:
            return False


class MessageCode:
    def __init__(self):
        # self.code = code
        # self.email = email
        self.redis_host = 'localhost'
        self.redis_port = 6379
        self.redis_db = 0
        self.r = redis.Redis(host=self.redis_host, port=self.redis_port, db=self.redis_db)
        self.at_time = round(time.time())

    def get_code(self, email, code):
        ut = self.r.get(email)
        self.r.close()
        if ut:
            ut = str(ut).split('.')
            u_code = int(ut[0].strip("b'"))
            u_time = int(ut[1].strip("'"))
            if len(str(code)) == 6:
                if int(code) == u_code:
                    if u_time > self.at_time:
                        return True  # 有效
                    else:
                        return 5
                else:
                    return 4
            else:
                return 3
        else:
            return 2


sendEmail = SendEmail
messageCode = MessageCode
# sn = messageCode('cyunlei9156468512@163.com', 888815).get_code()
# print(sn)
sendEmail(recipient_email='cyunlei9@163.com')
