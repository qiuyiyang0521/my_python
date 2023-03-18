import easygui as e

answer = e.enterbox("你喜欢哪种口味的冰激凌？", default="香草味")
e.msgbox("你喜欢的是" + answer)
