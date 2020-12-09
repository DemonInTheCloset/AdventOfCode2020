#!/bin/python3
from __future__ import annotations

import itertools

# Environment variables
FILE_NAME = "input08.txt"
SANITY_SAMPLES = 5

# Space for auxiliary functions
def parse(instr: str) -> tuple[str, int]:
    name, value, *_ = instr.split(' ')
    return (name, int(value))


def vm(prog) -> tuple[int, bool]:
    l = len(prog)
    acc = 0
    p_counter = 0
    excecuted = set()

    while (p_counter not in excecuted and p_counter < l):
        name, value = prog[p_counter]
        excecuted.add(p_counter)

        if name == 'jmp':
            p_counter += value
        else:
            if name == 'acc':
                acc += value

            p_counter += 1

    return (acc, p_counter == l)


def change(index: int, prog: list[tuple[str, int]]) -> list[tuple[str, int]]:
    copy = prog[:]
    name, value = prog[index]
    copy[index] = ('jmp' if name == 'nop' else 'nop', value)
    return copy


def helper(prog: list[tuple[str, int]]) -> int:
    indices = [i for i, s in enumerate(prog) if s[0] != 'acc']
    l = len(indices)
    i = 0
    acc, status = vm(prog)

    while (not status and i < l):
        p = change(i, prog)
        acc, status = vm(p)

        i += 1

    return acc


# Space for problem solutions
def problem_one(lines) -> int:
    instructions = [parse(line) for line in lines]

    acc, _ = vm(instructions)
    return acc


def problem_two(lines) -> int:
    instructions = [parse(line) for line in lines]
    
    return helper(instructions)


# CLI Code (No need to edit):
def get_lines():
    with open(FILE_NAME, 'r') as fp:
        for line in fp:
            yield line.strip()


def executor(function, *args, **kwargs):
    try:
        print(f'{function.__name__} returned: {function(*args, **kwargs)}')
    except Exception as e:
        print(f'{function.__name__} failed with error: {e}')


def main():
    print('Results:')
    executor(problem_one, get_lines())
    executor(problem_two, get_lines())

    print(f'\nSanity checks (only the first {SANITY_SAMPLES} lines):')
    executor(problem_one, itertools.islice(get_lines(), SANITY_SAMPLES))
    executor(problem_two, itertools.islice(get_lines(), SANITY_SAMPLES))



if __name__ == '__main__':
    main()

