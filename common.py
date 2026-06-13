a=[1,2,3,8,9,0]
b=[1,3,5,4,9]
common=[]
for i in a:
    if i in b:
        common.append(i)
print(common)