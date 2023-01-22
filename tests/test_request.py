import asyncio
import pytest
from aiohttp_mock import AiohttpMock


@pytest.mark.asyncio
async def test_post():
    async def mock_response(req):
        return 200, {}, '{"key": "value"}'

    url = 'https://example.com/api/endpoint'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_TOKEN"
    }
    data = [
        {"key1": "value1", "key2": "value2"},
        {"key3": "value3", "key4": "value4"},
        {"key5": "value5", "key6": "value6"},
        # ...
    ]

    mock = AiohttpMock(post=mock_response)
    with mock:
        async with aiohttp.ClientSession() as session:
            # use asyncio.gather to parallelize requests
            results = await asyncio.gather(*(post(session, url, d, headers) for d in data))
            assert results == [{"key": "value"}]*len(data)
