#! /usr/bin/env python

# chmod +x ./run.py

# def data(d=[]):
#     'Some data'
#     d.append(1)
#     return d
#
# if data()==[] or data()==[1]:
#     print data().__doc__
# elif len(data([0]))<=10 and len(data())>=4:
#     print len(data())
# else:
#     print len(data())





# input = [1, 3, [2, 4, [2, 5], 2], 6, [3, ], ]
# output = [1, 3, 2, 4, 2, 5, 2, 6, 3, ]
#
# def plain(input):
#     l=[]
#     for i in input:
#         if not isinstance(i, (list, tuple)):
#             l.append(i)
#         else:
#             l.extend(plain(i))
#     return l
#
# print(plain(input))
