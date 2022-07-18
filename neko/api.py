from contextlib import AbstractAsyncContextManager
from typing import List, Literal, Optional

import aiohttp

from .client import _HTTPClient
from .models import Image

Possible = Literal['threats', 'baguette', 'clyde', 'ship', 'captcha', 'whowouldwin',
                               'changemymind', 'ddlc', 'jpeg', 'lolice', 'kannagen',
                               'iphonex', 'kms', 'animeface', 'awooify', 'trap', 'nichijou',
                               'trumptweet', 'tweet', 'kidnap', 'deepfry', 'blurpify', 'phcomment',
                               'magik', 'osu', 'clickforhentai', 'fact', 'trash', 'stickbug']


class NekoClient(AbstractAsyncContextManager):
    BASE = "https://nekobot.xyz/api"

    POSSIBLE_ENDPOINTS = [
        'threats', 'baguette', 'clyde', 'ship', 'captcha', 'whowouldwin',
        'changemymind', 'ddlc', 'jpeg', 'lolice', 'kannagen',
        'iphonex', 'kms', 'animeface', 'awooify', 'trap', 'nichijou',
        'trumptweet', 'tweet', 'kidnap', 'deepfry', 'blurpify', 'phcomment',
        'magik', 'osu', 'clickforhentai', 'fact', 'trash', 'stickbug'
    ]

    def __init__(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        self._client = _HTTPClient(session)

    async def generate_image(self, endpoint: Possible, url: str, **kwargs) -> Image:
        if endpoint not in self.POSSIBLE_ENDPOINTS:
            raise ValueError(f"{endpoint} is not a valid endpoint")
        url = f"{self.BASE}/imagegen?type={endpoint}&url={url}"
        response = await self._client.get(url, **kwargs)
        json_data = await response.json()
        return Image(json_data['message'])

    @property
    def get_all_endpoints(self) -> List[str]:
        return self.POSSIBLE_ENDPOINTS

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> 'NekoClient':
        if not self._client.session:
            self._client.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._client.close()
