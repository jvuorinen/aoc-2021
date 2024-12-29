from hashlib import md5
from utils import read, print_answers

SECRET = read(2015, 4)

def hash(i):
    return md5(f"{SECRET}{i}".encode()).hexdigest()

def solve(zs):
    return next(i for i in range(int(1E12)) if hash(i)[:zs] == "0" * zs)

print_answers(solve(5), solve(6), day=4)
