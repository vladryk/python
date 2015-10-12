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
