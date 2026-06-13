def rev_str(s):
    word=s.split()
    rev_wrd=word[::-1]
    return" ".join(rev_wrd)
s=input()
print(rev_str(s))
