n=input()
s={}
for i in n:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
print(s)
for i in n:
    if s[i] == 1:
        print(i,"First non-repeating character" ,end=",")
        break

else:
    print("No non-repeating character found")

