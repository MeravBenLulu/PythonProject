import asyncio
import datetime


async def print_hi(name, delay):
    await asyncio.sleep(delay)
    if name == "Sara":
        raise Exception("oopsss")
    return f'Hi, {name}'


async def main():
    print(f'time: {datetime.datetime.now()}')
    res = await asyncio.gather(print_hi("Sara", 1), print_hi("Rut", 2), return_exceptions=True)
    print(f'time: {datetime.datetime.now()}')
    print(res)


asyncio.run(main())
