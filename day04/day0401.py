'''
@Author: your name
@Date: 2019-12-01 12:25:16
@LastEditTime: 2019-12-04 13:37:42
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \GoWebf:\python\day04\day0401.py
'''
def power(x):
    return x * x

# n可以省略，并不会报错
def power_1(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

power_1(3)

# 坑 L是一个指向对象[]的变量，每次调用该函数时L不会改变
def add_end(L = []):
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end([1,2,3]))
print(add_end())

def add_sum(L = 1):
    L +=1
    return L
print(add_sum())
print(add_sum())
# 

def add_end_update(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end_update())
print(add_end_update())

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 传入后其实接收到的是一个元组
calc(1,2,3,4)

def calc_one(*nums):
    print(type(nums))
    sum = 0
    for n in nums:
        sum = sum + n 
    return sum    
# 传入一个元组或list 需要在前面加一个*
print(calc_one(*[1,2,3,4]))
print(calc_one(*[1,2,3,4],*[1,2,3,4]))

def calc_two(*nums):
    print(type(nums))
    print(nums)
calc_two(*[1,2,3,4])
calc_two(*[1,2,3,4],*[1,2,3,4])

# 关键字参数,将传入的参数自动组装成字典
def person(name,age,**kv):
     print('name:', name, 'age:', age, 'other:', kv)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
# 更为简单的调用
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# 限制关键字参数的名字,使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。

def person_one(name, age, *, city, job):
    print(name, age, city, job)
person_one('Jack', 24, city='Beijing', job='Engineer')

# 如果缺少*如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person_two(name, age, *args, city, job):
    print(name, age, city, job)
person_two('Jack', 24, city='Beijing', job='Engineer')

# 参数组合 需按照必选参数、默认参数、可变参数、关键字参数和命名关键字参数顺序

def produce(x,y = 2,*args):
    sum = x*y
    for n in args:
        sum = sum * n
    return sum 
print(produce(1))
print(produce(1,3))
print(produce(1,2,3,4))
print(produce(1,2,*[3,4]))