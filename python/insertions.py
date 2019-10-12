def do_insertions_simple(l, insertions):
    """Performs the insertions specified into l.
    @param l: list in which to do the insertions.  Is is not modified.
    @param insertions: list of pairs (i, x), indicating that x should
        be inserted at position i.
    """
    r = list(l)
    for i, x in insertions:
        r.insert(i, x)
    return r


def do_insertions_fast(l, insertions):
    """Implement here a faster version of do_insertions_simple """
    # YOUR CODE HERE
    p = list(l)
    r = list()
    j = 0
    k = 0
    s = 0

    if insertions[0][0] == 0:
        r.append(insertions[0][1])
        while k < len(insertions):
            for i in range(0, len(l)):
                if i < insertions[k][0]:
                    r.append(l[i])
                else:
                    while k <= i+1:
                        r.append(insertions[k][1])
                        k += 1




    # while j < len(l):
    #     print("J: "+str(j))
    #     print("S: "+str(s))
    #     if k < len(insertions) and j == insertions[k][0]:
    #         print("__")
    #         print(insertions[k][0])
    #         r.append(insertions[k][1])
    #         k += 1
    #     if k < len(insertions) and j+1 == insertions[k][0]:
    #         r.append(insertions[k][1])
    #         k += 1
    #     else:
    #         r.append(l[s])
    #         s += 1
    #     j += 1
    return r



    # for i in range(0, len(insertions)):
    #     print(i)
    #     print(insertions[i][0])
    #     print("_______")
    #     if i < len(insertions) and i == insertions[i][0]:
    #         r.append(insertions[i][1])
    #         print(insertions[i+1][0])
    #         if insertions[i+1][0] == i:
    #             r.append(insertions[i+1][1])
    #         else:
    #             r.append(l[i])
    # return r

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
insertions = [(0, 'a'), (2, 'z'), (2, 'b'), (7, 'c')]
r1 = do_insertions_simple(l, insertions)
r2 = do_insertions_fast(l, insertions)
print("r1:", r1)
print("r2:", r2)