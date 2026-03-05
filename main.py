from utilities import get_db , engine , Base , AsyncSession
from config import Task
from routers import router
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/Home")
async def home():
    return {"message":"Welcome to Task Management API"}




# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


# if __name__ == "__main__":
#     asyncio.run(init_db())
#     print("Database initialized successfully.")


app.include_router(router=router, tags=["Tasks"])
