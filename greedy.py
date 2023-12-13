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
                    loop_counter = 0
                    while(top[1] == 0):
                        loop_counter += 1
                        if(loop_counter >= len(self.queue.get_list())):
                            break
                        self.queue.remove(top)
                        top = self.queue.get_first()

                    if(top[1] > 0):
                        course = self.queue.pop()
                        curr_cell = [room, time, course]
                        result.append(curr_cell)
        return result


G1 = Greedy()
print(G1.greedy())