from utils import read, print_answers

raw = read(2015, 1)

diff = [(-1, 1)[c == "("] for c in raw]
pos = [p := 0] + [p := p + d for d in diff]
print_answers(pos[-1], pos.index(-1), day=1)
