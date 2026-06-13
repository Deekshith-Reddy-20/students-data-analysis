a=[1,2,4,11,2,3,5,4,0]
s=[]
for i in a:
    if i not in s:
        s.append(i)
print(s)