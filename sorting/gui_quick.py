###################################
#   Created by Robert Choi 2020   #
#  https://github.com/robert-choi #
###################################

import tkinter as tk
from random import randint

class QuickSorterGUI():
    """
    Initialize all variables and widgets, then pack onto the window
    :param master: tkinter.Tk object
    """
    def __init__(self, master):
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
        self.quick_sort(0, len(self.sort_list)-1)
        if self.sorting:
            for line in self.sort_list:
                self.window.itemconfig(line[1], fill='green')
            self.window.update()
        self.sorting = False

    def quick_sort(self, start, end):
        """
        Called recursively by itself. The last item in the block (start, end)
        is chosen as the pivot. All items smaller than the pivot are moved to
        the left side of the block.
        :param start: int
        :param end: int
        """
        if start >= end:
            self.window.itemconfig(self.sort_list[end][1], fill='black')
            self.window.update()
            return

        counter = start
        pivot = self.sort_list[end]
        self.window.itemconfig(pivot[1], fill='red')
        self.window.update()

        for i in range(start, end):
            if not self.sorting:
                return
            if pivot[0] > self.sort_list[i][0]:
                self.sort_list[i], self.sort_list[counter] = self.sort_list[counter], self.sort_list[i]
                self.window.itemconfig(self.sort_list[counter][1], fill='blue')
                self.window.coords(self.sort_list[i][1], 4*i+50, 20, 4*i+50, self.sort_list[i][0])
                self.window.coords(self.sort_list[counter][1], 4*counter+50, 20, 4*counter+50, self.sort_list[counter][0])
                self.window.update()
                counter += 1
                self.window.itemconfig(self.sort_list[counter-1][1], fill='orange')
                self.window.update()

        self.sort_list[end], self.sort_list[counter] = self.sort_list[counter], self.sort_list[end]
        self.window.coords(self.sort_list[end][1], 4*end+50, 20, 4*end+50, self.sort_list[end][0])
        self.window.coords(self.sort_list[counter][1], 4*counter+50, 20, 4*counter+50, self.sort_list[counter][0])
        for line_id in range(start, counter+1):
            self.window.itemconfig(self.sort_list[line_id][1], fill='black')
        self.window.update()

        self.quick_sort(start, counter-1)
        self.quick_sort(counter+1, end)

##########################################################################

root = tk.Tk()
sorter = QuickSorterGUI(root)
root.mainloop()
