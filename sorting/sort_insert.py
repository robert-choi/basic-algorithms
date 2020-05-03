###################################
#   Created by Robert Choi 2020   #
#  https://github.com/robert-choi #
###################################

from random import randint
from time import sleep

class InsertionSorter():
    """
    Sort the sort_list using insertion sort algorithm
    :param sort_list: List[int]
    :param show_solving: bool
    """
    def __init__(self, sort_list, show_solving=False):
        self.sort_list = sort_list
        self.show_solving = show_solving
        self.sort()

    def sort(self):
        """
        The main for loop to iterate through the sort_list
        Each iteration will call the self.insert() method
        """
        for i, num in enumerate(self.sort_list):
            if i == 0:
                continue
            del self.sort_list[i]
            self.insert(num, i)
            if self.show_solving:
                print('\n',self.sort_list)
                sleep(0.1)

    def insert(self, item, index):
        """
        Called implicitly from self.sort() and recursively by self
        Re-inserts item into list once an appropriate location is found
        :param item: int
        :param index: int
        """
        if index == 0:
            self.sort_list.insert(index, item)
        elif item < self.sort_list[index-1]:
            self.insert(item, index-1)
        else:
            self.sort_list.insert(index, item)

example = []
for i in range(20):
    example.append(randint(10,50))

a = InsertionSorter(example, True)