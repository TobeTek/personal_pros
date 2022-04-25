import aiohttp
import asyncio

import async_api
import sync_api

from timeit import default_timer as timer

BASE_URL = "https://avatars.dicebear.com/api/{avatar_style}/{seed}"

ALL_STYLES = [
    "adventurer",
    "adventurer-neutral",
    "avataaars",
    "big-ears",
    "big-ears-neutral",
    "big-smile",
    "botts",
    "croodles",
    "micah"
]


def generate_profile_pics(n):
    for _ in range(n):
        sync_api.create_new_avatar(avatar_style="adventurer", base_url=BASE_URL)
        pass


async def async_generate_profile_pics(n):
    Client = aiohttp.ClientSession()
    Tasks = []

    
    for _ in range(n):
        # Create a new profile pic
        Tasks.append(async_api.aio_create_new_avatar(client_session=Client, avatar_style="big-smile", base_url=BASE_URL))
        
    try:
        await asyncio.gather(*Tasks)

    except:
        pass

    finally:
        await Client.close()



start = timer()
generate_profile_pics(20)
print(f"Time Elapsed: {timer()-start} seconds")


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
start = timer()
asyncio.run(async_generate_profile_pics(20))
print(f"Time Elapsed: {timer()-start} seconds")
