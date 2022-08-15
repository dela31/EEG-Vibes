def note0(num):
    C1 = 55
    C2 = 60
    D2 = 62
    E2 = 64
    Half = 65
    A2 = 67
    F2 = 69
    G2 = 71
    H2 = 72

    if num < 0.1:
        note = C1

    elif 0.15 > num >= 0.1:
        note = D2

    elif 0.25 > num >= 0.15:
        note = C2

    elif 0.3 > num >= 0.25:
        note = E2

    elif 0.35 > num >= 0.3:
        note = Half

    elif 0.4 > num >= 0.35:
        note = A2

    elif 0.45 > num >= 0.4:
        note = F2

    elif 0.5 > num >= 0.45:
        note = G2

    elif 0.6 > num >= 0.5:
        note = Half

    elif num >= 0.6:
        note = H2

    return note
