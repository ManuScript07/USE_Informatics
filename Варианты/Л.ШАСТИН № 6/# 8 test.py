from itertools import product


for ind, val in enumerate(product(sorted('АЕКНС'), repeat=6), start=1):
    if val == 'СЕНЕКА':
        print(ind)
