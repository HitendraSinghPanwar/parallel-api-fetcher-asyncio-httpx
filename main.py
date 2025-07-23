import asyncio
import httpx
import time

URLS = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums",
    "https://jsonplaceholder.typicode.com/photos",
    "https://jsonplaceholder.typicode.com/todos",
    "https://jsonplaceholder.typicode.com/users"
]

async def fetch(client, url):
    response = await client.get(url)
    data = response.json()
    return data

async def main():
    start = time.time()

    async with httpx.AsyncClient() as client:
        data = [fetch(client, url) for url in URLS]
        results = await asyncio.gather(*data)
        print(results)


    end = time.time() 
    print(f"time taken: {end - start:.2f} seconds")
asyncio.run(main())
