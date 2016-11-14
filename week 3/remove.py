def removeFunc(s,k,newString):
    print(k)
    if len(s)==k:
        return k
    else:
        if s[k] not in ['a','e','i','u','o','A','E','I','U','O']:
            newString += s[k]
        removeFunc(s,k+1,newString)
        
s = 'beautiful'
a = removeFunc(s, 0, '')

