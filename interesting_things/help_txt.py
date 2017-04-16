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

# Сортировка  []  ()
# https://docs.python.org/2.7/library/functions.html#sorted

# In [1]: lst = ['Stem', 'constitute', 'Sedge', 'Eflux', 'Whim', 'Intrigue']

# In [2]: sorted(lst)
# Out[2]: ['Eflux', 'Intrigue', 'Sedge', 'Stem', 'Whim', 'constitute']

# In [4]: sorted(lst, key=str.lower)
# Out[4]: ['constitute', 'Eflux', 'Intrigue', 'Sedge', 'Stem', 'Whim']

# In [12]: sorted(lst, reverse=True)
# Out[12]: ['constitute', 'Whim', 'Stem', 'Sedge', 'Intrigue', 'Eflux']

# In [13]: sorted(lst, key=str.lower, reverse=True)
# Out[13]: ['Whim', 'Stem', 'Sedge', 'Intrigue', 'Eflux', 'constitute']

# In [28]: lst = ['Stem', 'constitute', 'Sedge', 'Eflux', 'Whim', 'Intrigue']
# In [29]: lst.sort(key=lambda x: len(x))
# In [30]: lst
# Out[30]: ['Stem', 'Whim', 'Sedge', 'Eflux', 'Intrigue', 'constitute']

# In [31]: c={1: 'D', 2: 'B', 3: 'B', 5: 'E', 4: 'A'}
# In [32]: sorted(c)
# Out[32]: [1, 2, 3, 4, 5]
# In [33]: c
# Out[33]: {1: 'D', 2: 'B', 3: 'B', 4: 'A', 5: 'E'}

# In [34]:  c={1: 'D', 2: 'B', 3: 'B', 'some': 'E', 'another': 'A'}
# In [35]: sorted(c)
# Out[35]: [1, 2, 3, 'another', 'some']
# In [36]: c
# Out[36]: {1: 'D', 2: 'B', 3: 'B', 'another': 'A', 'some': 'E'}

# >>> student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]
# >>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# в sorted() sort([key], [reverse]) и можно передавать два и более параметров для сортировки
# отличия в методах - sort() изменяет список к которому был применен
# sorted() - возвращает новый. `key` - применяеться для каждого элемента списка,
# а потом список сортируеться

# In [55]: lst = ['Stem', 'constitute', 'Sedge', 'Eflux', 'Whim', 'Intrigue']

# In [56]: sorted(lst, key = lambda x: x.lower())
# Out[56]: ['constitute', 'Eflux', 'Intrigue', 'Sedge', 'Stem', 'Whim']

# In [57]: lst
# Out[57]: ['Stem', 'constitute', 'Sedge', 'Eflux', 'Whim', 'Intrigue']

# In [58]: sorted(lst, key = lambda x: len(x))
# Out[58]: ['Stem', 'Whim', 'Sedge', 'Eflux', 'Intrigue', 'constitute']

# In [59]: sorted(lst, key = lambda x: (x.lower(), len(x)))
# Out[59]: ['constitute', 'Eflux', 'Intrigue', 'Sedge', 'Stem', 'Whim']

# In [60]: sorted(lst, key = lambda x: (len(x), x.lower()))
# Out[60]: ['Stem', 'Whim', 'Eflux', 'Sedge', 'Intrigue', 'constitute']




# сравнения
# In [75]: a=None
# In [76]: 1 if a else 0
# Out[76]: 0

# In [77]: a=''
# In [78]: 1 if a else 0
# Out[78]: 0

# In [79]: a='sss'
# In [80]: 1 if a else 0
# Out[80]: 1

# In [81]: a=True
# In [82]: 1 if a else 0
# Out[82]: 1

# In [83]: a=False
# In [84]: 1 if a else 0
# Out[84]: 0


# копии словарей
# т.к. в питоне переменная - всего лишь ссылка на объект:

# In [37]: c={'a':1,'b':2,'c':{'e':4,'f':5}}

# In [38]: id(c['c'])
# Out[38]: 140183671184752

# In [39]: b={k:v for k,v in c.iteritems()}

# In [40]: id(b['c'])

# Out[40]: 140183671184752

# In [41]: id(b['a'])
# Out[41]: 24027480

# In [42]: id(c['a'])
# Out[42]: 24027480

# In [44]: import copy

# In [45]: d2 = copy.deepcopy(c)

# In [46]: d2
# Out[46]: {'a': 1, 'b': 2, 'c': {'e': 4, 'f': 5}}

# In [47]: id(d2['a'])
# Out[47]: 24027480

# НО !:

# In [49]: c
# Out[49]: {'a': 1, 'b': 2, 'c': {'e': 4, 'f': 5}}

# In [50]: b
# Out[50]: {'a': 1, 'b': 2, 'c': {'e': 4, 'f': 5}}

# In [51]: d2
# Out[51]: {'a': 1, 'b': 2, 'c': {'e': 4, 'f': 5}}

# In [63]: b['a']=7

# In [64]: b
# Out[64]: {'a': 7, 'b': 2, 'c': {'e': 4, 'f': 5}}
# в словаре с - ничего не поменяеться - т.к. значение ключа Immutable  types - см стр 14
# In [65]: c
# Out[65]: {'a': 1, 'b': 2, 'c': {'e': 4, 'f': 5}}

# In [66]: b['c']['e']=8

# In [67]: b
# Out[67]: {'a': 7, 'b': 2, 'c': {'e': 8, 'f': 5}}

# In [68]: c
# Out[68]: {'a': 1, 'b': 2, 'c': {'e': 8, 'f': 5}}

# и еще:

# In [75]: a = {1:{1:2}}

# In [76]: id(a[1])
# Out[76]: 140183671204672

# In [77]: b = a.copy()

# In [78]: id(b[1])
# Out[78]: 140183671204672

# In [79]: from copy import deepcopy

# In [80]: c = deepcopy(a)

# In [81]: id(c[1])
# Out[81]: 140183671203832

# In [82]: z={k:v for k,v in a.iteritems()}

# In [83]: id(z[1])
# Out[83]: 140183671204672


# Пoчему надо использовать deepcopy:
# In [75]: a = {1:{1:2}}

# In [76]: id(a[1])
# Out[76]: 140183671204672

# In [77]: b = a.copy()

# In [78]: id(b[1])
# Out[78]: 140183671204672

# In [79]: from copy import deepcopy

# In [80]: c = deepcopy(a)

# In [81]: id(c[1])
# Out[81]: 140183671203832

# In [82]: z={k:v for k,v in a.iteritems()}

# In [83]: id(z[1])
# Out[83]: 140183671204672
