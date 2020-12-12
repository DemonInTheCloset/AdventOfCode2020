#!/bin/python3
from __future__ import annotations

import itertools

from collections.abc import Iterator
from typing import Any

# Environment variables
FILE_NAME = "input12.txt"
SANITY_SAMPLES = 5

# Space for auxiliary functions
def parse_instr(instrs: Iterator[str]) -> Iterator[tuple[str,int]]:
    yield from ((s[0], int(s[1:])) for s in instrs)


def turn(instr, facing):
    dirs = ['N', 'E', 'S', 'W']

    d, v = instr
    i = dirs.index(facing)
    v //= 90
    if d == 'L':
        v *= -1

    v = (4 + i + v) % 4
    return dirs[v]


def turn_two(instr, poss, posw):
    d,v = instr
    v //= 90

    if d == 'L':
        v *= -1

    for _ in range(abs(v)):
        if (v < 0):
            posw = -posw[1], posw[0]
        else:
            posw = posw[1], -posw[0]

    return posw


def move(instr, facing, pos: tuple[int, int]) -> tuple[int, int]:
    d, v = instr
    if 'F' == d:
        d = facing
    
    if 'N' == d or 'S' == d:
        if 'S' == d:
            v *= -1

        return pos[0] + v, pos[1]
    elif 'E' == d or 'W' == d:
        if 'W' == d:
            v *= -1
        return pos[0], pos[1] + v


def execute_instr(instrs) -> tuple[tuple[int, int], str]:
    facing = 'E'
    pos = (0, 0)

    for d, v in instrs:
        # print(f'{pos}, {facing}: {(d,v)}', end='')
        if d == 'L' or d == 'R':
            facing = turn((d, v), facing)
        else:
            pos = move((d, v), facing, pos)
        # print(f' -> {pos}, {facing}')

    return pos, facing


def execute_instr_two(instrs) -> tuple[tuple[int, int], str]:
    facing = 'E'
    posw = (10, 1)
    poss = (0, 0)

    for d, v in instrs:
        #print(f'{poss}, {posw}: {(d,v)}', end='')
        if d == 'R':
            for i in range(abs(v) // 90):
                posw = posw[1], -posw[0]
        elif d == 'L':
            for i in range(abs(v) // 90):
                posw = -posw[1], posw[0]
        elif d == 'F':
            poss = poss[0] + v * posw[0], poss[1] + v * posw[1]
        elif d == 'E':
            posw = posw[0] + v, posw[1]
        elif d == 'N':
            posw = posw[0], posw[1] + v
        elif d == 'W':
            posw = posw[0] - v, posw[1]
        elif d == 'S':
            posw = posw[0], posw[1] - v

        #print(f' -> {poss}, {posw}')


    return poss, facing


# Space for problem solutions
def problem_one(lines: Iterator[str]) -> int:
    pos, facing = execute_instr(parse_instr(lines))
    return abs(pos[0]) + abs(pos[1])


def problem_two(lines: Iterator[str]) -> int:
    pos, facing = execute_instr_two(parse_instr(lines))
    return abs(pos[0]) + abs(pos[1])


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
    executor(problem_two, itertools.islice(['F10', 'N3', 'F7', 'R90', 'F11'], SANITY_SAMPLES))



if __name__ == '__main__':
    main()

