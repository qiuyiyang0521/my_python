import time as t


class MyTimer():
    '''
    :start:开始计时
    :stop:停止计时
    :实例对象:计时的时间，也可以用print打印出来
    '''

    def __init__(self) -> None:
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.borrow = [0, 12, 31, 24, 60, 60]
        self.prompt = '还没计时呢，认真点！'
        self.laster = []
        self.start_time = 0
        self.stop_time = 0

    def __str__(self) -> str:
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        property = "总共运行了"
        result = []
        for index in range(5):
            result.append(self.laster[index] + other.laster[index])
            if result[index] == 0:
                pass
            else:
                property += str(result[index] + self.unit[index])
        print(property)

    # 开始计时
    def start(self):
        print('开始计时')
        self.prompt = '请先调用stop方法停止计时，你一定没有看文档!'
        self.start_time = t.localtime()

    # 停止计时
    def stop(self):
        if self.start_time == 0:
            print('请先调用start方法开始计时，你一定没有看文档!')
        else:
            self.stop_time = t.localtime()
            print('计时结束')
            self._calc()

    # 内部方法
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            temp = self.stop_time[index] - self.start_time[index]

            # 低位不够减，需向高位借位
            if temp < 0:
                # 测试高位是否有得“借”，没得借的话向再高位借......
                i = 1
                while self.lasted[index-i] < 1:
                    self.lasted[index-i] += self.borrow[index-i] - 1
                    self.lasted[index-i-1] -= 1
                    i += 1

                self.lasted.append(self.borrow[index] + temp)
                self.lasted[index-1] -= 1
            else:
                self.lasted.append(temp)

        # 由于高位随时会被借位，所以打印要放在最后
        for index in range(6):
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]
        self.start_time = 0
        self.stop_time = 0
