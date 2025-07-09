def my_decerator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called")
        print(args)
        value = func(*args, **kwargs)
        print("After the function is called")
        return value
    
    return wrapper


@my_decerator
def add(a, b):
    return a + b

@my_decerator
def greeting(name):
    return f"Hello, {name}"

print(add(1, 2))
print(greeting("Mahmud"))