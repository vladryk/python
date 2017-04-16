# >>> a='abcd'
# >>> a[::-1]
# 'dcba'

# >>> a=2
# >>> b=5
# >>> a,b = b,a
# >>> a
# 5
# >>> b
# 2


# >>> x = 'foo'  Immutable  types
# >>> y = x
# >>> y += 'bar'
# >>> y
# 'foobar'
# >>> x
# 'foo'

# >>> x = 'foo'
# >>> y = x
# >>> x += 'bar'
# >>> y
# 'foo'
# >>> x
# 'foobar'

# >>> x = [1, 2, 3]   mutable  types
# >>> y = x
# >>> x[0]=5
# >>> x
# [5, 2, 3]
# >>> y
# [5, 2, 3]
# >>>
# >>> y[0]=7
# >>> x
# [7, 2, 3]
# >>> y
# [7, 2, 3]


# Словарь: ключ-значение в одну строку в значение-ключ
# In [82]: r={'s':2,'d':3,'f':4}
# In [83]: {k:v for v,k in r.iteritems()}
# Out[83]: {2: 's', 3: 'd', 4: 'f'}


# Срезы
# In [84]: a=[2,3,4,5]

# In [85]: a[:]
# Out[85]: [2, 3, 4, 5]

# In [86]: a[::]
# Out[86]: [2, 3, 4, 5]

# In [87]: a[::-1]
# Out[87]: [5, 4, 3, 2]



# Список и Генератор списка
# In [20]: a=(1,2,3)
# In [22]: c=[i for i in a]
# In [23]: c
# Out[23]: [1, 2, 3]
#
# In [24]: c=(i for i in a)
# In [25]: c
# Out[25]: <generator object <genexpr> at 0x7f952d1ca870>




# >>> a = [[]] * 3
# >>> id(a[1])
# 139760549199952
# >>> id(a[2])
# 139760549199952
# >>>
# >>>
# >>> c=[[], [], []]
# >>> id(c[1])
# 139760549137728
# >>> id(c[2])
# 139760549200096
# >>>


# class Vehicle(object):      # different behavior for Vehicle(object)  and  Vehicle()
#     def __init__(self):
#         print('Vehicle')
#
#
# class Truck(Vehicle):
#     def __init__(self):
#         print('Truck')
#
# isinstance(Vehicle(), Vehicle)  # returns True
# type(Vehicle()) == Vehicle      # returns True
# isinstance(Truck(), Vehicle)    # returns True
# type(Truck()) == Vehicle        # returns False, and this probably won't be what you want.
# In other words, isinstance is true for subclasses, too.





# class A(object):            # different behavior for Vehicle(object)  and  Vehicle()
#     def printchar(self):
#         print 'A'
#
# class B(A):
#     pass
#
# class C(A):
#     def printchar(self):
#         print 'C'
#
# class D(B, C):
#     pass
#
# D().printchar()
