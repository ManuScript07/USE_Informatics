for x in range(0, 10**6, 51):
    s = str(x)
    if s.startswith('56') and '98' in s:
        print(x, x//51)
##560898 10998
##562989 11039
##565998 11098
##567987 11137
##569823 11173
##569874 11174
