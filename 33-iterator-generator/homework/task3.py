import datetime


# def my_generator():
#     num = 1
#     while True:
#         yield num
#         num += 1
#
#
# for i in my_generator():
#     print(i)


class MyList:
    def __init__(self, my_list: list):
        self.my_list = my_list

    def start_index(self, index: int):
        if len(self.my_list) > index >= (len(self.my_list) * -1):
            return self.my_list[index:]
        else:
            return []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.my_list) == 0:
            raise StopIteration
        return self.random()

    def random(self):
        random_index = int(str(datetime.datetime.now().microsecond)[-1]) % len(self.my_list)
        value = self.my_list.pop(random_index)
        return value


obj = MyList(my_list=[1, 241, 4, 11])
for num in obj:
    print(num)
