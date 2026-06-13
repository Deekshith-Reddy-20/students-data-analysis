n="Stra@12345"
l=n.lower()
count=0
cnt=0
spe=0
for i in l:
    if i.isalpha():
        count+=1
    elif i.isdigit():
        cnt+=1
    else:
        spe+=1
print(f"str:{count}\nnum:{cnt}\nspe:{spe}")
