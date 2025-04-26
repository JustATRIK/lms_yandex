class Rewrite:

    def __init__(self, in_file, out_file):
        self.in_file = in_file
        self.out_file = out_file

    def read(self):
        return open(self.in_file, "r").read()

    def write(self, data):
        open(self.out_file, "w").write(data)

    def done(self):
        self.write(self.read())


class Calculus(Rewrite):

    def new_read(self):
        data = self.read()
        nums = []
        last_num = ""
        for symbol in data:
            if symbol.isdigit():
                last_num += symbol
            else:
                if last_num != "":
                    nums.append(int(last_num))
                last_num = ""
        if last_num != "":
            nums.append(int(last_num))
        return sorted(nums)

    def five_per_line(self):
        nums = self.new_read()
        to_write = ""
        for ind, num in enumerate(nums, 1):
            to_write += str(num) + " "
            if ind % 5 == 0:
                to_write += "\n"
        self.write(to_write)


class Align(Rewrite):

    def new_read(self):
        words = []
        lines = (self.read() + "\n").split("\n")
        for line in lines:
            line += " "
            for word in line.split():
                words.append(word.strip())
        max_len = len(max(words, key=len))
        return list(map(lambda x: " " * (max_len - len(x)) + x, words))

    def to_right(self):
        self.write("\n".join(self.new_read()))



