import aiohttp


class MyClass:
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    async def my_function(self):
        async with self.session.post('https://example.com') as resp:
            return await resp.json()
