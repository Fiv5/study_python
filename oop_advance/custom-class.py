# 定制一个类 Chain ,可以链式调用返回相应 Restful API
# Chain().users('michael').repos  =>  /users/:user/repos  => /users/michael/repos


class Chain(object):
    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __call__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path
    __repr__ = __str__


print(Chain().users('michael').repos)
