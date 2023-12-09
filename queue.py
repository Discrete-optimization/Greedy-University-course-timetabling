class Queue:
    def __init__(self, list):
        self.list = list

    def get_list(self):
        return self.list


list = [('A', 3), ('B', 3), ('C', 3), ('D', 2), ('E', 2), ('F', 1)]
Q = Queue(list)
print(Q.get_list())