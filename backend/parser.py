import requests
import sys


def parse(url):
    r = requests.get(url)
    return None if r.status_code == 404 else r.json()


if __name__ == "__main__":
    print(parse(sys.argv[1]))



