# sort
print(sorted([36,5,-12,9,-21]))
# 接收一个key实现自定义的排序，返回结果按照绝对值的大小进行排序，输出不变
print(sorted([23,1,23,4,2,34,2,4,-3],key=abs))

# 如字符串排列忽略daxiaox
print(sorted(['bot',"about","Zoo","Credit"],key=str.lower))

print(sorted(['bot',"about","zoo","credit"],key=str.lower))