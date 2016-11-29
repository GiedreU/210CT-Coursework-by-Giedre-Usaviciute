def remove(s):
    '''removes all vowels from a str recursively'''
    if s == '':
        return s
    elif s[0] not in ['a','e','i','u','o','A','E','I','U','O']:
        return s[0]+reMove(s[1:])
    else:
        return reMove(s[1:])

s = 'beautiful'
a = remove(s)
print(a)
