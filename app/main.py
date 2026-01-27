from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from redis.asyncio import Redis
import uvicorn
from app.db.db import get_db
from app.utils.redis_client import get_redis_client

app=FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
}

@app.get("/api/healthchecker")
async def health_checker(
    db: AsyncSession = Depends(get_db),
    r: Redis = Depends(get_redis_client)
):
    try:
        result = await db.execute(text("SELECT 1"))
        pg_status = result.scalar()

        if pg_status is None:
            raise HTTPException(status_code=500, detail="Database connection error")

        await r.set("test_key", "Redis Works!")
        redis_val = await r.get("test_key")

        return {
            "status": "success",
            "message": "Systems are operational",
            "postgres": "connected",
            "redis": f"connected, value: {redis_val}"
        }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Infrastructure connection error: {e}")


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)