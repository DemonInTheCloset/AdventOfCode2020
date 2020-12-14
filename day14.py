#!/bin/python3
from __future__ import annotations

import itertools

from collections.abc import Iterator
from typing import Any

# Environment variables
FILE_NAME = "input14.txt"
SANITY_SAMPLES = 5

# Space for auxiliary functions
def parse_mask(mask:str) -> tuple:
    _, m, *_ = mask.split('=')
    m: str = m.strip()
    and_mask = int(m.replace('X', '1'), 2)
    or_mask = int(m.replace('X', '0'), 2)

    return and_mask, or_mask


def parse_mask_v2(mask: str) -> Iterator[tuple[int, int]]:
    _, m, *_ = mask.split('=')
    m: str = m.strip()
    
    xs = int(2 ** m.count('X'))
    n = len(bin(xs -1)[2:])
    for i in range(xs):
        b = bin(i)[2:]
        y = len(b)
        m_o_copy = m[:]
        m_a_copy = m[:]
        m_a_copy = m_a_copy.replace('0', '1')

        if (n - y) > 0:
            m_o_copy = m_o_copy.replace('X', '0', n - y)
            m_a_copy = m_a_copy.replace('X', '0', n - y)

        for c in b:
            m_o_copy = m_o_copy.replace('X', c, 1)
            m_a_copy = m_a_copy.replace('X', c, 1)

        yield int(m_o_copy, 2), int(m_a_copy, 2)


def parse_mem(mem: str) -> tuple:
    addr, val, *_ = mem.split('=')
    
    val = val.strip()
    val = int(val)

    *_, addr = addr.split('[')
    addr, *_ = addr.split(']')
    addr = int(addr)

    return addr, val


# Space for problem solutions
def problem_one(lines: Iterator[str]) -> int:
    m_and, m_or = parse_mask(next(lines))

    memory = dict()
    for line in lines:
        instr, *_ = line.split('=')
        if instr.startswith('mem'):
            addr, val = parse_mem(line)
            memory[addr] = m_or | (m_and & val)
        else:
            m_and, m_or = parse_mask(line)

    return sum(memory.values())


def problem_two(lines: Iterator[str]) -> int:
    masks = list(parse_mask_v2(next(lines)))

    memory = dict()
    for line in lines:
        instr, *_ = line.split('=')
        if instr.startswith('mem'):
            addr, val = parse_mem(line)

            for mask_or, mask_and in masks:
                memory[(addr | mask_or) & mask_and] = val
        else:
            masks = list(parse_mask_v2(line))

    return sum(memory.values())


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
    # print(list(parse_mask_v2('mask = 1XXX')))
    print('Results:')
    executor(problem_one, get_lines())
    executor(problem_two, get_lines())

    print(f'\nSanity checks (only the first {SANITY_SAMPLES} lines):')
    executor(problem_one, itertools.islice(get_lines(), SANITY_SAMPLES))
    executor(problem_two, itertools.islice(get_lines(), SANITY_SAMPLES))



if __name__ == '__main__':
    main()

