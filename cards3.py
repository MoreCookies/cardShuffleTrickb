#cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
cards = [x for x in range(13)]
scards = cards[:3]


def check(ary):
    clone = ary[:]
    prev = None
    while len(clone) > 0:
        if prev is not None and (prev + 1) != clone[0]:
            return False
        prev = clone[0]
        del(clone[0])
        if len(clone) > 0:
            clone.append(clone[0])
            del(clone[0])
    return True

def findCombs(arr):
    for a in range(len(arr)):
        sl0 = removeItem(arr, a)
        #print(sl0)
        for b in range(len(sl0)):
            sl1 = removeItem(sl0, b)

            for c in range(len(sl1)):
                sl2 = removeItem(sl1, c)

                for d in range(len(sl2)):
                    sl3 = removeItem(sl2, d)

                    for e in range(len(sl3)):
                        sl4 = removeItem(sl3, e)

                        for f in range(len(sl4)):
                            sl5 = removeItem(sl4, f)

                            for g in range(len(sl5)):
                                sl6 = removeItem(sl5, g)

                                for h in range(len(sl6)):
                                    sl7 = removeItem(sl6, h)

                                    for i in range(len(sl7)):
                                        sl8 = removeItem(sl7, i)

                                        for j in range(len(sl8)):
                                            sl9 = removeItem(sl8, j)

                                            for k in range(len(sl9)):
                                                sl10 = removeItem(sl9, k)

                                                for l in range(len(sl10)):
                                                    sl11 = removeItem(sl10, l)

                                                    candidate = [arr[a], sl0[b], sl1[c], sl2[d], sl3[e], sl4[f], sl5[g], sl6[h], sl7[i], sl8[j], sl9[k], sl10[l], sl11[0] ]
                                                    if check(candidate):
                                                        print("good")
                                                        return candidate
                

def removeItem(aList, i):
    return aList[:i] + aList[i+1:]


print(findCombs(cards))