import turtle as t
import time

# 初始化
try:
    t.bgpic(r"F:\GitHub\my_python\素材\小挂钟表盘.gif")
except:
    t.bgcolor("black")
t.pencolor("red")
t.mode("logo")
t.clear()
t.speed(0)
t.ht()
t.down()


def 分针(分数):
    t.up()
    # 回到中心
    t.home()
    t.down()
    # 设置方向
    t.seth(分数)
    # 设置颜色
    t.pencolor("green")
    # 设置粗细
    t.width(8)
    # 长120像素
    t.fd(120)


def 秒针(秒数):
    t.up()
    # 回到中心
    t.home()
    t.down()
    # 设置方向
    t.seth(秒数)
    # 设置颜色
    t.pencolor("blue")
    # 设置粗细
    t.width(5)
    # 长120像素
    t.fd(120)


def main():
    miaoshu = 62
    while True:
        秒数 = 360 / 60 * time.localtime().tm_sec
        分数 = 360 / 60 * time.localtime().tm_min
        if time.localtime().tm_hour > 12:
            时数 = 360 / 60 * (time.localtime().tm_hour - 12)
        if miaoshu != 秒数:
            t.clear()
            秒针(秒数)
            分针(分数)
        miaoshu = 秒数


if __name__ == "__main__":
    main()


t.done()
