import redis.asyncio as redis
from app.core.config import settings

REDIS_URL = settings.REDIS_URL

async def get_redis_client():

    client = redis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
    try:
        yield client
    finally:
        await client.close()