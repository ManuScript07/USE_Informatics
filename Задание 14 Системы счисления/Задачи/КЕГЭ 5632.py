for x in range(0, 21):
    for y in range(1, 21, 2):
        n1 = 3*21**4 + 2*21**3 + y*21**2 + x*21 + 10
        n2 = 1*21**4 + 6*21**3 + y*21**2 + 1*21 + 8
        if (n1+n2) % 12 != 0:
            break
    else:
        n1 = 3*21**4 + 2*21**3 + 7*21**2 + x*21 + 10
        n2 = 1*21**4 + 6*21**3 + 7*21**2 + 1*21 + 8
        print((n1+n2)/12)
        break

# 71524
