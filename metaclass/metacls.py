
class MetaTest(type):

    def __new__(cls, name, bases, dict):
        klass = super(MetaTest, cls).__new__(cls, name, bases, dict)
        print "__new__(%r, %r, %r) -> %r" % (name, bases, dict, klass)
        return klass

    def __init__(cls, name, bases, dict):
        super(MetaTest, cls).__init__(name, bases, dict)
        print "__init__(%r, %r, %r)" % (name, bases, dict)

    def __call__(cls, *args, **kwargs):
        obj = super(MetaTest, cls).__call__(*args, **kwargs)
        print "__call__(%r, %r) -> %r" % (args, kwargs, obj)
        return obj


class Test(object):
    __metaclass__ = MetaTest  # MetaTest.__new__()  MetaTest.__init__()

test = Test()  # MetaTest.__call__()
