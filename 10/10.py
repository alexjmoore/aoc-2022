class CPU:
    def __init__(self):
        self.X = 1
        self.cycle = 0
        self.signal_strengths = []

    def noop(self):
        self.__cycle()

    def addx(self, value):
        self.__cycle()
        self.__cycle()
        self.X += value

    def __cycle(self):
        self.cycle += 1
        if (self.cycle - 20) % 40 == 0:
            self.signal_strengths.append(self.cycle * self.X)

theCPU = CPU()

with open('input.txt') as input:
    while line := input.readline().strip():
        if line.startswith("noop"):
            theCPU.noop()
        else:
            _, value = line.split()
            theCPU.addx(int(value))

    print(f"sum of all signal strengths: {sum(theCPU.signal_strengths)}")