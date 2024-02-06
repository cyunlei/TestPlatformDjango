from sqlalchemy import Column, Integer, String, MetaData, Table


metadata = MetaData()


# 如果只需要返回特定的字段，则只需定义特殊的模型即可
# 定义你的表和模型
class UserEntity:
    users = Table('cxx_user', metadata,
                  Column('uid', Integer, primary_key=True, nullable=False),
                  Column('u_account', String(20), nullable=False),
                  Column('u_name', String(20), nullable=False),
                  Column('u_passwd', String(20), nullable=False),
                  Column('u_phone', String(20), nullable=False),
                  Column('u_sex', String(20), nullable=False),
                  Column('u_address', String(20), nullable=False),
                  Column('u_token', String(20), nullable=False),
                  Column('create_time', String(20), nullable=False),
                  Column('u_email', String(20), nullable=False)
                  )


userEntity = UserEntity()
