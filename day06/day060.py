# map()和reduce()
def f(x):
    return x * x

# ，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
r = map(f,[1,2,3,4,5,6,7,8,9])
print(r)
print(list(r))

# 把这个list所有数字转为字符串：
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
from functools import reduce
def add(x,y):
    return x + y

l = reduce(add,[1,3,5,7,9])
print(l)

def fn(x, y):
    return x * 10 + y
print(reduce(fn,[1,3,4,5,6]))

# 字符串转换成数字
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn,map(char2num,'13579')) )
