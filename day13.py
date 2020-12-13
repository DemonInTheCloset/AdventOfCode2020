#!/bin/python3
from __future__ import annotations

import itertools

from collections.abc import Iterator
from typing import Any

from sympy.ntheory.modular import crt

# Environment variables
FILE_NAME = "input13.txt"
SANITY_SAMPLES = 5

# Space for auxiliary functions
def parse(lines):
    start = int(next(lines))
    busses = [int(i) for i in next(lines).split(',') if i != 'x']

    return start, busses


def valid(buses, t) -> bool:
    for i, b in enumerate(buses):
        if (t + i) % b:
            return False

    return True


# Space for problem solutions
def problem_one(lines: Iterator[str]) -> int:
    start, busses = parse(lines)

    best_bus = 0
    wait_time = 10 ** 10

    for i in busses:
        departure = start // i
        if start % i:
            departure += 1

        departure *= i

        wt = departure - start
        if wt < wait_time:
            best_bus = i
            wait_time = wt

    return best_bus * wait_time


def problem_two(lines: Iterator[str]) -> int:
    start = int(next(lines))
    buses = [int(x) if x != 'x' else 1 for x in next(lines).split(',')]

    b = list(filter(lambda x: x != 1, buses))
    r = list((buses[x] - x) % buses[x] for x in range(len(buses)) if buses[x] != 1)
    t, _ = crt(b, r)
    return t 


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

