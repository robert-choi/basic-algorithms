###################################
#   Created by Robert Choi 2020   #
#  https://github.com/robert-choi #
###################################

import tkinter as tk
from random import randint

class InsertionSorterGUI():
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
            self.sort_list.append([random_height, line_id])
        self.window.update()

    ##########################################################################

    def start_sorting(self):
        """
        Starts the sorter using basic insertion sort algorithm 
        The line being compared is highlighted in red, upon completion, all 
        lines turn green
        """
        self.sorting = True
        for i, line in enumerate(self.sort_list):
            if not self.sorting:
                break
            if i==0:
                continue
            del self.sort_list[i]
            self.window.itemconfig(line[1], fill='red')
            self.window.update()
            self.insert(i, line, 0)

            if i == len(self.sort_list)-1:
                self.sorting = False
                for complete_line in self.sort_list:
                    self.window.itemconfig(complete_line[1], fill='green')
                self.window.update()

    def insert(self, index, line, lines_skipped=None):
        """
        Called implicitly from the start_sorting method. The skipped lines are 
        highlighted before returning to the main function
        :param index: int
        :param line: List
        :param lines_skipped: int
        """
        if not self.sorting:
            return
        if index == 0:
            pass
        elif line[0] < self.sort_list[index-1][0]:
            lines_skipped += 1
            self.window.itemconfig(self.sort_list[index-1][1], fill='blue')
            self.window.update()
            self.window.itemconfig(self.sort_list[index-1][1], fill='orange')
            self.window.update()
            self.insert(index-1, line, lines_skipped)
            return

        self.sort_list.insert(index, line)
        self.window.coords(line[1], 4*index+50, 20, 4*index+50, line[0])
        self.window.itemconfig(line[1], fill='black')
        for i in range(index+1, index+lines_skipped+1):
            self.window.coords(self.sort_list[i][1], 4*i+50, 20, 4*i+50, self.sort_list[i][0])
            self.window.itemconfig(self.sort_list[i][1], fill='black')
        self.window.update()

##########################################################################

root = tk.Tk()
sorter = InsertionSorterGUI(root)
root.mainloop()
