from itertools import combinations, permutations, count, cycle
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
import re
import networkx as nx
from utils import read, print_answers

raw = read().split("\n")
# raw = read(2024, None).split("\n")


a1 = None
a2 = None

print_answers(a1, a2, day=99)
