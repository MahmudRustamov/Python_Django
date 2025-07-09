import time

def timer(func):
    def wrapper(*args, **kwrgs):
        start_time = time.time()
        value = func(*args, **kwrgs)
        finish_time = time.time()
        print(finish_time - start_time)
        return func()
    return wrapper



@timer
def counter():
    ls = []
    for i in range(1000000000):
        ls.append(i)
    return ls


print(counter())

