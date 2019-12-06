# 列表生成式
# 生成1，10的列表
l = list(range(1,11))
print(l)
# 生成[1x1, 2x2, 3x3, ..., 10x10]
l = [x * x for x in range(1,11)]
print(l)
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
l = [x * x for x in range(1,11) if x % 2 ==0]
print(l)

# 还可以使用两层循环，可以生成全排列：
l = [m + n for m in 'ABC' for n in 'xyz']
print(l)

l = [m+n+z for m in 'abc' for n in 'abc' if m !=n for z in 'abc' if m !=z and n !=z]
print(l)

# 使用for循环迭代字典可以实现多个变量接收
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
    print(k,'=',v)

# 因此使用列表生成式也可以
l = [k+'='+v for k,v in d.items()]
print(l)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)