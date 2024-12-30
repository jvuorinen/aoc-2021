from utils import read, print_answers

a1 = a2 = 0
for line in read(2015, 5).split("\n"):
    t1 = sum(1 for x in line if x in "aeiou") >= 3
    t2 = any(True for a, b in zip(line[:-1], line[1:]) if a==b)
    t3 = not any(x in line for x in ["ab", "cd", "pq", "xy"])
    t4 = any(line[i:i+2] in f"{line[:i]}_{line[i+2:]}" for i in range(len(line)-1))
    t5 = any(True for a, b in zip(line[:-2], line[2:]) if a==b)

    a1 += t1 and t2 and t3
    a2 += t4 and t5

print_answers(a1, a2, day=5)
