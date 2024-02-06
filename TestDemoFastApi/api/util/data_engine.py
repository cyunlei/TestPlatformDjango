from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base
import databases

DATABASE_URL = "mysql+pymysql://root:123456@hadoop102:3306/cxx"


class BaseEngine:

    def __init__(self):
        self.database = databases.Database(DATABASE_URL)
        self.engine = create_engine(DATABASE_URL)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()
        self.create_all()
        self.database.disconnect().close()

    def create_all(self):
        self.Base.metadata.create_all(self.engine)

    def drop_all(self):
        self.Base.metadata.drop_all(self.engine)

    def get_session(self):
        return Session(self.engine)


baseEngine = BaseEngine()
