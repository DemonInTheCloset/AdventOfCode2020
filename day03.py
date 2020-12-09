#!/bin/python3
import itertools

# Environment variables
FILE_NAME = "input03.txt"
SANITY_SAMPLES = 5

# Space for auxiliary functions

# Space for problem solutions
def problem_one(lines):
    return 0


def problem_two(lines):
    return 0


# CLI Code (No need to edit)
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

