###################################
#   Created by Robert Choi 2020   #
#  https://github.com/robert-choi #
###################################

from random import randint
from time import sleep

class QuickSorter():
    """
    Sort the sort_list using quick sort algorithm
    :param sort_list: List[int]
    :param show_solving: bool
    """
    def __init__(self, sort_list, show_solving=False):
        self.sort_list = sort_list
        self.show_solving = show_solving
        self.sort(0, len(self.sort_list)-1)

    def sort(self, start, end):
        """
        Called recursively by itself. The last item in the block (start, end)
        is chosen as the pivot. All items smaller than the pivot are moved to
        the left side of the block.
        :param start: int
        :param end: int
        """
        if start >= end:
            return
        counter = start
        pivot = self.sort_list[end]
        for i in range(start, end):
            if pivot > self.sort_list[i]:
                self.sort_list[i], self.sort_list[counter] = self.sort_list[counter], self.sort_list[i]
                counter += 1
        self.sort_list[end], self.sort_list[counter] = self.sort_list[counter], self.sort_list[end]

        if self.show_solving:
            print('\n',self.sort_list)
            sleep(0.1)

        self.sort(start, counter-1)
        self.sort(counter+1, end)

example = []
for i in range(0,30):
    example.append(randint(10,99))

a = QuickSorter(example, True)