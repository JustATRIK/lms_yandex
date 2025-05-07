class FastFibonacci:
    
    _cache = {1: 1, 2: 1}

    def __call__(self, num):
        if num in self._cache:
            return self._cache[num]
        if num - 1 not in self._cache:
            num_prev = self.__call__(num - 1)
        else:
            num_prev = self._cache[num - 1]
        self._cache[num] = num_prev + self._cache[num - 2]
        return self._cache[num]
