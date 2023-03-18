# 用递归效率太低了，不用

num = int(input("请输入一个正整数："))
answer = 1
for x in range(2, num+1):
    answer *= x

print("答案是：" + str(answer))
