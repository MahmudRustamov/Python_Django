def numbers():
    counter = 1

    while True:
        yield counter
        counter += 1


for i in numbers():
    print(i)