# 高阶函数
# 高阶函数英文叫Higher-order function
# 以Python内置的求绝对值的函数abs()为例，调用该函数用以下代码：
print(abs(-10))
print(abs)
# 可见，abs(-10)是函数调用，而abs是函数本身。

f = abs
print(f(-10))
print(f)

# 函数名也是变量

# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)

print(add(-1,-2,abs))