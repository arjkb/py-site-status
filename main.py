import concurrent.futures
import requests

def is_site_working(url):
    try:
        r = requests.head(url, timeout=2)
        r.raise_for_status()
        return True if r.status_code == 200 else False
    except requests.exceptions.RequestException as e:
        pass

    return False

def main():
    urls = None
    with open('sitelist.txt') as f:
        urls = [url.strip() for url in f.read().split("\n")]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(is_site_working, urls)

if __name__ == "__main__":
    main()