class CPU:
    def __init__(self):
        self.X = 1
        self.cycle = 0
        self.rows = ''

    def noop(self):
        self.__cycle()

    def addx(self, value):
        self.__cycle()
        self.__cycle()
        self.X += value

    def __cycle(self):
        if (self.cycle % 40 >= self.X - 1) and (self.cycle % 40 <= self.X + 1):
            self.rows +='#'
        else:
            self.rows +='.'

        self.cycle += 1
        if (self.cycle) % 40 == 0:
            self.rows += '\n'


theCPU = CPU()

with open('input.txt') as input:
    while line := input.readline().strip():
        if line.startswith('noop'):
            theCPU.noop()
        else:
            _, value = line.split()
            theCPU.addx(int(value))

    print(f"{theCPU.rows}")
