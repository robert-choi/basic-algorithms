from random import randint
from time import sleep

class InsertionSorter():
    def __init__(self, sort_list):
        self.sort_list = sort_list
        self.sort()

    def sort(self):
        for i, num in enumerate(self.sort_list):
            if i == 0:
                continue
            del self.sort_list[i]
            self.insert(num, i)
            print(self.sort_list)
            sleep(0.5)

    def insert(self, item, index):
        if index == 0:
            self.sort_list.insert(index, item)
        elif item < self.sort_list[index-1]:
            self.insert(item, index-1)
        else:
            self.sort_list.insert(index, item)

do = []
for i in range(20):
    do.append(randint(10,50))
print(do)

a = InsertionSorter(do)