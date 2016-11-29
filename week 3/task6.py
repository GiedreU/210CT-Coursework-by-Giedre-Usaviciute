def reverse(s,a): # a is an empty string
    '''reverses words in a sentece s by dividing the sentence and recursively adding last word into new string 
    and removing the last word from s sentence'''
    if type(s) == str:
        s = s.split()
    if len(s) == 0:
        return a
    else:
        a += str(s[-1]) + " "
        s.remove(s[-1])
        return reverse(s,a)
