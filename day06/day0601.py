# 过滤序列 根据true还是false进行返回
def is_odd(n):
    return n %2 == 1
print(list(filter(is_odd,[1,2,3,4,5,6])))

def deletebank(n):
    return n != ' '
print(list(filter(deletebank,'asd dfgds ')))

# 求素数

# 构建一个生成器
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

# 删选函数
def _not_divisable(n):
    return lambda x: x % n >0



# 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisable(n),it)



def pr():
    for n in primes():
        if n < 100:
            print(n)
        else:
            break
# pr()



def choose(n):
    return lambda x: x % n == 0

# 定义一个生成器
def zhengshu():
    n =  0
    while True:
        if n < 20:
            n =  n + 1
            yield n
        else:
            break

g = zhengshu()
# for n in range filter(choose(n),g)
print(list(filter(choose(5),g)))