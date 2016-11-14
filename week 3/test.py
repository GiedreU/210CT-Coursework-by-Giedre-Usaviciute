def reMove(s):
    if s == '':
        return s
    elif s[0] not in ['a','e','i','u','o','A','E','I','U','O']:
        return s[0]+reMove(s[1:])
    else:
        return reMove(s[1:])

s = 'oooooo'
a = reMove(s)
print(a)
