def main():
    with open('sitelist.txt') as f:
        for site in f:
            print(site)

if __name__ == "__main__":
    main()