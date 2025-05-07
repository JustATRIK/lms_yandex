class TwoFacedJanus:
    
    def __init__(self, face='future'):
        self.face = face

    def __call__(self, arg):
        if self.face == 'future':
            numbers = range(arg, arg + 10)
        else:
            numbers = range(arg, arg - 10, -1)

        result = []
        for num in numbers:
            result.append(str(num))
            if num == 0:
                break

        print(' '.join(result))
        