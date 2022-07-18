# Neko.py
`pip install neko.py`

A Python API Wrapper for [NekoBot API](https://docs.nekobot.xyz/#image-generation-threats)

# usage

```py
import neko

client = neko.NekoClient()

async def get_image():
    image = await client.generate_image('baguette', 'https://example.com/image.jpg')
    return image.url


async def main():
    image_url = await get_image()
    print(image_url)

asyncio.run(main())
```
