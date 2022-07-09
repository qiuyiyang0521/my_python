# -*- coding: utf-8 -*-
# @Author: qiuyiyang
# @Date: 2022-07-09 16:28:29
# @Email: 22133090041@qq.com
# @Last_modified_by: qiuyiyang
# @Last_modified_time: 2022-07-09 17:55:12

"""
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
玩家如果摇出其他点数则玩家继续摇骰子，
如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数玩家继续摇骰子，直到分出胜负。
"""

import time
import random

money = 0
du_zhu = 0
tong_xin_zheng = "False"

#获取本金（1-10000）
while money > 10000 or money <= 0:
	money = float(input("请输入你的本金："))

while money != 0: #只要不破产游戏就继续进行
	du_zhu = 0
	tong_xin_zheng = "False"
	time.sleep(1)
	print("你的本金是{}".format(money))

	#获取赌注
	while du_zhu > money or du_zhu <= 0:
		du_zhu = float(input("请输入你的赌注："))

	time.sleep(1)

	#第一轮
	first = int(random.randint(1,6))
	print("开始摇骰子。。。")
	time.sleep(0.5)
	print("3")
	time.sleep(1)
	print("2")
	time.sleep(1)
	print("1")
	time.sleep(1)
	print("投出的点数是。。。")
	time.sleep(1)
	print("{}点!".format(first))

	time.sleep(1)
	
	#判断是谁赢
	if first == 7 or first == 11:
		tong_xin_zheng = "False"
		money += du_zhu
		print("你胜了！")
	elif first == 2 or first == 3 or first == 12:
		tong_xin_zheng = "False"
		money -= du_zhu
		print("庄家胜！")
	else:
		tong_xin_zheng = "True"
		print("你和庄家都没胜，继续下一轮")

	time.sleep(1)

	#第二轮
	while True:
		if tong_xin_zheng == "False":
			break
		second = int(random.randint(1,6))
		print("开始摇骰子。。。")
		time.sleep(0.5)
		print("3")
		time.sleep(1)
		print("2")
		time.sleep(1)
		print("1")
		time.sleep(1)
		print("投出的点数是。。。")
		time.sleep(1)
		print("{}点!".format(second))

		time.sleep(1)

		#判断是谁赢
		if second == first:
			tong_xin_zheng = "False"
			money += du_zhu
			print("你胜了！")
			break
		elif second == 7:
			tong_xin_zheng = "False"
			money -= du_zhu
			print("庄家胜了！")
			break
		else:
			tong_xin_zheng = "True"
			print("你和庄家还是都没胜，继续下一轮")

print("你破产了")
time.sleep(1)
print("感谢你玩这个游戏！")
