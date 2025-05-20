class Service:

    def __init__(self, address, id):
        self.address = address
        self.id = id

    def arrival_time(self):
        return len(self.address)

    def get(self):
        return self.__dict__


class Ambulance(Service):

    def __init__(self, address, id, mode, severity):
        super().__init__(address, id)
        self.mode = mode
        self.severity = severity


class Firefighters(Service):

    def __init__(self, address, id, mode, victims):
        super().__init__(address, id)
        self.mode = mode
        self.victims = victims


class Police(Service):

    def __init__(self, address, id, mode, victims, armament_required):
        super().__init__(address, id)
        self.mode = mode
        self.victims = victims
        self.armament_required = armament_required

