from mylib2 import twice_swirled_vortex


class FakeVortex:
    counter = 0

    def swirl(self):
        self.counter += 1


def test_swirl_twice():
    vortex = FakeVortex()
    twice_swirled_vortex(vortex)
    assert vortex.counter == 2
