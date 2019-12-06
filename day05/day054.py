# 迭代器
# 之前使用isinstance（）判断一个对象是否时迭代对象
from collections import  Iterable
from collections import  Iterator
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
print(isinstance((x for x in range(10)), Iterable))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))

# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass
# d等价于
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break