from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
    "status": "success",
    "code": 200,
    "message": "HiList API is working!"
}