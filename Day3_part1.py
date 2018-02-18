

def main():

    number = 289326

    # constants
    direction_right = 0
    direction_up = 1
    direction_left = 2
    direction_down = 3

    # location of the given number
    x = 0
    y = 0

    # initial directionection
    direction = 0

    # how many steps in actual directionection
    max_steps = 1
    steps = 0
    direction_changes = 0

    for i in range(1, number):
        if direction == direction_right:
            x = x+1
        if direction == direction_up:
            y = y+1
        if direction == direction_left:
            x = x-1
        if direction == direction_down:
            y = y-1

        steps = steps+1
        if steps == max_steps:
            direction_changes = direction_changes+1
            direction = (direction + 1) % 4
            steps = 0
            if direction_changes % 2 == 0:
                max_steps = max_steps+1

    print("First part: " + str(abs(x)+abs(y)))


if __name__ == '__main__':
    main()
