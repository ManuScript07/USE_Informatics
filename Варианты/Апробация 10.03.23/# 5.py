for n in range(1, 9):
    R = bin(n)[2:]
    if n % 2 == 0:
        R = '10' + R
    else:
        R = '1' + R + '01'
    print(int(R, 2))
        

# 63
