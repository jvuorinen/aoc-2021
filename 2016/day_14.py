import re
from collections import Counter, defaultdict
from functools import cache, reduce
from itertools import combinations, count, cycle, permutations
from math import prod

import networkx as nx
import numpy as np

from utils import print_answers, read

from utils import print_answers, read

raw = read().split("\n")
# raw = read(2016, 14).split("\n")


a1 = None
a2 = None

print_answers(a1, a2, day=14)
