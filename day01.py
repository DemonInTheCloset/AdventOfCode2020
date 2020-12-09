# Auxiliarry functions
def get_entries():
    with open('input01.txt', 'r') as fp:
        for line in fp:
            if line.strip():
                yield int(line.strip())


def first_problem():
    entries = list(get_entries())

    for x in entries:
        for y in entries:
            if x + y == 2020:
                return x * y


def second_problem():
    entries = list(get_entries())

    for x in entries:
        for y in entries:
            for z in entries:
                if x + y + z == 2020:
                    return x * y * z


# Main function
def main():
    print(f"First problem: {first_problem()}")
    print(f"Second problem: {second_problem()}")


if __name__ == '__main__':
    main()
