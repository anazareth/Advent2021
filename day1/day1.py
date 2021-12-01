import urllib.request

DATA_URL = r'https://adventofcode.com/2021/day/1/input'


def main():
    with urllib.request.urlopen(DATA_URL) as response:
        html = response.read()
    print(type(html))


if __name__ == '__main__':
    main()
