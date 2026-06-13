n=int(input())
if n<=1:
    print("not")
else:
    for i in range(2,n):
        if n%i==0:
            print("not")
            break
    else:
        print('prm')