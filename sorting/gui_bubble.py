###################################
#   Created by Robert Choi 2020   #
#  https://github.com/robert-choi #
###################################

import tkinter as tk
from random import randint

class BubbleSorterGUI():
    def __init__(self, master):
        """
        Initialize all variables and widgets, then pack onto the window
        :param master: tkinter.Tk object
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
            self.sort_list.append([random_height, line_id])
        self.window.update()

    def start_sorting(self):
        """
        Starts the sorter using basic bubble sort algorithm
        Swaps are highlighted in red, upon completion the lines will turn green
        """
        if self.sorting:
            return None
        self.sorting = True

        passes = 0
        while self.sorting:
            swap_done = False
            for i in range(len(self.sort_list)-passes-1):
                if not self.sorting:
                    break
                if self.sort_list[i][0] > self.sort_list[i+1][0]:
                    self.sort_list[i], self.sort_list[i+1] = self.sort_list[i+1], self.sort_list[i]
                    self.window.coords(self.sort_list[i][1], 4*i+50, 20, 4*i+50, self.sort_list[i][0])
                    self.window.coords(self.sort_list[i+1][1], 4*(i+1)+50, 20, 4*(i+1)+50, self.sort_list[i+1][0])
                    self.window.itemconfig(self.sort_list[i][1], fill='red')
                    self.window.itemconfig(self.sort_list[i+1][1], fill='red')
                    swap_done = True
                    self.window.update()
                    self.window.itemconfig(self.sort_list[i][1], fill='black')
                    self.window.itemconfig(self.sort_list[i+1][1], fill='black')
                    self.window.update()
            passes += 1

            if not swap_done:
                self.sorting = False
                for line in self.sort_list:
                    self.window.itemconfig(line[1], fill='green')
                self.window.update()

##########################################################################

root = tk.Tk()
sorter = BubbleSorterGUI(root)
root.mainloop()
