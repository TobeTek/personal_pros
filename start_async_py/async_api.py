import aiohttp
import asyncio
import utils 

async def aio_create_new_avatar(client_session:aiohttp.ClientSession, avatar_style:str, base_url:str):    
    seed = utils.generate_random_seed()
    request_url = utils.generate_api_url(seed=seed, avatar_style=avatar_style, base_url=base_url)
    async with client_session.get(request_url) as resp:
        data = await resp.read()
    utils.write_to_file(data=data, file_name=seed, file_path=r"C:/Users/user/desktop/pp")
