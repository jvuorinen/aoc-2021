from itertools import combinations, permutations
from functools import reduce
from collections import Counter, defaultdict
from math import prod
import numpy as np
import re
import networkx as nx
from utils import read, print_answers

raw = read().split("\n")
# raw = read(2017, 19).split("\n")


a1 = None
a2 = None
print_answers(a1, a2, day=19)
