#!/bin/python3
from __future__ import annotations

import itertools

from collections.abc import Iterator
from typing import Any
from math import log

# Environment variables
FILE_NAME = "data/input25.txt"
SANITY_SAMPLES = 5


# Space for auxiliary functions
def handshake(subject: int, loop_size: int) -> int:
    return pow(subject, loop_size, 20201227)


def get_loop_size(public_key: int) -> int:
    k = int(log(public_key, 7))
    
    while handshake(7, k) != public_key:
        k += 1

    return k


# Space for problem solutions
def problem_one(lines: Iterator[str]) -> int:
    keys = list(map(int, lines))
    card, door, *_ = keys

    loop_size = get_loop_size(card)

    return handshake(door, loop_size)


def problem_two(lines: Iterator[str]) -> int:
    return 0


# CLI Code (No need to edit)
def get_lines() -> Iterator[str]:
    with open(FILE_NAME, 'r') as fp:
        for line in fp:
            yield line.strip()


def executor(function: callable[[Any], int], *args, **kwargs) -> None:
    try:
        print(f'{function.__name__} returned: {function(*args, **kwargs)}')
    except Exception as e:
        print(f'{function.__name__} failed with error: {e}')


def main() -> None:
    print('Results:')
    executor(problem_one, get_lines())
    executor(problem_two, get_lines())

    print(f'\nSanity checks (only the first {SANITY_SAMPLES} lines):')
    executor(problem_one, ["5764801", "17807724"])
    executor(problem_two, itertools.islice(get_lines(), SANITY_SAMPLES))


if __name__ == '__main__':
    main()

