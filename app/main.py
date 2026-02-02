from fastapi import FastAPI
import uvicorn
from app.core.config import settings
from app.routers import health


app=FastAPI()

app.include_router(health.router)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", 
        host=settings.APP_HOST, 
        port=settings.APP_PORT, 
        reload=True
    )