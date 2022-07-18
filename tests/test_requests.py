import asyncio


from neko import NekoClient


async def test_generate_image(client):
    image = await client.generate_image('baguette', 'https://images.unsplash.com/photo-1453728013993-6d66e9c9123a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8dmlld3xlbnwwfHwwfHw%3D&w=1000&q=80')
    print(image.url)


async def start_tests():
    print('Starting tests...')
    client = NekoClient()
    await test_generate_image(client)
    await client.close()
    

asyncio.run(start_tests())
