from fnmatch import *

for x in range(0, 10**10, 11071):
    if fnmatch(str(x), '[13579]136*1'):
        s = str(x)
        if int(s[4:-1])%2==0:
            print(x, x//11071)
#7136931221 644651
#9136132401 825231
#9136353821 825251
#9136575241 825271
#9136796661 825291



