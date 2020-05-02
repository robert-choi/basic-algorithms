from time import sleep

class BubbleSorter():
    def __init__(self, sort_list, show_solving=False):
        """
        Sorts the sort_list using bubble sorting algorithm
        :param sort_list: List[int]
        :param show_solving: bool
        """
        self.show_solving = show_solving
        self.sort_list = self.sort(sort_list)
    
    def sort(self, sort_list):
        """
        The actual sorting
        :param sort_list: List[int]
        """
        sorting = True
        while sorting:
            swap_done = False
            for i in range(len(sort_list)-1):
                if sort_list[i] > sort_list[i+1]:
                    sort_list[i], sort_list[i+1] = sort_list[i+1], sort_list[i]
                    swap_done = True

            if self.show_solving:
                for spacer in range(5): #pylint: disable=unused-variable
                    print()
                print(sort_list)
                sleep(0.05)

            if not swap_done:
                break
        return sort_list

##########################################################################

a = BubbleSorter([166, 459, 382, 578, 498, 125, 447, 548, 537, 461, 505, 377, 504, 356, 250, 106, 222, 469, 347, 558, 220, 400, 297, 118, 248, 492, 207, 413, 534, 205, 353, 449, 513, 117, 446, 586, 492, 357, 510, 367, 243, 211, 165, 134, 412, 144, 485, 519, 172, 375, 404, 179, 262, 172, 322, 530, 377, 214, 443, 183, 152, 343, 515, 475, 529, 468, 277, 392, 322, 187, 582, 288, 541, 399, 429, 307, 594, 231, 420, 411, 175, 423, 571, 568, 594, 137, 592, 332, 588, 212, 383, 190, 245, 313, 271, 585, 228, 176, 225, 546, 450, 150, 223, 273, 396, 493, 259, 222, 153, 188, 457, 146, 410, 152, 391, 336, 181, 530, 566, 578, 289, 400, 252, 271, 183, 523, 528, 358, 581, 582, 260, 483, 590, 331, 395, 366, 480, 110, 481, 136, 478, 137, 566, 599, 326, 398, 374, 339, 598, 331, 265, 399, 412, 264, 273, 179, 539, 428, 470, 111, 137, 154, 221, 409, 363, 242, 217, 193, 523, 179, 424, 163, 556, 420, 324, 120, 222, 353, 346, 438, 414, 490, 438, 471, 589, 520, 278, 349, 251, 158, 430, 499, 453, 445, 424, 114, 261, 182, 202, 342], True)