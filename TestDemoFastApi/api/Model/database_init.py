from api import router
from api.util.data_engine import baseEngine


@router.on_event("startup")
async def startup():
    # 初始化数据库连接
    await baseEngine.database.connect()


@router.on_event("shutdown")
async def shutdown():
    # 关闭数据库连接
    await baseEngine.database.disconnect()
