def double_char(s):
    '''Given a string, 
you have to return a string in which each character (case-sensitive) is repeated once.'''
    b = ''
    for i in s:
        b += i*2
    return b