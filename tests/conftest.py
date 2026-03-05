import pytest_asyncio
from httpx import AsyncClient , ASGITransport
from app.main import app
from asgi_lifespan import LifespanManager

@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            yield ac