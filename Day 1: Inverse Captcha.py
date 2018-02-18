

def read_puzzle_input(filename):
    with open(filename, 'r') as textfile:
        list_of_numbers = list((textfile.read()))
        list_of_numbers.pop()
        list_of_numbers = [int(number) for number in list_of_numbers]

    return(list_of_numbers)


def main():

    list_of_numbers = read_puzzle_input('input.txt')
    
    first_number = list_of_numbers[0]
    last_number = list_of_numbers[len(list_of_numbers) - 1]
    sum_of_numbers = 0
    k = 0
    temp = 0
    number = 0
    

    while number < len(list_of_numbers) - 1:

        if list_of_numbers[number] == list_of_numbers[number + 1]:

            if k >= 3:
                temp = list_of_numbers[number] * k
                k += 1
                print(" k rowne wieksze 3")

            if k == 1:
                temp = list_of_numbers[number] * k + list_of_numbers[number]
                k += 2
                print("k rowne 1")

            if k == 0:
                k += 1
                temp = list_of_numbers[number]
                print('k rowne 0')

        if list_of_numbers[number] != list_of_numbers[number + 1]:

            sum_of_numbers += temp
            print("test sum")
            print(sum_of_numbers)
            k = 0
            temp = 0

        number += 1

    if first_number == last_number:
        sum_of_numbers += first_number

    print("moja suma")
    print(sum_of_numbers)


if __name__ == '__main__':
    main()
