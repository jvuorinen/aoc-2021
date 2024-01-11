from utils import print_answers

INPUT = 990941

a, b = 0, 1
recipes = [3, 7]

for _ in range(22_000_000):
    c, d = divmod(recipes[a] + recipes[b], 10)
    recipes += [c, d] if c >= 1 else [d]
    a = (a + recipes[a] + 1) % len(recipes)
    b = (b + recipes[b] + 1) % len(recipes)

a1 = "".join(map(str, recipes[INPUT : INPUT + 11]))
a2 = "".join(map(str, recipes)).index(str(INPUT))
print_answers(a1, a2, day=14)
