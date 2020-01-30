import calendar
import datetime
import random
import sys

from my_module import find_index

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')

print(index)
print(sys.path)

random_course = random.choice(courses)

print(f'Random Course: {random_course}')

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))
