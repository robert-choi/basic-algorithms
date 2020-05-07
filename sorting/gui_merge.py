###################################
#   Created by Robert Choi 2020   #
#  https://github.com/robert-choi #
###################################

import tkinter as tk
from random import randint

class MergeSorterGUI():
    """
    A window widget with buttons to give a visual representation of the merge 
    sorting algorithm
    :param master: tkinter.Tk object
    """
    def __init__(self, master):
        """
        Initialize all variables and widgets, then pack onto the window
        """
        self.window = tk.Canvas(master, width=500, height=300)
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_window)
        self.start_button = tk.Button(master, text="Start", command=self.start_sorting)
        self.window.pack()
        self.reset_button.pack()
        self.start_button.pack()
        self.reset_window()

    ##########################################################################

    def reset_window(self):
        """
        Reset the sorting list, then draw the new line set with random heights
        """
        self.sorting = False
        self.sort_list = []
        self.window.delete('all')
        for i in range(100):
            random_height = randint(40,280)
            line_id = self.window.create_line(4*i+50, 20, 4*i+50, random_height)
            self.sort_list.append((random_height, line_id))
        self.window.update()

    ##########################################################################

    def start_sorting(self):
        """
        Starts the sorter using basic quick sort algorithm. 
        """
        if self.sorting:
            return None
        self.sorting = True
        self.merge_sort(self.sort_list, 0)
        if self.sorting:
            for line in self.sort_list:
                self.window.itemconfig(line[1], fill='green')
            self.window.update()
        self.sorting = False

    def merge_sort(self, sort_list, start_index):
        if len(sort_list) <= 1:
            return
        center = len(sort_list)//2
        left = sort_list[:center]
        right = sort_list[center:]

        self.merge_sort(left, start_index)
        self.merge_sort(right, center)

        for i_fill in range(start_index, len(sort_list)):
            self.window.itemconfig(self.sort_list[i_fill][1], fill='orange')
            self.window.update()

        i = 0
        while left and right:
            if left[0][0] < right[0][0]:
                sort_list[i] = left.pop(0)
            else:
                sort_list[i] = right.pop(0)
            self.window.itemconfig(self.sort_list[start_index+i][1], fill='blue')
            self.window.coords(self.sort_list[start_index+i][1], 4*(start_index+i)+50, 20, 4*(start_index+i)+50, sort_list[i][0])
            i += 1
            self.window.update()

        if left:
            for item_l in left:
                sort_list[i] = item_l
                self.window.itemconfig(self.sort_list[start_index+i][1], fill='blue')
                self.window.coords(self.sort_list[start_index+i][1], 4*(start_index+i)+50, 20, 4*(start_index+i)+50, sort_list[i][0])
                i += 1
                self.window.update()
        elif right:
            for item_r in right:
                sort_list[i] = item_r
                self.window.itemconfig(self.sort_list[start_index+i][1], fill='blue')
                self.window.coords(self.sort_list[start_index+i][1], 4*(start_index+i)+50, 20, 4*(start_index+i)+50, sort_list[i][0])
                i += 1
                self.window.update()

        for i_fill in range(start_index, len(sort_list)):
            self.window.itemconfig(self.sort_list[i_fill][1], fill='black')
        self.window.update()

##########################################################################

root = tk.Tk()
sorter = MergeSorterGUI(root)
root.mainloop()
