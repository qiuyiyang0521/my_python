# pickle永久储存对象
import pickle
import time
# 创建列表
list1 = ["qiuyiyang", "is a big 帅哥", "and 天才"]
# 新建文件,文件后缀随意
f = open("list1.qiuyiyang", "wb")
# 写入
pickle.dump(list1, f)
f.close()
# 读取
f = open("list1.qiuyiyang", "rb")
list2 = pickle.load(f)
print("list1=", list1)
print("list2=", list2)
f.close()

# 储存函数对象


def times(func):
    def call_time(*args, **kwargs):
        print("开始调用函数")
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("函数调用完毕...")
        print("调用函数一共用了", end_time-start_time, "秒")
    return call_time


help(times)
pickle_file = open("times.pkl", "wb")
pickle.dump(times, pickle_file)
pickle_file.close()


@times
def a(a):
    print(a)


a("qiuyiyang")

pickle_file = open("times.pkl", "rb")
times2 = pickle.load(pickle_file)
help(times2)
pickle_file.close()


@times2
def a2(a):
    print(a)


a2("qiuyiyang")
