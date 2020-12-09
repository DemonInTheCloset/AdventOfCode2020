#!/bin/python3
from __future__ import annotations

import itertools

from collections.abc import Iterator
from typing import Any

# Environment variables
FILE_NAME = "input09.txt"
SANITY_SAMPLES = 26

# Space for auxiliary functions
def valid(numbers: list[int]) -> bool:
    previous = numbers[:25]
    target = numbers[25]

    for x, y in itertools.combinations(previous, 2):
        if (x + y == target):
            return True

    return False


def contigous_set(numbers: list[int], target: int) -> list[int]:
    i = 0
    e = 0
    n = len(numbers)

    while ((s := sum(numbers[i:e])) != target and i < n):
        if s < target:
            e += 1
        else:
            i += 1
            e = i

    return numbers[i:e] if i < n else []


# Space for problem solutions
def problem_one(lines: Iterator[str]) -> int:
    numbers = list(map(int, lines))
    n = len(numbers)

    while (valid(numbers) and n > 25):
        n -= 1
        numbers.pop(0)

    return numbers[25]


def problem_two(lines: Iterator[str]) -> int:
    numbers = list(map(int, lines))

    s = contigous_set(numbers, 41682220)

    return min(s) + max(s)


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
    print(contigous_set([15,25,47,40],127))
    print('Results:')
    executor(problem_one, get_lines())
    executor(problem_two, get_lines())

    print(f'\nSanity checks (only the first {SANITY_SAMPLES} lines):')
    executor(problem_one, itertools.islice(get_lines(), SANITY_SAMPLES))
    executor(problem_two, itertools.islice(get_lines(), SANITY_SAMPLES))



if __name__ == '__main__':
    main()

