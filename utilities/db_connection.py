from sqlalchemy.ext.asyncio import create_async_engine , AsyncSession
from sqlalchemy.orm import sessionmaker , declarative_base

database_url = "sqlite+aiosqlite:///./Poc.db"  # Replace with your actual database URL
engine = create_async_engine(database_url)
AsyncSessionLocal = sessionmaker(class_=AsyncSession, bind=engine , expire_on_commit=False)

Base = declarative_base()
async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()

