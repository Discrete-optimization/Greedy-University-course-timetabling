from queue import Queue
from data import Data



data = Data()
courses = data.get_courses()

queue = Queue(courses)
print(queue.get_list())
