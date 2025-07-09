def my_outer_decorater(num):
    def my_decorater(func):
        def wrapper(*args, **kwargs):
            for _ in range(num -1 ):
                result = func(*args, **kwargs)
                print(result)
            return result
        return wrapper
    return my_decorater


@my_outer_decorater(3)
def add(a, b):
    return a + b

print(add(3, 5))