from queue import Queue
from data import Data
from queue import Sorting

class Greedy:
    def __init__(self):
        print("Greedy constructor is called!")
        self.data = Data()
        self.queue = Queue(self.data.get_courses())

    def greedy(self):
        result = []
        for day in self.data.get_weeDays():
            print(day)
            for room in self.data.get_classRooms():
                for time in self.data.get_classTimes():
                    top = self.queue.get_first()
                    if(top[1] > 0):
                        course = self.queue.pop()
                        curr_cell = [room, time, course]
                        result.append(curr_cell)
                        print(course, end=" ")
                print("...")

        print(self.queue.get_list())

G1 = Greedy()
G1.greedy()