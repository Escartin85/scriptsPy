
# Example login code
from crypt import crypt
import sqlite3

# Bard security, store safely
salt = '$6$ZmBkxkRFj03LQOvr'
db = sqlite3.connect('passwords.db')
# Access columns by names
db.row_factory = sqlite3.Row

# Get user passwor form db
def user_passwd(user):
    cur = db.cursor()
    cur.execute('SELECT passwd FROM users WHERE user = ?', (users, ))
    row = cur.fetchone()
    # No such user
    if row is None:
        raise KeyError(user)
    return row['passwd']

# Encrypt user password
def encrypt_passwd(passwd):
    return crypt(passwd, salt)

# Return True is user/password pair matches
def login(user, password):
    try:
        db_passwd = user_passwd(user)
    except KeyError:
        return False

    passwd = encrypt_passwd(password)
    return passwd == db_passwd

# -----------------
from random import random

# Generate tests cases
def gen_cases(number):
    for i in range(number):
        # 90% of logins are OK
        if random() > 0.1:
            yield ('daffy', 'rabbit season')
        else:
            # No such user
            if random() < 0.2:
                yield ('tweety', 'puddy tat')
            else:
                yield ('daffy', 'rabbit season')

# Benchmark login with test cases
def bench_login(cases):
    for user, passwd in cases:
        login(user, passwd)


if __name__ == '__main__':
    num = 1000
    cases = list(gen_cases(num))

    if 0:
        bench_login(cases)

    if 0:
        import cProfile
        cProfile.run('bench_login(cases)')
