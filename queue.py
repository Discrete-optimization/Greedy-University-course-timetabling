class Queue:
    def __init__(self, list):
        self.list = list

    def get_list(self):
        return self.list


list = ['A', 'B', 'C']
Q = Queue(list)
print(Q.get_list())