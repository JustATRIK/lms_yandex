class Inversion:

    @staticmethod
    def solve(x):
        return not x

    @staticmethod
    def truth_table():
        print("X\tF")
        for x in [0, 1]:
            f = int(not x)
            print(f"{x}\t{f}")


class Conjunction:

    @staticmethod
    def solve(x, y):
        return x and y

    @staticmethod
    def truth_table():
        print("X\tY\tF")
        for x in [0, 1]:
            for y in [0, 1]:
                f = int(x and y)
                print(f"{x}\t{y}\t{f}")


class Disjunction:

    @staticmethod
    def solve(x, y):
        return x or y

    @staticmethod
    def truth_table():
        print("X\tY\tF")
        for x in [0, 1]:
            for y in [0, 1]:
                f = int(x or y)
                print(f"{x}\t{y}\t{f}")


def info(obj):
    print(f"Truth table of {obj.__class__.__name__}:")
    obj.truth_table()
