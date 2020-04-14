def ExtendEuclid(a,m) : 
    y0 = 0
    y1 = 1
    while(a > 0) :
        r = m % a
        if(r == 0):
            break 
        q = m//a
        y = y0 -y1 * q
        m = a
        a = r
        y0 = y1
        y1 = y
    if(a > 1):
        return null
    else:
        return y

print(ExtendEuclid(31,3480))