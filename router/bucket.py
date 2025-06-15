from fastapi import APIRouter

router = APIRouter()

@router.get("/list")
async def list():
    return {
    "status": "success",
    "code": 200,
    "data": [{"id": 1, "name": "Test"}]
    }