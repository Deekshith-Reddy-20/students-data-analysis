a=[1,2,4,11,2,3,5,4,0]
s=a[0]
d=a[0]
for i in a:
    if i>s:
       s=i

    if i<d:
        d=i

print(s)
print(d)