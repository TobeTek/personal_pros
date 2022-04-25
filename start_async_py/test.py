import asyncio 

from timeit import default_timer as timer

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def wait_for_some_time(n):
    await asyncio.sleep(n)
    print(f"Done Sleeping {n=} :P")

async def main():
    tasks = [wait_for_some_time(i) for i in range(1, 4)] # 1 - 3 
    await asyncio.gather(*tasks)

start = timer()
asyncio.run(main())
print(f"Time Elapsed: {timer()-start} seconds")
