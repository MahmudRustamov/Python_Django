import time

class LsIterator:
    def __init__(self, ls):
        self.ls = ls
        self.cur_index = 0


    def __iter__(self):
        return self
    

    def __next__(self):
        if len(self.ls) <= self.cur_index:
            raise StopIteration
        else:
            value = self.ls[self.cur_index]                                 
            self.cur_index += 1
            return value


    def start_from(self, index):
        if 0 <= index < len(self.ls):
            self.cur_index = index
        else:
            raise ValueError("Index is out of range")
        return self
    

    def random_num(self):
        r_didgit = str(time.time())[-1]
        print(self.ls[int(r_didgit)])
        



new = LsIterator([1,8,3,45,6,7,89,9,12])
# for item in new.start_from(3):
#     print(item)

new.random_num()


