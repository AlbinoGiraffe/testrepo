def lhf(a, n=100):
    l = [a]
    bigl = l * n
    bigl[0].append('hello')
    return bigl


# bigl merely contains pointers to l, appending hello,
# modifies all the pointers because it is just pointing to l
# bigl = [@, @, @, @, @]
# @ --> ['hi']
