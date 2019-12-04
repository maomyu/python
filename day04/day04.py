'''
@Author: your name
@Date: 2019-11-27 18:59:07
@LastEditTime: 2019-12-01 12:24:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \GoWebf:\python\day04\day04.py
'''
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

my_abs(-10)

# 空函数 pass语句用于占位符
def nop():
    pass

# 使用内置数据类型检查函数
def my_abs_two(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 返回多个值
import math


def move(x,y,step,angle=0):
    nx = x +step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx,ny
m = move(100,100,60,math.pi/6)
x ,y = move(100,100,60,math.pi/6)
print(m)
print(x)
print(y)

def quadratic(a, b, c):
    m = b*b-4*a*c
    if m >=0:
        xx = (math.sqrt(m)-b)/(2*a)
        yy = (-b-math.sqrt(m))/(2*a)
        return xx,yy
    else:
        return 'no answer'

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))