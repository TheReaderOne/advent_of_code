

def read_puzzle_input(filename):
    with open(filename, 'r') as file:
        data = file.read().strip()
    
    return(data)


def main():
    data = read_puzzle_input('input2day.txt')

    checksum = 0
    for line in data.split('\n'):
        ll = [int(x) for x in line.split('\t')]
        checksum += max(ll) - min(ll)
    print (checksum)

if __name__ == '__main__':
    main()
