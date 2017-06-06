import random


class Vortex:
    def swirl(self):
        for _ in range(10000):
            print(chr(random.randrange(255, 512)), end='')
        print()
        return '@'

    def double_swirl(self):
        return self.swirl() + self.swirl()
