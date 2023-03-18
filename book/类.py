class 邱一阳:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def 名字(self):
        return self.name

    def 年龄(self):
        return self.age

    def 体重(self):
        return self.height

    def 设置名字(self, name):
        self.name = name

    def 设置年龄(self, age):
        self.age = age

    def 设置体重(self, height):
        self.height = height


if __name__ == '__main__':
    example_name = input('你想造一个叫什么名字的实例(人):')
    example_age = str(input('你想造一个年龄是多少的实例(人):'))
    example_height = str(input('你想造一个体重是多少的实例(人):'))
    a = 邱一阳(example_name, example_age, example_height)
