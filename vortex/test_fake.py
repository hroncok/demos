from mylib import swirl_twice


class FakeVortex:
    counter = 0

    def swirl(self):
        self.counter += 1


def test_swirl_twice():
    vortex = FakeVortex()
    swirl_twice(vortex)
    assert vortex.counter == 2
