

def my_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("code before call function")
        res = function_to_decorate()
        print("code after call function")
        return res
    return the_wrapper_around_the_original_function


@my_decorator
def another_stand_alone_function():
    return 3
    # print("function's code")

# a = another_stand_alone_function()

# Without @ decorator
# another_stand_alone_function = my_decorator(another_stand_alone_function)
# another_stand_alone_function ()


# Function take a parameters
def my_decorator_parameters_to_function(function_to_decorate):
    @functools.wraps(function_to_decorate)  # need for original __name__ , __doc__
    def the_wrapper_around_the_original_function(*args, **kwargs):
        print(args, kwargs)
        res = function_to_decorate(*args, **kwargs)
        print("code after call function with parameter")
        return res
    return the_wrapper_around_the_original_function


@my_decorator_parameters_to_function
def with_parameters_function(parameter):
    return parameter

# b = with_parameters_function(4)


def decorator_with_parameters(*dec_args, **dec_kwargs):
    def my_decorator(function):
        def wrapper(*args, **kwargs):
            print("code before call function")
            print(dec_args, dec_kwargs)
            f = function(*args, **kwargs)
            print("code after call function")
            return f
        return wrapper
    return my_decorator





@decorator_with_parameters(3)
def with_parameters_function(*args, **kwargs):
    print(args, kwargs)

# c = with_parameters_function(4)



# Simple decorator
def dec_param(d=None):
    def dec(func):
        def wrapper(a):
            print('before')
            print('dec param: {}'.format(d))
            func(a)
            print('after')
        return wrapper
    return dec

@dec_param(9)
def my(a):
    print(a)

my(5)




import functools

def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer




def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


def fibonachi(n, a=0, b=1):
    if n == 0:
        return a
    else:
        return fibonachi(n-1, b, a+b)


