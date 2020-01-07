# 匿名函数
# lambda函数就是一个匿名函数，冒号前面的x表示参数
# 但是匿名函数有一个限制就是只能是一个表达式，不用写return
l = list(map(lambda x:x*x, [1,2,3,4,5,6]))
print(l)

# 匿名函数也是一个对象，可以将匿名函数进行赋值
h = lambda x : x * x
print(h(8))

# 也可以把匿名函数当作返回值
def build(x,y):
    return lambda: x*x + y*y

print(build(2,3)())
