from fastapi import FastAPI
from DB.Model.UserBaseModel import User

app = FastAPI()


@app.post('/login')
def login(User: User):
    pass
