# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间

import time
import functools


def metric(fn):
    @functools.wraps(fn)
    def wrap(*args, **kv):
        start = time.time()
        result = fn(*args, **kv)
        end = time.time()
        executedTime = (end - start) * 1000
        print('%s executed in %f ms' % (fn.__name__, executedTime))
        print('%s executed is %s' % (fn.__name__, result))
        return result
    return wrap

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
# 再思考一下能否写出一个@log的decorator，使它既支持：


def log(*args):
    if isinstance(*args, str):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*p, **kv):
                print(*args)
                print('begin call')
                result = fn(*p, **kv)
                print('end call')
                return result
            return wrapper
        return decorator
    else:
        fn = args[0]
        @functools.wraps(fn)
        def wrapper(*p, **kv):
            print('begin call')
            result = fn(*p, **kv)
            print('end call')
            return result
        return wrapper
