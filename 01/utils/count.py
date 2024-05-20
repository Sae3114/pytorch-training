from .function import add

def count_word(s, c):
    ret = 0
    for i in range(len(s)):
        if s[i] == c:
            ret = add(ret, 1)
    
    return ret
