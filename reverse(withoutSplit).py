
def rev_str(s):
    word=" "
    result=[]
    for char in s:
        if char!=" ":
            word+=char
        else:
            result.append(word)
            word=""
    result.append(word)
    return " ".join(result[::-1])
s=input()
print(rev_str(s))