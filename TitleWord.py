n='hello WoRld'
s=''
new_word=True
for i in n:
    if i==" ":
        s+=i
        new_word=True
    else:
        if new_word:
            s+=i.upper()
            new_word=False
        else:
            s+=i.lower()
print(s)