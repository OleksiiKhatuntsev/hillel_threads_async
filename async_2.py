import asyncio
import time


async def async_function():
    await asyncio.sleep(0.5)
    print("AWAIT")
    return 2


async def func_2():
    await async_function()
    await async_function()
    print("AFTER RUN")

print(asyncio.run(func_2()))