def append_to_file(text: str):
    with open(file='logs.txt', mode="a", encoding="UTF-8") as file:
        file.write(text)


def logger(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            text = f"{func.__name__}, args: {args}, kwargs: {kwargs}, result: {result}\n"
            append_to_file(text=text)
            return result
        except Exception as exc:
            text = f"{func.__name__}, args: {args}, kwargs: {kwargs}, error: {exc}\n"
            append_to_file(text=text)
            raise Exception(exc)

    return wrapper


@logger
def add(a, b):
    return a / b


print(add(1, 0))
