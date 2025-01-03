from utils import read, print_answers

raw = read(2015, 8)

a1 = a2 = 0
for word in raw.split("\n"):
    cc = word[1:-1].replace(r"\\", "_").replace(r"\"", "_")
    a1 += len(word) - (len(cc) - 3 * cc.count("\\x"))
    a2 += 2 + word.count("\\") + word.count("\"") 

print_answers(a1, a2, day=8)