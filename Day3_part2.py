

def main():
   
    n = 20
    number = 289326 
    tab = [ [0]*n for _ in range(n) ]
    y = int(n/2)
    x = y+1

    tab[y][x-1] = 1       # initial value

    direction = 0
    max_steps = 1
    steps = 0
    direction_changes = 0
    direction_right = 0
    direction_up = 1
    direction_left = 2
    direction_down = 3

    while (x<=n and y<=n):
        tab[y][x] += (tab[y-1][x-1] if y>0 and x>0 else 0) + (tab[y-1][x] if y>0 else 0) + (tab[y-1][x+1] if y>0 and x<n else 0)
        tab[y][x] += (tab[y][x-1] if x>0 else 0) + (tab[y][x+1] if x<n else 0)
        tab[y][x] += (tab[y+1][x-1] if y<n and x>0 else 0) + (tab[y+1][x] if y<n else 0) + (tab[y+1][x+1] if y<n and x<n else 0)

        if tab[y][x] > number:
            print("Result: " + str(tab[y][x]))
            break

        steps = steps+1
        if steps==max_steps:
            direction_changes = direction_changes+1
            direction = (direction+1)%4
            steps = 0
            if direction_changes%2==0:
                max_steps = max_steps+1

        if direction==direction_right:
            x = x+1
        if direction==direction_up:
            y = y+1
        if direction==direction_left:
            x = x-1
        if direction==direction_down:
            y = y-1


if __name__ == '__main__':
    main()
