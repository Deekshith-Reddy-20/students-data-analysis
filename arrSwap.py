n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(arr)
s=0
even=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        s+=even
print(s)