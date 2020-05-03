import tkinter as tk
from random import randint

class InsertionSorterGUI():
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
            random_height = randint(20,260)
            line_id = self.window.create_line(4*i+50, 20, 4*i+50, random_height+20)
            self.sort_list.append([random_height, line_id])
        self.window.update()

    def start_sorting(self):
        self.sorting = True
        for i, line in enumerate(self.sort_list):
            if not self.sorting:
                break
            if i==0:
                continue
            del self.sort_list[i]
            self.window.delete(line[1])
            line[1] = self.window.create_line(4*i+50, 20, 4*i+50, line[0], fill='red')
            self.window.update()
            self.insert(i, line)
        print(self.sort_list)

    def insert(self, index, line):
        if index == 0:
            self.sort_list.insert(index, line)
        elif line[0] < self.sort_list[index-1][0]:
            self.insert(index-1, line)
        else:
            self.sort_list.insert(index, line)

##########################################################################

root = tk.Tk()
sorter = InsertionSorterGUI(root)
root.mainloop()
