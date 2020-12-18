#!/bin/python3
from __future__ import annotations

import itertools

from collections.abc import Iterator
from typing import Union

# Environment variables
FILE_NAME = "input18.txt"
SANITY_SAMPLES = 5


# Space for auxiliary functions
def parse(expr: str) -> list:
    special = {'+', '*', '(', ')'}
    expr_0 = []
    
    for c in expr:
        if c != ' ':
            if c in special:
                expr_0.append(c)
            else:
                expr_0.append(int(c))

    return parenthesis(expr_0)


def parenthesis(expr: list) -> Union[list, tuple[int, list]]:
    result = []
    n = len(expr)
    i = 0
    
    while i < n:
        c = expr[i]
        
        if c == '(':
            consumed, e = parenthesis(expr[i + 1:])
            result.append(e)
            i += consumed + 1
        elif c == ')':
            return i, result
        else:
            result.append(c)
        
        i += 1

    return result


def evaluate_v2(expr: list) -> int:
    # Evaluate parenthesis
    expr_0 = [evaluate_v2(e) if isinstance(e, list) else e for e in expr]

    # Evaluate adds
    expr_1 = []
    prev = expr_0[0]
    n = len(expr_0)
    i = 1
    
    while i < n:
        e = expr_0[i]
        
        if e == '+':
            prev += expr_0[i + 1]
            i += 2
        else:
            expr_1.append(prev)
            prev = e
            i += 1
    
    expr_1.append(prev)

    # Evaluate multiplies
    r = 1
    
    for e in expr_1:
        if isinstance(e, int):
            r *= e

    return r


def evaluate(string: str) -> tuple[int, int]:
    lhs = 0
    operation = '+'
    consumed = 0
    
    for i, c in enumerate(string):
        if consumed:
            consumed -= 1
        elif c != ' ':
            if c == '+' or c == '*':
                operation = c
            elif c == '(':
                rhs, consumed = evaluate(string[i + 1:])
                if operation == '+':
                    lhs += rhs
                else:
                    lhs *= rhs
                
            elif c == ')':
                return (lhs, i + 1)
            else:
                if operation == '+':
                    lhs += int(c)
                else:
                    lhs *= int(c)
    
    return (lhs, 0)


# Space for problem solutions
def problem_one(lines: Iterator[str]) -> int:
    return sum(map(lambda x: x[0], map(evaluate, lines)))


def problem_two(lines: Iterator[str]) -> int:
    return sum(map(evaluate_v2, map(parse, lines)))


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

