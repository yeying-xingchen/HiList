from fastapi import APIRouter
from common import config
import mariadb

router = APIRouter()

db_config = config.get_db_info()
conn = mariadb.connect(
    host=db_config.host,
    port=db_config.port,
    database=db_config.database,
    user=db_config.user,
    password=db_config.password,
)

@router.get("/list")
async def list():
    return {
    "status": "success",
    "code": 200,
    "data": [{"id": 1, "name": "Test"}]
    }