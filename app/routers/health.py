from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from redis.asyncio import Redis
from app.db.db import get_db
from app.utils.redis_client import get_redis_client
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/healthcheck", tags=["Healthcheck"])
async def health_check(
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
        logger.error(f"Healthcheck error: {e}")
        raise HTTPException(status_code=500, detail=f"Infrastructure connection error: {e}")
