def seq_numbers(num):
    for i in range(1, num+1):
        yield i ** 2


numbers = seq_numbers(20)
for i in numbers:
    print(i)

