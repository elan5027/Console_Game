import random
import numpy
import os


forest = [
    ['!', '#', '*', '#', '#', '#', '#'],
    ['#', '!', '#', '#', '#', '#', '$'],
    ['#', '#', '!', '#', '#', '*', '#'],
    ['#', '#', '!', '#', '$', '#', '#'],
    ['#', '$', '!', '#', '#', '#', '#'],
    ['#', '#', '!', '#', '#', '#', '#']
]

forest2 = []


def mapset():

    for i in forest:
        random.shuffle(i)
    for val in range(0, len(forest)):
        line = []
        for va in range(0, len(forest[0])):
            line.append(' ')
        forest2.append(line)
    forest[5][3] = '@'
    forest2[5][3] = '@'


def showmap():
    print(*forest2, sep='\n')


def userCur():
    userxy = numpy.array(forest2)
    x, y = map(int, numpy.where(userxy == "@"))
    return x, y


def checkEvent(x, y):
    if forest[x][y] == '!':
        # print("적을 만낫다.")
        return "battle"
    elif forest[x][y] == '*':
        # print("탈출루트를 만낫다.")
        return "escape"
    elif forest[x][y] == '$':
        # print("아이템 획득 기회를 만낫다.")
        return "camp"


def move(usermove):
    doc = {'1': [-1, 0], '4': [1, 0], '2': [0, -1], '3': [0, 1]}
    x, y = userCur()
    if doc[usermove]:
        movexy = doc[usermove]
        if usermove == '1' and x == 0:
            print("이곳은 막다른 길이다")
            os.system("pause")
        elif usermove == '4' and x == 5:
            print("이곳은 막다른 길이다")
            os.system("pause")
        elif usermove == '2' and y == 0:
            print("이곳은 막다른 길이다")
            os.system("pause")
        elif usermove == '3' and y == 6:
            print("이곳은 막다른 길이다")
            os.system("pause")
        else:
            forest[x][y] = '#'
            forest2[x][y] = '#'
            x += movexy[0]
            y += movexy[1]
            event = checkEvent(x, y)
            forest[x][y] = '@'
            forest2[x][y] = '@'
            return event
