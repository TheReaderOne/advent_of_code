

def main():
   
    number = 289326

    # constants
    DIR_RIGHT = 0
    DIR_UP = 1
    DIR_LEFT = 2
    DIR_DOWN = 3

    # location of the given number
    x = 0
    y = 0

    # initial direction
    DIR = 0

    # how many steps in actual direction
    MAX_STEPS = 1
    STEPS = 0
    DIR_CHANGES = 0


    for i in range(1,number):
        if DIR==DIR_RIGHT:
            x = x+1
        if DIR==DIR_UP:
            y = y+1
        if DIR==DIR_LEFT:
            x = x-1
        if DIR==DIR_DOWN:
            y = y-1
        
        STEPS = STEPS+1
        if STEPS==MAX_STEPS:
            DIR_CHANGES = DIR_CHANGES+1
            DIR = (DIR+1)%4
            STEPS = 0
            if DIR_CHANGES%2==0:
                MAX_STEPS = MAX_STEPS+1

    print("First part: " + str(abs(x)+abs(y)))



if __name__ == '__main__':
    main()
