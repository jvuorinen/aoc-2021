from collections import Counter
from string import ascii_lowercase as abc
from utils import read, print_answers


def is_legit(words, chk):
    cnt = Counter("".join(words))
    return chk == "".join(sorted(cnt, key=lambda x: (-cnt[x], ord(x)))[:5])


def decypher(word, r):
    return "".join(abc[(abc.index(c) + r) % len(abc)] for c in word)


a1 = 0
for line in read(2016, 4).split("\n"):
    tmp, chk = line[:-1].split("[")
    *words, rid = tmp.split("-")

    if is_legit(words, chk):
        a1 += int(rid)

    decrypted = " ".join(decypher(w, int(rid)) for w in words)
    if decrypted == "northpole object storage":
        a2 = rid


print_answers(a1, a2, day=4)  # 173787 548
