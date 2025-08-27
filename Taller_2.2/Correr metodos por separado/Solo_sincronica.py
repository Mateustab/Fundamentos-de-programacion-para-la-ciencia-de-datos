import requests
import time

image_urls = [
    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800",
    "https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=800",
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800",
    "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/jpeg"
] *25

def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


def main():
    sites = image_urls
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    
    print(f"Descarga sincrónica:{len(sites)} en {duration:.2f} segundos")


if __name__ == "__main__":
    main()