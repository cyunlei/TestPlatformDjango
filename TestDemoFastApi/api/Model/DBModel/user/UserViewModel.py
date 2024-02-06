from pydantic import BaseModel


# 定义返回模型


class UserToken(BaseModel):
    u_name: str
    u_phone: str


# 定义登录成功后返回的数据模型
class LoginListResponse(BaseModel):
    code: int
    msg: str
    UserToken: list[UserToken]


class TokenAccount(BaseModel):
    account: str


class product_list_l(BaseModel):
    product_id: int
    product_name: str
    product_size: str
    product_color: str
    product_system: str
    product_price: str
    phone_number: str
    phone_putaway_time: str


class product_list(BaseModel):
    code: int
    msg: str
    product_list: list[UserToken]


class UserModel(BaseModel):
    u_email: str
    u_account: str
    u_name: str
    u_passwd: str
    u_phone: str
    u_sex: str
    u_address: str
    u_token: str
    create_time: str