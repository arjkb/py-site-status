import concurrent.futures
import requests

from termcolor import colored

def is_site_working(url):
    try:
        r = requests.head(url, timeout=2)
        r.raise_for_status()
        return True if r.status_code == 200 else False
    except requests.exceptions.RequestException as e:
        pass

    return False

def get_site_status(url):
    (color, status) = ('green', 'ONLINE') if is_site_working(url) else ('red', 'OFFLINE')
    report_string = "{}\t{}".format(status, url)
    print(colored(report_string, color))

def main():
    urls = None
    with open('sitelist.txt') as f:
        urls = [url.strip() for url in f.read().strip().split("\n")]

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(get_site_status, urls)

if __name__ == "__main__":
    main()