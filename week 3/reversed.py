def reverse(s,a): # a is an empty string
    if type(s) == str:
        s = s.split()
    if len(s) == 0:
        return a
    else:
        a += str(s[-1]) + " "
        s.remove(s[-1])
        return reverse(s,a)
