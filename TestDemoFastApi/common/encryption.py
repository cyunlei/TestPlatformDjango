import jwt
import time, os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import hashlib


class Encryption:
    def __init__(self, account=None, token=None, password=None):
        self.secret_key = 'CYUNLEI9@163.COM_KEY'
        self.algorithm = 'HS256'
        self.expire_start_time = round(time.time() * 1000)
        self.account = account
        self.payload = {
            'account': self.account,
            'exp': round(self.expire_start_time + 1000 * 60 * 60 * 24 * 7)
        }
        self.token = token
        self.path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), r'common\secret_key')
        self.password = password

    def token_encode(self):
        return jwt.encode(self.payload, self.secret_key, algorithm=self.algorithm)

    def token_decode(self):
        try:
            jwt_token = jwt.decode(self.token, self.secret_key, algorithms=self.algorithm)
        except Exception as e:
            return 'token验证失败，错误原因：{}'.format(e)
        else:
            if self.expire_start_time < jwt_token['exp']:
                # 'token验证成功' 返回为真
                return True
            else:
                # 'token验证失败' 返回为假
                return False

    def token_account_decode(self):
        try:
            token_decode=jwt.decode(self.token, self.secret_key, algorithms=self.algorithm)
        except Exception as e:
            return False
        return token_decode['account']

    def create_rsa_encode(self):
        # 生成RSA密钥对
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=1024)
        with open(self.path + "/" + 'private_key.pem', 'wb') as f:
            # 保存私钥到文件
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
        public_key = private_key.public_key()
        with open(self.path + "/" + 'public_key.pem', 'wb') as f:
            # 保存公钥到文件
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            ))

    def read_rsa_encode(self):
        with open(self.path + "/" + 'private_key.pem', 'rb') as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None
            )
        with open(self.path + "/" + 'public_key.pem', 'rb') as f:
            public_key = serialization.load_pem_public_key(
                f.read()
            )
        return private_key, public_key

    def pwd_encode(self):
        # 生成RSA密钥对
        private_key, public_key = self.read_rsa_encode()
        # 使用公钥加密
        encrypted_password = public_key.encrypt(
            self.password.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_password

    def pwd_decode(self):
        # 生成RSA密钥对
        private_key, public_key = self.read_rsa_encode()
        # 使用私钥解密
        decrypted_password = private_key.decrypt(
            self.password,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_password

    def md5(self):
        # md5加密
        return hashlib.md5(self.password.encode()).hexdigest()


ep = Encryption
# # token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50IjoiMTUxMTAyNjQxMjEiLCJleHAiOjE3MDU0NzY5NDM1NTJ9.DzNU_DMf8GF9c6EmoMChBXgfQj8mEtoTcF0VdNuDlKA'
# a='123456'
# s=ep(password=a).md5()
# print(s)
# decode_token = ep(token=token).token_account_decode()
# print(decode_token)
