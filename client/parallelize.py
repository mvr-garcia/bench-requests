import asyncio
import aiohttp
import time


async def post(session, url, data):
    async with session.post(url, json=data) as response:
        if response.status != 200:
            print(f"Request to {url} returned status code {response.status}. Response will be None")
            return None
        return await response.json()


async def main():
    url = "http://0.0.0.0:8000/items/"

    sample = {
        "name": "Marcos",
        "description": "Garcia",
        "price": 10,
        "tax": 2
    }
    data = [sample for _ in range(1000)]

    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        # use asyncio.gather to parallelize requests
        results = await asyncio.gather(*(post(session, url, d) for d in data))
        for result in results:
            print(result)

    end = time.perf_counter()
    print("Time taken: ", end - start)


asyncio.run(main())
