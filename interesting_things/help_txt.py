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
# sorted() - возвращает новый

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
