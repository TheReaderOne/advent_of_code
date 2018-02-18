

def read_puzzle_input(filename):
    with open(filename, 'r') as file:
        data = file.read().strip()

    return(data)


def main():
    data = read_puzzle_input('input2day.txt')
    result = 0
    for line in data.split('\n'):
        row_of_numbers = [int(x) for x in line.split('\t')]
        for number in row_of_numbers:
            for temp_number in row_of_numbers:
                if number != temp_number and number % temp_number == 0:
                    result += number / temp_number

    print(result)


if __name__ == '__main__':
    main()
