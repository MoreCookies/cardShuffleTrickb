#cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
cards = [x for x in range(13)]
scards = cards[:3]

#Slow find combination. Brute force search for every single combination. ~6 billion.
#Also takes a few minutes to find the correct combination.
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


def removeItem(aList, i):
    return aList[:i] + aList[i+1:]


#print(findCombs(cards))

# ?  ?   ?  ?   ?   ?  ?  ?   ?   ?  ?  ?   ? 
# 1, x1, 2, x2, 3, x3, 4, x4, 5, x5, 6, x6, 7
#   x6     x1     x2     x3     x4     x5
#   x6     8      x2     9       x4    10
#   x6            11            x4   
#   12                          x4
#                               13
def find(n):
    cards = [i for i in range(n)]
    solution = [None] * n
    unknownIndexes = [j for j in range(n)]
    tail = []
    pushToBack = False
    while len(cards) > 0:
        for i in unknownIndexes:
            if solution[i] is None:
                if not pushToBack:
                    solution[i] = cards[0]
                    del(cards[0])
                    pushToBack = True
                else:
                    tail.append(i)
                    pushToBack = False
        unknownIndexes = tail
        tail = []
    return solution

print(find(1200))