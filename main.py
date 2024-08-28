import asyncio
from prisma import Prisma

async def main() -> None:
    # doma 
    # pip install prisma
    # prisma db push
    prisma = Prisma()
    await prisma.connect()

    # write your queries here
    #await prisma.query_raw('INSERT INTO fruits_and_vegi(name) VALUES(?)', 'pineapple')

    els = await prisma.query_raw('SELECT * FROM fruits_and_vegi')
    print(els)
    
    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())