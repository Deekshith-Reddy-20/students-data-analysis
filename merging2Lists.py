a=[1,2,3,8]
b=[1,3,5,4,9]
i=j=0
merge=[]
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        merge.append(a[i])
        i+=1
    else:
        merge.append(b[j])
        j+=1
while i<len(a):
    merge.append(a[i])
    i+=1
while j<len(b):
    merge.append(b[j])
    j+=1
print(sorted(merge))