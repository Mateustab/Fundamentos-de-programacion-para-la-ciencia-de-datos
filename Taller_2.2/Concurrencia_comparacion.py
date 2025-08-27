import requests
import time
import concurrent.futures
import threading
import asyncio
import aiohttp
import multiprocessing

# Definición de URLs de imágenes
image_urls = [
    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800",
    "https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=800",
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800",
    "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/jpeg"
] *25

#----------------------Synchronous------------------------------------------------------------------------

def download_siteSynchronous(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} bytes from {url}")

def download_all_sitesSynchronous(sites):
    with requests.Session() as session:
        for url in sites:
            download_siteSynchronous(url, session)

#----------------------Threading------------------------------------------------------------------------

thread_local = threading.local()

def get_sessionThreading():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_siteThreading(url):
    session = get_sessionThreading()
    with session.get(url) as response:
        print(f"Read {len(response.content)} bytes from {url}")

def download_all_sitesThreading(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_siteThreading, sites)

#----------------------Asyncio--------------------------------------------------------------------------

async def download_siteAsyncio(session, url):
    async with session.get(url) as response:
        print(f"Read {response.content_length} bytes from {url}")

async def download_all_sitesAsyncio(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_siteAsyncio(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

#----------------------Multiprocessing------------------------------------------------------------------
# Es necesario declarar esta variable global y la función de inicialización
# para que cada nuevo proceso del pool tenga su propia sesión de requests.
# 

session = None

def set_global_session_multiprocessing():
    global session
    if not session:
        session = requests.Session()

def download_site_multiprocessing(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}: Read {len(response.content)} bytes from {url}")

def download_all_sites_multiprocessing(sites):
    # 'initializer' se utiliza para que cada proceso en el pool
    # configure su propia sesión de requests, evitando problemas de concurrencia.
    with multiprocessing.Pool(initializer=set_global_session_multiprocessing) as pool:
        pool.map(download_site_multiprocessing, sites)

#--------------------------------------------------------------------------------------------------------

def run_all_methods():
    sites = image_urls
    
    start_time_sync = time.time()
    download_all_sitesSynchronous(sites)
    duration_sync = time.time() - start_time_sync
    
    start_time_threading = time.time()
    download_all_sitesThreading(sites)
    duration_threading = time.time() - start_time_threading
    
    start_time_async = time.time()
    asyncio.run(download_all_sitesAsyncio(sites))
    duration_async = time.time() - start_time_async
    
    start_time_mp = time.time()
    download_all_sites_multiprocessing(sites)
    duration_mp = time.time() - start_time_mp
    

    print("---------------------------------")
    print("    Resultados    ")
    print("---------------------------------")
    print(f"Descarga sincrónica:{len(sites)} in {duration_sync:.2f} segundos")
    print(f"Descarga con hilos:{len(sites)} in{duration_threading:.2f} segundos")
    print(f"Descarga con asyncio:{len(sites)} in{duration_async:.2f} segundos")
    print(f"Descarga con multiprocessing:{len(sites)} in {duration_mp:.2f} segundos")
    
    
if __name__ == "__main__":
    run_all_methods()