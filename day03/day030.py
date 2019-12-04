'''
@Author: your name
@Date: 2019-11-27 18:42:17
@LastEditTime: 2019-11-27 18:55:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \GoWebf:\python\day03\day030.py
'''
# 字典
names = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# 不存在的键会报错
# print(names['Bod'])
print(names['Bob'])
# 二次赋值
names['Bob'] = 888
print(names['Bob'])

# 避免不存在的键
print('Toms' in names)
# or
print(names.get('Thomas'))
# 指定value
print(names.get('Thomas',-1))

# 删除key
names.pop('Bob')
print(names)

# set 也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
print(set([1, 1, 2, 2, 3, 3]))

# 字符串不可变
str = 'abc'
p = str.replace('a','A')
print(p)
print(str)