from utils import read, print_answers
import json

def count(doc, no_reds=False):
    if isinstance(doc, dict):
        if no_reds and "red" in doc.values():
            return 0
        return sum(count(v, no_reds) for v in doc.values())
    if isinstance(doc, list):
        return sum(count(x, no_reds) for x in doc)
    return doc if isinstance(doc, int) else 0

doc = json.loads(read(2015, 12))

a1 = count(doc)
a2 = count(doc, no_reds=True)
print_answers(a1, a2, day=12)
