import requests

def check_site(url):
    try:
        r = requests.head(url, timeout=5)
        status = 'ONLINE' if r.status_code == 200 else 'OFFLINE'
    except:
        status = 'OFFLINE'
    print("{} {}".format(status, url))

def main():
    with open('sitelist.txt') as f:
        for site in f:
            check_site(site.strip())

if __name__ == "__main__":
    main()