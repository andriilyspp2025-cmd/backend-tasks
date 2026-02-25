from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.logger import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    logger.info("Application is starting up...")
    
    yield
    
    # Shutdown logic
    logger.info("Application is shutting down...")
    
