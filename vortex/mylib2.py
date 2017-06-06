from weather import Vortex


def twice_swirled_vortex(vortex=None):
    vortex = vortex or Vortex()
    vortex.swirl()
    vortex.swirl()
    return vortex
