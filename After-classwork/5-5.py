import random
day = int(input("今天是星期几(1--7)："))
time = int(input("现在是几点（1--24）："))
if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
	if time == 18 or time == 19 or time == 20 or time == 21 or time == 22:
		print("全场8折优惠")
if day == 6 or day == 7:
	if time == 16 or time == 17 or time == 18 or time == 19 or time == 20 or time == 21 or time == 22:
		print("全场7折优惠")