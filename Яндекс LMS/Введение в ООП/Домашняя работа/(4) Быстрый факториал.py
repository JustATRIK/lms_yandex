class QuickFactorial:

    _cache = {0: 1}

    def result(self, fact):
        if fact in self._cache.items():
            return self._cache[fact]

        maxx = self._cache[max(self._cache.keys())]
        for i in range(maxx + 1, fact + 1):
            maxx *= i
            self._cache[i] = maxx
        return maxx
