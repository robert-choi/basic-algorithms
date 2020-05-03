###################################
#   Created by Robert Choi 2020   #
#  https://github.com/robert-choi #
###################################

from random import randint
from time import sleep

class BubbleSorter():
    """
    Sorts the sort_list using bubble sorting algorithm
    :param sort_list: List[int]
    :param show_solving: bool
    """
    def __init__(self, sort_list, show_solving=False):
        self.show_solving = show_solving
        self.sort_list = self.sort(sort_list)
    
    def sort(self, sort_list):
        """
        The main loop for the bubble sort method. Swaps items if they appear 
        out of order
        :param sort_list: List[int]
        """
        sorting = True
        passes = 0
        while sorting:
            swap_done = False
            for i in range(len(sort_list)-passes-1):
                if sort_list[i] > sort_list[i+1]:
                    sort_list[i], sort_list[i+1] = sort_list[i+1], sort_list[i]
                    swap_done = True
            passes +=1

            if self.show_solving:
                for spacer in range(5): #pylint: disable=unused-variable
                    print()
                print(sort_list)
                sleep(0.05)
            
            if not swap_done:
                break
        return sort_list

##########################################################################

example = []
for i in range(100):
    example.append(randint(100,999))

a = BubbleSorter(example, True)
