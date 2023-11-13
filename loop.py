#!/usr/bin/env python

# Number to guess: How many passwords
# can we bcrypt in a second?
### To run, in terminal python loop.py 122
import bcrypt
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <NUMBER>")
    sys.exit(1)

password = 'a' * 100

def f(NUMBER):
    for _ in range(NUMBER):
        bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

f(int(sys.argv[1]))
