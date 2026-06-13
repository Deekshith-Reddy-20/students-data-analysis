n=[21,2,3,4,6,7,88,77,65,8]
l=len(n)
for i in range(l):
    for j in range(0,l-i-1):
        if n[j] > n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)