class Controller:

    channel = 1

    def click(self):
        self.channel = (self.channel % 5) + 1
