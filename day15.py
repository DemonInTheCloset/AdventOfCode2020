#!/bin/python3
from __future__ import annotations

import itertools

from collections.abc import Iterator
from typing import Any
from tqdm import trange

# Environment variables
FILE_NAME = "input15.txt"
SANITY_SAMPLES = 5

# Space for auxiliary functions


# Space for problem solutions
def problem_one(lines: Iterator[str]) -> int:
    last_turn_spoken = dict()
    numbers = [0, 1, 4, 13, 15, 12, 16]
    i = 0

    for n in numbers:
        last_turn_spoken[n] = i
        i += 1

    i += 1
    last = 0
    while i < 2020:
        tmp = last

        if last in last_turn_spoken:
            last = i - last_turn_spoken[last] - 1
        else:
            last = 0

        last_turn_spoken[tmp] = i - 1
        i += 1


    return last


def problem_two(lines: Iterator[str]) -> int:
    last_turn_spoken = dict()
    numbers = [0, 1, 4, 13, 15, 12, 16]
    # numbers = [3,2,1]

    for i,n in enumerate(numbers):
        last_turn_spoken[n] = i

    index = len(numbers)
    last = 0

    for i in trange(index + 1, 30000000):
        tmp = last

        if last in last_turn_spoken:
            last = i - last_turn_spoken[last] - 1
        else:
            last = 0
            
        last_turn_spoken[tmp] = i - 1

    return last


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
    executor(problem_one, itertools.islice(get_lines(), SANITY_SAMPLES))
    executor(problem_two, itertools.islice(get_lines(), SANITY_SAMPLES))



if __name__ == '__main__':
    main()

