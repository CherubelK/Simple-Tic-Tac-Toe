# tic tac toe

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def determine(z):
    for i in x:
        if i[0] == z and i[1] == z and i[2] == z:
            for q in x:
                print(q)
            if z == 'X':
                return 'YOU WIN!'
            return 'YOU LOSE!'
    if (x[0][0] == z and x[1][0] == z and x[2][0] == z) or \
            (x[0][1] == z and x[1][1] == z and x[2][1] == z) or \
            (x[0][2] == z and x[1][2] == z and x[2][2] == z) or \
            (x[0][0] == z and x[1][1] == z and x[2][2] == z) or \
            (x[0][2] == z and x[1][1] == z and x[2][0] == z):
        for q in x:
            print(q)
        if z == 'X':
            return 'YOU WIN!'
        return 'YOU LOSE!'
    for i in x:
        if type(i[0]) == int or type(i[1]) == int or type(i[2]) == int:
            break
    else:
        for i in x:
            print(i)
        return 'DRAW'
    if z == 'X':
        return comp_move()
    return your_move()


def your_move():
    for i in x:
        print(i)
    n = int(input('Please enter a number spot that you want to take: '))
    for index1, item1 in enumerate(x):
        for index2, item2 in enumerate(item1):
            if n == item2:
                x[index1][index2] = 'X'
                return determine('X')


def comp_move():
    if ((x[0][0] == 'O' and x[2][0] == 'O') or (x[1][1] == 'O' and x[1][2] == 'O')) and type(x[1][0]) == int:
        x[1][0] = 'O'
    elif ((x[1][0] == 'O' and x[2][0] == 'O') or (x[0][1] == 'O' and x[0][2] == 'O') or (
            x[1][1] == 'O' and x[2][2] == 'O')) and type(x[0][0]) == int:
        x[0][0] = 'O'
    elif ((x[2][1] == 'O' and x[2][2] == 'O') or (x[0][0] == 'O' and x[1][0] == 'O') or (
            x[0][2] == 'O' and x[1][1] == 'O')) and type(x[2][0]) == int:
        x[2][0] = 'O'
    elif ((x[0][1] == 'O' and x[1][1] == 'O') or (x[2][0] == 'O' and x[2][2] == 'O')) and type(x[2][1]) == int:
        x[2][1] = 'O'
    elif ((x[1][1] == 'O' and x[2][1] == 'O') or (x[0][0] == 'O' and x[0][2] == 'O')) and type(x[0][1]) == int:
        x[0][1] = 'O'
    elif ((x[0][2] == 'O' and x[1][2] == 'O') or (x[2][0] == 'O' and x[2][1] == 'O') or (
            x[0][0] == 'O' and x[1][1] == 'O')) and type(x[2][2]) == int:
        x[2][2] = 'O'
    elif ((x[0][2] == 'O' and x[2][2] == 'O') or (x[1][0] == 'O' and x[1][1] == 'O')) and type(x[1][2]) == int:
        x[1][2] = 'O'
    elif ((x[1][2] == 'O' and x[2][2] == 'O') or (x[0][0] == 'O' and x[0][1] == 'O') or (
            x[2][0] == 'O' and x[1][1] == 'O')) and type(x[0][2]) == int:
        x[0][2] = 'O'
    elif ((x[0][0] == 'O' and x[2][2] == 'O') or (x[2][0] == 'O' and x[0][2] == 'O') or (
            x[0][1] == 'O' and x[2][1] == 'O') or (x[1][0] == 'O' and x[1][2] == 'O')) and type(x[1][1]) == int:
        x[1][1] = 'O'
    elif ((x[0][0] == 'X' and x[2][0] == 'X') or (x[1][1] == 'X' and x[1][2] == 'X')) and type(x[1][0]) == int:
        x[1][0] = 'O'
    elif ((x[1][0] == 'X' and x[2][0] == 'X') or (x[0][1] == 'X' and x[0][2] == 'X') or (
            x[1][1] == 'X' and x[2][2] == 'X')) and type(x[0][0]) == int:
        x[0][0] = 'O'
    elif ((x[2][1] == 'X' and x[2][2] == 'X') or (x[0][0] == 'X' and x[1][0] == 'X') or (
            x[0][2] == 'X' and x[1][1] == 'X')) and type(x[2][0]) == int:
        x[2][0] = 'O'
    elif ((x[0][1] == 'X' and x[1][1] == 'X') or (x[2][0] == 'X' and x[2][2] == 'X')) and type(x[2][1]) == int:
        x[2][1] = 'O'
    elif ((x[1][1] == 'X' and x[2][1] == 'X') or (x[0][0] == 'X' and x[0][2] == 'X')) and type(x[0][1]) == int:
        x[0][1] = 'O'
    elif ((x[0][2] == 'X' and x[1][2] == 'X') or (x[2][0] == 'X' and x[2][1] == 'X') or (
            x[0][0] == 'X' and x[1][1] == 'X')) and type(x[2][2]) == int:
        x[2][2] = 'O'
    elif ((x[0][2] == 'X' and x[2][2] == 'X') or (x[1][0] == 'X' and x[1][1] == 'X')) and type(x[1][2]) == int:
        x[1][2] = 'O'
    elif ((x[1][2] == 'X' and x[2][2] == 'X') or (x[0][0] == 'X' and x[0][1] == 'X') or (
            x[2][0] == 'X' and x[1][1] == 'X')) and type(x[0][2]) == int:
        x[0][2] = 'O'
    elif ((x[0][0] == 'X' and x[2][2] == 'X') or (x[2][0] == 'X' and x[0][2] == 'X') or (
            x[0][1] == 'X' and x[2][1] == 'X') or (x[1][0] == 'X' and x[1][2] == 'X')) and type(x[1][1]) == int:
        x[1][1] = 'O'
    elif x[0][0] == 'X' and type(x[2][2]) == int:
        x[2][2] = 'O'
    elif x[0][2] == 'X' and type(x[2][0]) == int:
        x[2][0] = 'O'
    elif x[2][0] == 'X' and type(x[0][2]) == int:
        x[0][2] = 'O'
    elif x[0][0] == 1:
        x[0][0] = 'O'
    elif x[2][2] == 9:
        x[2][2] = 'O'
    elif x[2][0] == 7:
        x[2][0] = 'O'
    elif x[0][2] == 3:
        x[0][2] = 'O'
    elif x[1][1] == 5:
        x[1][1] = 'O'
    elif x[1][0] == 4:
        x[1][0] = 'O'
    elif x[2][1] == 8:
        x[2][1] = 'O'
    elif x[1][2] == 6:
        x[1][2] = 'O'
    elif x[0][1] == 2:
        x[0][1] = 'O'
    return determine('O')


def start(starter):
    if starter == 1:
        return your_move()
    return comp_move()


print(start(int(input("Please enter 1 if you want to go first or 2 if you want to go second: "))))
