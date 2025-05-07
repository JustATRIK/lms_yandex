class EmergencyCall:

    def __init__(self, name, surname, message="Alarm!", date=None, time=None):
        self.date = date
        self.message = message
        self.surname = surname
        self.name = name
        self.time = time

    def __repr__(self):
        return f"EmergencyCall({self.name=}, {self.surname=}, {self.message=}, {self.date=}, {self.time=})".replace(
            "self.", "")

    def __str__(self):
        return f"""Имя, фамилия: {self.name} {self.surname}
Сообщение: {self.message}
Дата, время: {self.date}, {self.time}"""
