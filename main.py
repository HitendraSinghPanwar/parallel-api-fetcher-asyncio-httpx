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
    try:
        response = await client.get(url, timeout=10.0)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as e:
        print(f"Request error for {url}: {e}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error for {url}: {e.response.status_code}")
    except Exception as e:
        print(f"Unexpected error for {url}: {e}")
    return None

async def main():
    start = time.time()

    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, url) for url in URLS]
        results = await asyncio.gather(*tasks)
        print(results)

    end = time.time()
    print(f"time taken: {end - start:.2f} seconds")

asyncio.run(main())
