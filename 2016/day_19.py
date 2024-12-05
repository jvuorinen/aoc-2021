from collections import deque
from utils import read, print_answers

n = int(read(2016, 19))

# Part 1
Q = deque(range(1, n + 1))
while len(Q) > 1:
    Q.rotate(-1)
    Q.popleft()
a1 = Q.pop()

# Part 2
L = deque(range(1, n // 2 + 2))
R = deque(range(n // 2 + 2, n + 1)[::-1])
while len(R) > 0:
    if len(L) == len(R):
        L.append(R.pop())
    L.pop()
    R.appendleft(L.popleft())
    L.append(R.pop())
a2 = L.pop()

print_answers(a1, a2, day=19)
