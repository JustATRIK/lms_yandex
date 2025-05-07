class Human:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Student(Human):

    def __init__(self, name, university):
        super().__init__(name)
        self.university = university
        self.year = 1

    def get_university(self):
        return self.university

    def get_year(self):
        return self.year

    def study(self):
        if self.year < 6:
            self.year += 1


class Employee(Human):

    POSITIONS = ["junior", "middle", "senior", "lead"]

    def __init__(self, name, company):
        super().__init__(name)
        self.company = company
        self.position = 0

    def get_company(self):
        return self.company

    def get_position(self):
        return Employee.POSITIONS[self.position]

    def work(self):
        if self.position < len(Employee.POSITIONS) - 1:
            self.position += 1
