# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

# 方法一, 用一个引用变量存值


def createCounter1():
    L = [0]

    def counter():
        L[0] += 1
        return L[0]
    return counter


# 方法二, 外部构造一个生成器通过迭代返回
def generateCounter():
    num = 1
    while 1:
        yield num
        num += 1


def createCounter2():
    g = generateCounter()

    def counter():
        return next(g)
    return counter


# 测试:
counterA = createCounter1()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter1()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
