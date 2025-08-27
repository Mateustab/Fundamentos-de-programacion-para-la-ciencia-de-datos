import asyncio
import time
import aiohttp

image_urls = [
    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800",
    "https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=800",
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800",
    "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/jpeg"
] *25

async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


async def main():
    sites = image_urls
    start_time = time.time()
    await asyncio.create_task(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Descarga con asyncio:{len(sites)} en {duration:.2f} segundos")


if __name__ == "__main__":
    asyncio.run(main())