from random import randint
from time import sleep  # 자연스러운 게임 진행을 위해 사용


class Stack(list):
    push = list.append

    pop = list.pop

    def is_empty(self):
        return 0 if self else 1

    def peek(self):
        return self[-1] if self else -1


# 얍
if __name__ == '__main__':
    wonStack = Stack()
    myStack = Stack()
    nums = []

    while True:
        times = input('동덕이와 원준이가 숫자를 몇 번 외칠까요? ')
        if times.isalpha():
            print('게임 횟수를 숫자로 입력하세요!')
            continue
        break
    times = int(times)

    # 이걸 이렇게 크게 나누는게 맞을까?
    # 함수로 따로 깔끔하게 뺄 수 있는 방법 없나?
    for i in range(0, times):
        if i % 2:
            sleep(0.5)
            num = randint(1, 9)
            print(f'{i}.원준: {num}')
            if num % 3 == 0:
                try:
                    popNum = myStack.pop()
                    print(f'{popNum}가 지워졌어요~')
                except IndexError:
                    print('스택이 비어있어요!')
                    pass
            else:
                wonStack.push(num)
                nums.append(num)
            sleep(0.5)

        else:
            while True:
                num = int(input(f'{i}.당신: '))
                if num < 1 or num > 9:
                    print('1~9 사이의 수를 입력하세요!')
                    continue
                break
            if num % 3 == 0:
                try:
                    popNum = wonStack.pop()
                    print(f'{popNum}가 지워졌어요~')
                except IndexError:
                    print('스택이 비어있어요!')
                    pass
            else:
                myStack.push(num)
                nums.append(num)

    if len(nums):
        isFirst = True
        sumNums = 0
        for n in nums:
            if isFirst:
                print(n, end='')
                isFirst = False
            else:
                print(f' + {n}', end='')
            sumNums += n

        print(' =', sumNums)
    else:
        print('모든 스택이 비어있어요!')
