#!/bin/python3
from argparse import ArgumentParser, Namespace

import requests

# CLI Code
def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('day', metavar='DAY', type=int, help='The day to prepare an environment for')

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Get Request cookies
    cookies = None
    with open('session.txt', 'r') as fp:
        tag, data, *_ = fp.read().split(':')
        cookies = {tag.strip(): data.strip()}

    # Get input data
    url = f'https://adventofcode.com/2020/day/{args.day}/input'
    with requests.get(url, cookies=cookies) as r:
        with open(f'data/input{args.day:02}.txt', 'w') as fp:
            fp.write(r.text)

    # Copy template into new file
    with open('template.py', 'r') as template:
        # Read from template
        s = template.read()

        s = s.replace('FILE_NAME = None', f'FILE_NAME = "data/input{args.day:02}.txt"')

        with open(f'day{args.day:02}.py', 'w') as fp:
            fp.write(s)


if __name__ == '__main__':
    main()

