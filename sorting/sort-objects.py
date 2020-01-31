from operator import attrgetter


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'({self.name},{self.age},${self.salary})'


e1 = Employee('Alice', 23, 400)
e2 = Employee('Moreen', 25, 500)
e3 = Employee('Beatrice', 25, 100)

emps = [e1, e2, e3]

'''Sorting Objects
To sort 'emps' above, we have to provide a criteria to use while sorting
'''


def sort_by_name(emp):
    return emp.name


sorted_emps_name = sorted(emps, key=sort_by_name)
# [(Alice,23,$400), (Beatrice,25,$100), (Moreen,25,$500)]
print(sorted_emps_name)

# using lambdas:
sorted_emps_age = sorted(emps, key=lambda e: e.age)
# [(Alice,23,$400), (Moreen,25,$500), (Beatrice,25,$100)]
print(sorted_emps_age)

# Using the inbuilt  attrgetter to sort by attribute:
sorted_emps_salary = sorted(emps, key=attrgetter('salary'))
# [(Beatrice,25,$100), (Alice,23,$400), (Moreen,25,$500)]
print(sorted_emps_salary)
