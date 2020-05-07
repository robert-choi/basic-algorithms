###################################
#   Created by Robert Choi 2020   #
#  https://github.com/robert-choi #
###################################

from random import randint
from time import sleep

class MergeSorter():
    """
    Sort the sort_list using merge sort algorithm
    :param sort_list: List[int]
    :param show_solving: bool
    """
    def __init__(self, sort_list, show_solving=False):
        self.sort_list = sort_list
        self.show_solving = show_solving
        self.sort(self.sort_list)

    def sort(self, sort_list):
        """
        Called recursively by self on each half of inputted list. Each half is 
        divided to parts of one, merged together while sorting the smaller 
        elements
        :param sort_list: List[int]
        """
        if len(sort_list) <= 1:
            return
        center = len(sort_list)//2
        left = sort_list[:center]
        right = sort_list[center:]

        self.sort(left)
        self.sort(right)

        i = 0
        while left and right:
            if self.show_solving:
                print(sort_list, left, right)
                sleep(0.1)
            if left[0] < right[0]:
                sort_list[i] = left.pop(0)
            else:
                sort_list[i] = right.pop(0)
            i += 1
        if left:
            sort_list[i:] = left
        elif right:
            sort_list[i:] = right

        if self.show_solving:
                print(sort_list,'\n')
                sleep(0.1)

example = []
for i in range(0,30):
    example.append(randint(10,99))
a = MergeSorter(example, True)
