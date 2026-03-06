from utilities import get_db , engine , Base , AsyncSession
from config import Task
from routers import router
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/Home")
async def home():
    return {"message":"Welcome to Task Management API"}










app.include_router(router=router, tags=["Tasks"])
