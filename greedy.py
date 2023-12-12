from queue import Queue
from data import Data

class Greedy:
    def __init__(self):
        print("Greedy constructor is called!")
        self.data = Data()
        self.queue = Queue(self.data)




G1 = Greedy()
print(G1.data.available_classes())