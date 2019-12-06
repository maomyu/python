# 迭代
from collections import Iterable
d = {'a': 1, 'b': 2, 'c': 3}
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
for key in d:
    print(key)

# 迭代values
for key in d.values():
    print(key)

for c in 'ACV':
    print(c)

# 如何判断一个对象是可迭代对象呢
print(isinstance('abc', Iterable))  # str是否可迭代)
#  c:\users\dell\appdata\local\programs\python\python37\lib\site-packages (6.2.1)
# 对list实现下表循环
l = ['A','B','C']
for i,value in enumerate(l):
    print(i,value)

# 使用迭代查找list中的最小和最大
def findMinAndMax(L):
    min = L[0]
    max = L[0]
    for v in L:
        if min > v:
            min = v
        if max < v:
            max = v
    return (min,max)


print(findMinAndMax([1, 2, 4, 2]))
