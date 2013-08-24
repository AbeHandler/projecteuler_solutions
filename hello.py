def fiveDigitPals():
    L = list()
    for x in range(1,10):
        for y in range(1,10):
            for z in range(1,10):
                L.append(str(x)+str(y)+str(z)+str(y)+str(x))
    return L


