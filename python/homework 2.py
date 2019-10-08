def do_insertions_fast(l, insertions):
    new_l = []
    used = 0
    for i, x in insertions:
        # Have already processed all insertions before the ith one,
        # and new_l is at least as long as the end of the previous insertion
        # new)l contains used elements of l, no more, no less
        # because the insertions are in order, I know that before im I already
        # have the correct result, that is, new_l[:i] is already the correct output

        # I also know that new_l is equal to a prefix of the result of the
        # simple iteration after processing the same insertions.
        len_new_l = len(new_l)
        if i < len_new_l:
            new_l.insert(i, x)
        else:
            d = i - len(new_l)
            new_l += l[used : used + d]
            new_l.append(x)
            used += d
        new_l += l[used:]
        return new_l

