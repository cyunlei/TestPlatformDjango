from pydantic import BaseModel, EmailStr


# 用户模型
class User(BaseModel):
    uid: int
    income_uid: int
    parent_id: int
    company_id: int
    account: str
    pwd: str
    real_name: str
    birthday: int
    card_id: str
    mark: str
    partner_id: int
    group_id: int
    nickname: str
    avatar: str
    phone: str
    add_time: int
    add_ip: str
    last_time: int
    last_ip: str
    now_money: float
    brokerage_price: float
    integral:int
    new_integral:int
    reward:int
    exp:float
    sign_num:int
    status:int
    is_company:int
    is_agent:int
    is_del:int
    level:int
    is_money_level:int
    is_first_register:int
    flag:int
    uuid:int
    balance:int

