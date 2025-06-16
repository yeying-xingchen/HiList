from fastapi import APIRouter
from common import config
import mariadb
import logging as log

router = APIRouter()

db_config = config.get_db_info()

try:
    conn = mariadb.connect(
        host=db_config["host"],
        port=db_config["port"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"],
    )
except mariadb.Error as e:
    log.error(f"数据库连接失败{e}")

@router.get("/list")
async def list():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM bucket")
        rows = cursor.fetchall()
        data = [{"id": row[0], "name": row[1]} for row in rows]
        return {
            "status": "success",
            "code": 200,
            "data": data
        }
    except mariadb.Error as e:
        return {
            "status": "error",
            "code": 500,
            "message": f"Database error: {e}"
        }