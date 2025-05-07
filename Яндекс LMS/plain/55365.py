class Marks:

    def __init__(self, name, second_name, marks):
        self.name = name
        self.second_name = second_name
        self.marks = marks

    def set_mark(self, subject, mark):
        self.marks[subject] = mark

    def get_marks(self):
        return self.marks

    def __eq__(self, other):
        return other.marks == self.marks

    def __repr__(self):
        return f"Marks({self.name=}, {self.second_name=}, {self.marks=})".replace("self.", "")

