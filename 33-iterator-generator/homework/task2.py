def numbers():
    counter = 1

    while True:
        yield counter
        counter += 1


n = int(input("N = "))

num_generator = numbers()
for i in range(n):
    print(next(num_generator))