#打印乘法表
import os #防止用命令行运行窗口一闪而过
number = eval(input("你要打印几乘几的乘法表（x * x）"))
number **= 0.5
print("窗口全屏观看")
for x in range(1, int(number + 1)):
    for y in range(1, x + 1):
        print(f"%d * %d = %d" % (x , y, x *y), end = "\t")
    if x >= 10:
        for z in range(3):
            print()
    else:
        for z in range(2):
            print()

os.system("pause")
