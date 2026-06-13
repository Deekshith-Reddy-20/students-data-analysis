n=input()
s=''
for ch in n:
    if ch.isalpha():
        s+=ch
    else:
        continue


print(s)