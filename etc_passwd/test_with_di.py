from etc_passwd_di import parse_etc_passwd


def test_parse_etc_passwd(tmpdir):
    passwd = tmpdir.join('passwd')
    passwd.write('faker:x:666:666:faker:/home/faker:/bin/fake\n')
    users = parse_etc_passwd(passwd)
    assert 'faker' in users
    assert len(users) == 1
