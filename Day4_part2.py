

def read_puzzle_input(filename):
    with open(filename, 'r') as file:
        data = file.read().strip().split('\n')

    return(data)


def main():

    data = read_puzzle_input('input_day4.txt')

    result = 0
    for line in data:
        line_as_list = [''.join(sorted(x)) for x in line.split(' ')]
        if len(line_as_list) == len(set(line_as_list)):
            result += 1

    print(result)


if __name__ == '__main__':
    main()
