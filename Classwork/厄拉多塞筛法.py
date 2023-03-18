fan_wei = int(input("求1到~多少范围内的质数？\n"))
a = []
a = list(range(2, fan_wei + 1))
i = 0
while True:
    while i < len(a):
        j = i + 1
        while j < len(a):
            if a[j] % a[i] == 0:
                a.pop([j])
            else:
                j = j + 1
        else:
            i + 1
    else:
        break

print(a)
