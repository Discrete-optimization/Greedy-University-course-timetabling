class Sorting:
    def __init__(self, array):
        self.array = array

    def get_array(self):
        return self.array

    def insertionSort(self):
        self.array.sort(key=lambda x: x[1], reverse=True)

class Queue:
    def __init__(self, list):
        self.list = list

    def get_list(self):
        return self.list

    def dequeue(self):
        current_element = self.list[0]
        current_sign = current_element[0]
        current_value = current_element[1]
        current_value = current_value - 1

        self.list.remove(current_element)

        new_element = (current_sign, current_value)
        self.list.append(new_element)

    def pop(self):
        item = self.list[0]
        self.dequeue()
        return item


    def printer(self):
        for element in self.list:
            print("{} with value: {}".format(element[0], element[1]))


list = [('A', 3), ('B', 3), ('C', 3), ('D', 2), ('E', 2), ('F', 1)]
S = Sorting(list)
S.insertionSort()
print(S.get_array())