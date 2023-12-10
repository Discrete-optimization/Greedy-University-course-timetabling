class Sorting:
    def __init__(self, array):
        self.array = array

    def get_array(self):
        return self.array

    def insertionSort(self):
        n = len(self.array)  # Get the length of the array

        if n <= 1:
            return  # If the array has 0 or 1 element, it is already sorted, so return

        for i in range(1, n):  # Iterate over the array starting from the second element
            key = self.array[i][1]  # Store the current element as the key to be inserted in the right position
            j = i - 1
            while j >= 0 and key < self.array[j][1]:  # Move elements greater than key one position ahead
                self.array[j + 1][1] = self.array[j][1]  # Shift elements to the right
                j -= 1
            self.array[j + 1][1] = key  # Insert the key in the correct position

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
S = Sorting
S.insertionSort()
print(S.get_array())