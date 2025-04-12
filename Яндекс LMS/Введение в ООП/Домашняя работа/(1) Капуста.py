class Cabbage:
    
    def __init__(self, start, step, end):
        self._size = start
        self.step = step
        self.end = end
    
    def leaf(self):
        self._size -= self.step
        if self._size < self.end:
            self._size = self.end
        print(self._size)
        