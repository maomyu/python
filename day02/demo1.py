# 列表
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print("列表的长度：",len(classmates))
print("通过索引访问元素",classmates[0],classmates[1])
print("如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引",classmates[-1])
# 追加元素
classmates.append('yuwei')
print(classmates)
# 删除末尾的元素使用pop
print(classmates.pop())
print(classmates)
# 删除指定元素
print(classmates.pop(0))
print(classmates)
# 替换元素
classmates[0] = '替换'
print(classmates)
# 列表的元素类型可以是不同的
classmates.append(10)
print(classmates)

# 元组
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
t = (1, 2)
print(t)
# 定义一个元素的元组
t = (1,)
print(t)

# 可变的元组
t = ('a','b',['A','B'])
t[2][0] = 'X'
print(t)