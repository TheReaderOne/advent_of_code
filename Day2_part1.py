

def read_puzzle_input(filename):
    with open(filename, 'r') as file:
        data = file.read().strip()

    return(data)


def main():
    data = read_puzzle_input('input2day.txt')

    result = 0

    for line in data.split('\n'):

        list_of_numbers = [int(number) for number in line.split('\t')]
        result += max(list_of_numbers) - min(list_of_numbers)

        print(result)


if __name__ == '__main__':
    main()
