class Sorting:
    def __init__(self, array):
        print("Sorting constructor is called!")
        self.array = array

    def get_array(self):
        return self.array

    def sort(self):
        self.array.sort(key=lambda x: x[1], reverse=True)

class Queue:
    def __init__(self, list):
        print("Queue constructor is called!")
        sorter = Sorting(list)
        sorter.sort()
        list = sorter.get_array()
        self.list = list

    def get_list(self):
        return self.list

    def get_first(self):
        if(len(self.list) > 0):
            return self.list[0]
        else:
            return [0, 0]

    def dequeue(self):
        current_element = self.list[0]
        current_sign = current_element[0]
        current_value = current_element[1]
        current_value = current_value - 1

        self.list.remove(current_element)

        new_element = [current_sign, current_value]
        self.list.append(new_element)

    def pop(self):
        item = self.list[0]
        self.dequeue()
        return item


    def remove(self, item):
        if (len(self.list) > 0):
            self.list.remove(item)


    def printer(self):
        for element in self.list:
            print("{} with value: {}".format(element[0], element[1]))