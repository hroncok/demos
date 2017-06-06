from weather import Vortex


def twice_swirled_vortex():
    vortex = Vortex()
    vortex.swirl()
    vortex.swirl()
    return vortex
