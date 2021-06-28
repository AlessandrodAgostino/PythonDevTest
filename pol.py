import random

class Pol:
    def __init__(self, mon_list):
        self.mon_list = mon_list

    def __str__(self):
        return ' '.join([p.__str__() for p in self.mon_list])

    def sort(self, reverse=False):
        self.mon_list.sort(reverse=reverse, key = lambda m : m.degree)

    def shuffle(self):
        random.shuffle(self.mon_list)
