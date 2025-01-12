import numpy as np
from utils import read, print_answers

THRS = int(read(2015, 20))
SIZE = 1_000_000

arr1, arr2 = np.zeros(SIZE, int), np.zeros(SIZE, int)
for i in range(1, SIZE):
    idx = np.arange(i, SIZE, i)
    arr1[idx] += i*10
    arr2[idx[:50]] += i*11

a1, a2 = [np.argmax(a > THRS) for a in (arr1, arr2)]
print_answers(a1, a2, day=20)
