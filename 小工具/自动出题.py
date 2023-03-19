import random
correct = 0
mistake = 0
x = 1
print('输入"exit"退出')
while True:

    if random.randint(1, 2) == 1:
        a1 = random.randint(1, 10)
        a2 = random.randint(1, 10)
        operator = '+'
        answer = a1 + a2
    else:
        operator = '-'
        while True:
            a1 = random.randint(1, 10)
            a2 = random.randint(1, 10)
            if a1 > a2:
                break
        answer = a1 - a2

    print(f'{x}、 {a1} {operator} {a2} = ', end='')
    input_answer = input('')

    if input_answer == "exit":
        print(f"一共答了{x - 1}题,答对了{correct}题答错了{mistake}题，正确率是{correct / (x - 1) * 100}%")
        break
    else:
        input_answer = int(input_answer)

    if input_answer == answer:
        print('正确')
        correct += 1
        x += 1
    else:
        print('错误')
        mistake += 1
        x += 1
