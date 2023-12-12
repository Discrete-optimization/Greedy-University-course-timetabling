class Data:
    def __init__(self):
        print("Data constructor is called!")
        self.classRooms = ['ClassRoom 1', 'ClassRoom 2']
        self.classTimes = ['08:00 - 10:00', '10:00 - 12:00']
        self.cources = [
            ['cource 1', 3],
            ['cource 2', 3],
            ['cource 3', 3],
            ['cource 4', 3],
            ['cource 5', 3],
            ['cource 6', 3],
            ['cource 7', 3],
            ['cource 8', 2],
            ['cource 9', 2],
            ['cource 10', 1],
            ['cource 11', 1]
        ]

    def get_classRooms(self):
        return self.classRooms

    def get_classTimes(self):
        return self.classTimes

    def get_courses(self):
        return self.cources

    def available_classes(self):
        classRooms_num = len(self.classRooms)
        classTimes_num = len(self.classTimes)

        available_class = classRooms_num * classTimes_num

        return available_class * 5 #five das in each week!



data = Data()
print(data.available_classes())