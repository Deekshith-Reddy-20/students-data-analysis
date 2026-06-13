from collections import Counter


def first_unique(s):
    count=Counter(s)
    for i in s:
        if count[i]==1:
            return i
    return None

s=input()
print(first_unique(s))