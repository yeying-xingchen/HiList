from fastapi import FastAPI
from router import bucket

app = FastAPI()

app.include_router(
    bucket.router,
    prefix="/bucket",
    tags=["bucket"]
)

@app.get("/")
async def root():
    return {
    "status": "success",
    "code": 200,
    "message": "HiList API is working!"
}
