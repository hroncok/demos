from weather import Vortex


def test_double_swirl():
    vortex = Vortex()
    # swirl() takes time, so replace it
    vortex.swirl = lambda: '@'
    assert vortex.double_swirl() == '@@'
