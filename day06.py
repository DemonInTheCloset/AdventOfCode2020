# Auxiliary functions
def get_lines():
   with open('input06.txt') as fp:
        for line in fp:
            yield line.strip()


def get_groups():
    group = []

    for line in get_lines():
        if line:
            group.append({ c for c in line })
        else:
            yield group
            group = []

    yield group


def reduce(operator, values):
    value = next(values)

    for v in values:
        value = operator(value, v)
    
    return value

def first_problem():
    count = 0
    answers = set()

    for line in get_lines():
        if line:
            answers |= set([c for c in line])
        else:
            count += len(answers)
            answers = set()

    count += len(answers)
    return count

def second_problem():
    return sum(map(len, [reduce(lambda x, y: x & y, (g for g in group)) for group in get_groups()]))


# Main Function
def main():
    print(f"First problem: {first_problem()}")
    print(f"Second problem {second_problem()}")


if __name__ == '__main__':
    main()
