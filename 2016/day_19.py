from collections import deque
from utils import read, print_answers

n = int(read(2016, 19))

Q = deque(range(1, n+1))
while len(Q) > 1:
    Q.rotate(-1)
    Q.popleft()
a1 = Q.pop()

# Slow
Q = deque(range(1, n+1))
while (lq := len(Q)) > 1:
    if lq % 10000 == 0:
        print(lq)
    offset = len(Q)//2
    Q.rotate(-offset)
    Q.popleft()
    Q.rotate(offset-1)
a2 = Q.pop()

print_answers(a1, a2, day=19)
# 1816277
# 1410967