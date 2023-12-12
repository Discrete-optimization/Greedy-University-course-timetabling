from queue import Queue
from data import Data
from queue import Sorting

class Greedy:
    def __init__(self):
        print("Greedy constructor is called!")
        self.data = Data()
        self.queue = Queue(self.data.get_courses())

    def greedy(self):
        for room in self.data.get_classRooms():
            for time in self.data.get_classTimes():
                print(room, time, end=" ")
            print("...")

G1 = Greedy()
G1.greedy()