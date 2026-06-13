
n=int(input())
s=[]
p=1
for i in range(1,n):
        s.append(i)
        p=(p*i)%n
if p!=1:
    s.remove(p)
print(len(s))