class Avalanche:

    def __init__(self):
        self.value = ""

    def go(self):
        if self.value == "":
            self.value = "O"
        else:
            tmp = ""
            for i in self.value:
                tmp += "ooOoo" if i == "O" else "oOo"
            self.value = tmp
        print(self.value)
        