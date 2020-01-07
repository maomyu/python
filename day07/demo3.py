# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，
# 通过变量也可以调用该函数
def now():
    print('2016-12-2')

f = now
f()

# 函数对象有一个__name__属性，可以拿到函数的名字
name = now.__name__
print(name)

# 增加now函数的特性，要求在函数执行前和执行后打印日志
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now_two():
    print("34353")

now_two()