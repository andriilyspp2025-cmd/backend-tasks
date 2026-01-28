from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import os
from app.routers import health

load_dotenv()

app=FastAPI()

app.include_router(health.router)

if __name__ == "__main__":
    HOST = os.getenv("APP_HOST", "127.0.0.1")
    PORT = int(os.getenv("APP_PORT", 8000))
    
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)
