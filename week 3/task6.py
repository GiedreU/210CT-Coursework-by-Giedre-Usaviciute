def reverse(s,a): # a is an empty string
    '''reverses words in a sentece s by dividing the sentence and recursively adding last word into new string 
    and removing the last word from s sentence'''
    if type(s) == str:                                   #(1)
        s = s.split()                                    #(n)
    if len(s) == 0:                                      #(1)
        return a                                         #(1)
    else:
        a += str(s[-1]) + " "                            #(1)
        s.remove(s[-1])                                  #(1)
        return reverse(s,a)                              #(1)
    
'''BigO notation for this function is O(n) because split funcion itertaively goes through the whole sentence
and whole function is called recursevily n times.'''
