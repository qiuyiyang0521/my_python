import easygui as g
import sys

while True:
    g.msgbox("小游戏", "小游戏")
    going = True

    while going:
        msg = "邱一阳是什么？"
        title = "邱一阳是什么"
        choices = ["帅哥", "天才与帅哥兼备", "傻瓜"]

        choice = g.choicebox(msg, title, choices)

        msg = "你选择的是：", choice
        title = "结果"

        g.msgbox(msg, title)

        if choice == "天才与帅哥兼备":

            msg = "看来你的判断很准确！w(°ｏ°)w"
            title = "Perfect"

            g.msgbox(msg, title)
            going = False

        elif choice == "帅哥":

            msg = "你的选择和正确答案只差了一点点，再试一次吧！(o^▽^o)"
            title = "Good"

            g.msgbox(msg, title)
            going = True

        else:

            msg = "你的判断能力很差呀，这么显而易见的答案都选不对！(∘⁼̴⃙̀˘︷˘⁼̴⃙́∘)"
            title = "No"

            g.msgbox(msg, title)
            going = True

    msg = "你希望重新开始小游戏吗"
    title = "请选择"

    if g.ccbox(msg, title, ('继续[a]', '取消[b]')):
        pass
    else:
        sys.exit()
