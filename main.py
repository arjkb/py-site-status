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
    with open('sitelist.txt') as f:
        for site in f:
            print(is_site_working(site.strip()))

if __name__ == "__main__":
    main()