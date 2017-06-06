from unittest.mock import Mock

from weather import Vortex


def test_double_swirl():
    vortex = Vortex()
    vortex.swirl = Mock(return_value='@')
    assert vortex.double_swirl() == '@@'
    assert vortex.swirl.call_count == 2
