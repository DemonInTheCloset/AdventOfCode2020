#!/bin/python3
from __future__ import annotations

import itertools

from collections.abc import Iterator
from typing import Any
from tqdm import trange

# Environment variables
FILE_NAME = "input24.txt"
SANITY_SAMPLES = 5

Coordinate = tuple[int, int, int]
Instructions = list[Coordinate]
DIRECTIONS: dict[str, Coordinate] = {'se': (0, -1, +1), 'sw': (-1, 0, 1), 'ne': (1, 0, -1), 'nw': (0, 1, -1), 'e': (1, -1, 0), 'w': (-1, 1, 0)}


# Space for auxiliary functions
def parse_directions(line: str) -> Instructions:
    l = line[:]
    instr = []

    while l:
        if l[0] == 's' or l[0] == 'n':
            d = l[:2]
            l = l[2:]
            instr.append(DIRECTIONS[d])
        else:
            d = l[:1]
            l = l[1:]
            instr.append(DIRECTIONS[d])

    return instr


def flipped(instr: list[Instructions]) -> set[Coordinate]:
    black_tiles = set()
    
    for l in instr:
        t = 0, 0, 0
        
        for c in l:
            t = add_coord(t, c)
        
        if t in black_tiles:
            black_tiles.discard(t)
        else:
            black_tiles.add(t)

    return black_tiles


def add_coord(a: Coordinate, b: Coordinate) -> Coordinate:
    x, y, z = a
    p, q, r = b

    return x + p, y + q, z + r


def neighbours(tile: Coordinate) -> list[Coordinate]:
    return [add_coord(tile, d) for d in DIRECTIONS.values()]


def update_tiles(black_tiles: set[Coordinate]) -> set[Coordinate]:
    to_flip: set[Coordinate] = set()

    white_tiles: set[Coordinate] = set()
    for tile in black_tiles:
        adjacent = neighbours(tile)
        white = [n for n in adjacent if n not in black_tiles]
        white_tiles.update(white)

        if (n := len(white)) == 6 or n < 4:
            to_flip.add(tile)

    for tile in white_tiles:
        if len([n for n in neighbours(tile) if n in black_tiles]) == 2:
            to_flip.add(tile)

    return black_tiles ^ to_flip


# Space for problem solutions
def problem_one(lines: Iterator[str]) -> int:
    return len(flipped(list(map(parse_directions, lines))))


def problem_two(lines: Iterator[str]) -> int:
    black_tiles: set[Coordinate] = flipped(list(map(parse_directions, lines)))
    
    for _ in trange(100):
        black_tiles = update_tiles(black_tiles)

    return len(black_tiles)


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

