#!/bin/python3
from __future__ import annotations

import itertools

from collections.abc import Iterator
from typing import Any

# Environment variables
FILE_NAME = "input16.txt"
SANITY_SAMPLES = 5

Rule = list[int]
Ticket = list[int]


# Space for auxiliary functions
def parse_header(lines) -> tuple[dict[str, list[Rule]], Ticket, list[Ticket]]:
    data = lines
    rules = dict()
    for line in data:
        if line:
            name, ranges, *_ = line.split(':')
            ranges = [
                    [int(y) for y in x.split('-')] for x in ranges.split('or')
                ]
            rules[name] = ranges
        else:
            break

    # discard your ticket line
    next(data)

    ticket = [int(x) for x in next(data).split(',')]

    # discard two lines
    next(data)
    next(data)

    other_tickets = [[int(x) for x in t.split(',')] for t in data]

    return rules, ticket, other_tickets


def in_range(rule: list[list[int]], number: int):
    for r in rule:
        if r[0] <= number <= r[1]:
            return True
    return False


def valid_ticket(ticket, rules: dict):
    for n in ticket:
        for rule in rules.values():
            if in_range(rule, n):
                break
        else:
            return False
    return True


def invalid_values(ticket, rules: dict):
    for n in ticket:
        for rule in rules.values():
            if in_range(rule, n):
                break
        else:
            yield n


# Space for problem solutions
def problem_one(lines: Iterator[str]) -> int:
    rules, _, tickets = parse_header(lines)

    return sum(map(sum, map(lambda x: invalid_values(x, rules), tickets)))


def problem_two(lines: Iterator[str]) -> int:
    rules, my_ticket, tickets = parse_header(lines)

    tickets = list(filter(lambda x: valid_ticket(x, rules), tickets))
    # six_rules = [r for (n, r) in rules.items() if n.startswith('departure')]
    positions = []
    for rule in rules.values():
        pos_set = {i for (i, x) in enumerate(tickets[0]) if in_range(rule, x)}
        positions.append(pos_set)
        for ticket in tickets[1:]:
            def ticket_entry(i: int):
                return in_range(rule, ticket[i])

            positions[-1] = set(filter(ticket_entry, positions[-1]))
            if len(positions[-1]) <= 1:
                positions[-1] = positions[-1].pop()
                break

    # print('\n'.join(map(str, positions)))
    while any(map(lambda x: isinstance(x, set), positions)):
        for x in positions:
            if isinstance(x, int):
                for i, s in enumerate(positions):
                    if isinstance(s, set):
                        s.discard(x)
                        if len(s) == 1:
                            positions[i] = s.pop()
    result = 1

    six_positions = [i for (k, i) in zip(rules.keys(), positions) if k.startswith('departure')]

    for i in six_positions:
        result *= my_ticket[i]

    return result


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

