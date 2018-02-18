

def read_puzzle_input(filename):
    with open(filename, 'r') as file:
        data = file.read().strip()
    
    return(data)


def main():

    data = read_puzzle_input('input.txt')
    expected_sum = 0
    for i in range(len(data)):
        if data[i] == data[int(i + len(data) / 2) % len(data)]:
            expected_sum += int(data[i])
    print (expected_sum)


if __name__ == '__main__':
    main()
