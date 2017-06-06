from pathlib import Path


def parse_etc_passwd():
    users = {}
    path = Path('/etc/passwd')
    with path.open() as f:
        for line in f.readlines():
            parts = line.rstrip().split(':')
            users[parts[0]] = {
                'password': None if parts[1] == 'x' else parts[1],
                'uid': int(parts[2]),
                'gid': int(parts[3]),
                'info': parts[4],
                'home': parts[5],
                'shell': parts[6],
            }
    return users
