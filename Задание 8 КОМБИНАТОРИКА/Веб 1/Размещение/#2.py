from itertools import product
k = 0
for x in product('КАНТ', repeat=6):
    if x.count('К') == 2:
        k += 1
print(k)