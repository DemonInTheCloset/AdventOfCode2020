#!/bin/python3
from __future__ import annotations

import itertools

from collections.abc import Iterator
from typing import Any

# Environment variables
FILE_NAME = "input03.txt"
SANITY_SAMPLES = 5

# Space for auxiliary functions
def traverse(trees: str, start: int, slope: tuple[int, int]) -> bool:
    n = len(trees)
    return trees[(start + slope[0] + n) % n] == '#'


# Space for problem solutions
def problem_one(lines: Iterator[str]) -> int:
    total = 0
    slope = (3, 1)
    i = 0

    for trees in lines:
        total += traverse(trees, i, slope)
        i += slope[1]

    return total


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
    executor(problem_one, itertools.islice(get_lines(), SANITY_SAMPLES))
    executor(problem_two, itertools.islice(get_lines(), SANITY_SAMPLES))



if __name__ == '__main__':
    main()

