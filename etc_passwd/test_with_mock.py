from io import StringIO
from unittest.mock import Mock, patch

from etc_passwd import parse_etc_passwd


def test_parse_etc_passwd():
    fake_file = StringIO('faker:x:666:666:faker:/home/faker:/bin/fake\n')
    with patch('builtins.open', Mock(return_value=fake_file)):
        users = parse_etc_passwd()
        assert open.call_count == 1
    assert 'faker' in users
    assert len(users) == 1
