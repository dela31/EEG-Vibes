def volume0(num):
    C1 = 70
    C2 = 80
    D2 = 86
    E2 = 90
    Half = 95
    A2 = 100
    F2 = 105
    G2 = 110
    H2 = 127

    if num < 0.10:
        vol = C1

    elif 0.20 > num >= 0.10:
        vol = C2

    elif 0.23 > num >= 0.20:
        vol = D2

    elif 0.26 > num >= 0.23:
        vol = E2

    elif 0.30 > num >= 0.26:
        vol = Half

    elif 0.37 > num >= 0.30:
        vol = A2

    elif 0.45 > num >= 0.37:
        vol = F2

    elif 0.6 > num >= 0.45:
        vol = G2

    elif num >= 0.60:
        vol = H2

    return vol
