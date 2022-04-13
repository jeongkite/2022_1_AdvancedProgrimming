from random import randint
from time import sleep  # 자연스러운 게임 진행을 위해 사용


class Stack(list):
    push = list.append

    pop = list.pop

    def is_empty(self):
        return 0 if self else 1

    def peek(self):
        return self[-1] if self else -1


# [func] - 외친 숫자를 판단해 pop(비었을 시 메시지 출력) || push
def checkNumber(num, stack):
    if num % 3:
        stack.push(num)
    else:
        if not stack.is_empty():
            popNum = stack.pop()
            print(f'{popNum}가 지워졌어요~')
        else:
            print('스택이 비어있어요!')
            pass


# [func] - stack 유효 범위 내의 item 모두 출력
def printStackItem(i, length, stack):
    if length > i:
        print(f'{stack[i]} ', end='')
        return stack[i]
    return 0


if __name__ == '__main__':
    wonStack = Stack()
    myStack = Stack()
    nums = []

    # 숫자 외에 입력시 다시 입력 받음
    while True:
        times = input('동덕이와 원준이가 숫자를 몇 번 외칠까요? ')
        if not times.isnumeric():
            print('게임 횟수를 숫자로 입력하세요!')
            continue
        break
    times = int(times)

    for i in range(0, times):
        if i % 2:
            sleep(0.5)
            num = randint(1, 9)
            print(f'{i}.원준: {num}')
            checkNumber(num, wonStack)
            sleep(0.5)
        else:
            # 숫자인지, 범위 내인지 메세지 출력 및 다시 입력 받음
            while True:
                num = input(f'{i}.당신: ')
                if num.isnumeric():
                    num = int(num)
                    if num < 1 or num > 9:
                        print('"1~9 사이"의 숫자를 입력하세요!')
                        continue
                    checkNumber(num, myStack)
                else:
                    print('1~9 사이의 "숫자"를 입력하세요!')
                    continue
                break

    if wonStack.is_empty() and myStack.is_empty():
        print('모든 스택이 비어있어요!')
    else:
        sumNums = 0
        wonLen = len(wonStack)
        myLen = len(myStack)
        if wonLen > myLen:
            maxLen = wonLen
        else:
            maxLen = myLen
        for i in range(0, maxLen):
            sumNums += printStackItem(i, myLen, myStack)
            sumNums += printStackItem(i, wonLen, wonStack)
        print('=', sumNums)
