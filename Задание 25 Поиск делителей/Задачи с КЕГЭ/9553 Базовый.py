for i in '39':
    for x in '02468':
        n = int(f'24{x}68{i}35')
        if n % 13 == 0:
            print(n, n//13)
for i in '39':
    for x in '02468':
        for y in '02468':
            n = int(f'24{x}{y}68{i}35')
            if n % 13 == 0:
                print(n, n//13)
##24268335 1866795
##24868935 1912995
##240068335 18466795
##240668935 18512995
##242668335 18666795
##248468935 19112995
