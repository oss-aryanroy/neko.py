from typing import Optional

import aiohttp

class _HTTPClient:
    def __init__(
        self, 
        session: Optional[aiohttp.ClientSession] = None
    ) -> None:
        self.session = session

    async def get(self, url: str, **params) -> aiohttp.ClientResponse:
        if not self.session or self.session.closed:
            self.session = aiohttp.ClientSession()
        return await self.session.get(url, **params)

    async def close(self) -> None:
        if self.session:
            await self.session.close()
