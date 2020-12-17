#!/bin/python3
from __future__ import annotations

import itertools

from collections.abc import Iterator
from typing import Any

# Environment variables
FILE_NAME = "input17.txt"
SANITY_SAMPLES = 5

vec3d = tuple[int, int, int]


# Space for auxiliary functions
def coodinates(lines: Iterator[str]) -> set[tuple[int, int, int]]:
    s = set()
    
    for j, row in enumerate(lines):
        for i, c in enumerate(row):
            if c == '#':
                s.add((i, j, 0))
    
    return s


def neighbours(cell: vec3d, i: int = 2) -> Iterator[vec3d]:
    cell = list(cell)
    if i >= 0:
        cell[i] -= 1
        yield from neighbours(cell[:], i -1)
        cell[i] += 1
        yield from neighbours(cell[:], i - 1)
        cell[i] += 1
        yield from neighbours(cell[:], i - 1)
    else:
        yield tuple(cell)


def neighbours4D(cell) -> Iterator:
    yield from neighbours(cell, 3)


def update(board: set, f: callable = neighbours) -> set:
    result = set()

    for cell in board:
        near = {x for x in f(cell)}
        near.discard(cell)
        n = 0
        for c in near:
            if c in board:
                n += 1
            else:
                if len(list(filter(lambda x: x in board, f(c)))) == 3:
                    result.add(c)

        if 2 <= n <= 3:
            result.add(cell)
    
    return result


# Space for problem solutions
def problem_one(lines: Iterator[str]) -> int:
    board = coodinates(lines)

    for i in range(6):
        board = update(board)

    return len(board)


def problem_two(lines: Iterator[str]) -> int:
    board = { c + (0,) for c in coodinates(lines) }

    for i in range(6):
        board = update(board, neighbours4D)

    return len(board)


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
    
    problem_one(get_lines())
    problem_two(get_lines())


if __name__ == '__main__':
    main()

