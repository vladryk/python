import random

class RandIter(object):

    def __init__(self):
        self.last = 1
        self.rand = random.random()

    def __iter__(self):
        # return self
        if self.rand < 0.1:
            raise StopIteration
        else:
            while abs(self.last-self.rand) < 0.4:
                print '*',
                self.rand = random.random()
            self.last = self.rand
            yield self.rand

    def next(self):
        if self.rand < 0.1:
            raise StopIteration
        else:
            while abs(self.last-self.rand) < 0.4:
                print '*',
                self.rand = random.random()
            self.last = self.rand
            return self.rand



class Yrange(object):
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

y = Yrange(3)
# y.next()
# 0
# y.next()
# 1


def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

y1 = yrange(3)
# y
# <generator object yrange at 0x401f30>
# y.next()
# 0




