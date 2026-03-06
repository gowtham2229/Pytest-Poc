import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from asgi_lifespan import LifespanManager
from ..main import app


@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)

    async with LifespanManager(app):
        async with AsyncClient(
            transport=transport,
            base_url="http://test"
        ) as ac:
            yield ac