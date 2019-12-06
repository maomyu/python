# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
# 那后面绝大多数元素占用的空间都白白浪费了。

# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list

# 创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * x for x in range(10))
# 打印出g中的每一个元素，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
# 直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
print([n for n in g])

# 第二种生成方法
# 先看一个斐波那契数列
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'done'
fib(10)
# fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator
# 上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fibgenerator(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done',"done"

f = fibgenerator(10)
print([v for v in f])

# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    # print('step 1')
    yield 1
    # print('step 2')
    yield 3
    # print('step 3')
    yield 5
    # return 'done'
o = odd()

for v in o:
    print(v)
# generator的函数中一旦迭代依次后生成器中的值将不存在，再次打印会出现空值
print([v for v in o])

# 回到fibgenertor的例子，函数遇到yeild就会返回，最终函数结束时实在return
# 如果想要拿到return的数据，需要进行捕获StopIteration错误
g = fibgenerator(10)
while True:
    try:
        x = next(g)
        print('g = ',x)
    except StopIteration as e:
        print(e.value)
        break
# 杨辉三角练习
def triangles():
#     定义一个10 x 10 的矩阵
    matrix = [[0 for i in range(10)] for i in range(10)]
#     定义连个变量，代表下标
    i,j = 0,0
    for h in matrix:
        matrix[i][0] = 1
        matrix[i][j] = 1
        i +=1
        j +=1
    for index,item in enumerate(matrix):
        for col,v in enumerate(item):
            if col == index:
                break
            if index > 1 and col !=0:
                matrix[index][col] = matrix[index-1][col] + matrix[index-1][col-1]
    for v in matrix:
        yield [value for value in v if value !=0]
# 更为简单的思路，不考虑下表，直接考虑值的由来
def triange_one():
    L = [1]
    while True:
        print(L)
        L = [L[x]+L[x+1] for x in range(len(L)-1)]
        print('更该数据后', L)
        L.insert(0,1)
        L.append(1)
        if len(L)>10:
            break
triange_one()
g = triangles()
for v in g:
    print(v)