#!/bin/python3
from __future__ import annotations

import itertools

from collections.abc import Iterator
from collections import Counter
from typing import Any

# Environment variables
FILE_NAME = "input10.txt"
SANITY_SAMPLES = 5

# Space for auxiliary functions
def diffs(numbers):
    return [y - x for x, y in zip(numbers, numbers[1:])]


def arragenments(diff, can_takeout, i=0):
    for b in can_takeout[i:]:
        if b:
            yield from arragenments(diff, can_takeout, i + 1)

            c = diff[:]
            v = c.pop(i)
            t = can_takeout[:]
            t.pop(i)

            try:
                c[i] += v

                if c[i] < 3:
                    yield from arragenments(c, can_takeout, i)
            except Exception:
                pass
            finally:
                break
        i += 1
    else:
        yield diff



# Space for problem solutions
def problem_one(lines: Iterator[str]) -> int:
    numbers: list[int] = [int(x) for x in lines]
    numbers.sort()
    m = numbers[-1]
    numbers.append(m + 3)
    numbers.insert(0, 0)

    diff = diffs(numbers)
    c = Counter(diff)
    return c[1] * c[3]


def problem_two(lines: Iterator[str]) -> int:
    numbers: list[int] = [int(x) for x in lines]
    numbers.sort()
    m = numbers[-1]
    numbers.append(m + 3)
    numbers.insert(0, 0)

    diff = diffs(numbers)

    can_takeout = [x + y < 3 for x, y in zip(diff, diff[1:])]
    can_takeout.insert(0, False)
    possibilities = 0

    a = list(arragenments(diff, can_takeout))
    
    return len(a)


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

    problem_two(get_lines())

if __name__ == '__main__':
    main()

