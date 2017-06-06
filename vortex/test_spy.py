from functools import update_wrapper

from weather import Vortex


class Spy:
    def __init__(self, func):
        self.func = func
        self.calls = []
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.calls.append((args, kwargs))
        return self.func(*args, **kwargs)

    @property
    def call_count(self):
        return len(self.calls)


def test_double_swirl():
    vortex = Vortex()
    vortex.swirl = Spy(vortex.swirl)
    assert vortex.double_swirl() == '@@'
    assert vortex.swirl.call_count == 2
