a='aaaba'
b=len(a)
c=len(a)//2
valid=True
for i in range(int(b)):
    left=a[i]
    right=a[(b-1-i)]
    print(left, right)
    if left!=right:
        valid=False

        break
if valid:
    print("yes")
else:
    print("no")
