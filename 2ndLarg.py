n=[21,2,3,4,6,7,88,77,65,8]
s=n[0]
sec=n[0]
third=n[0]
for i in n:
    if i>s:
        s=i
    elif i>sec and sec<s:
        sec=i
    elif i>third and third<sec:
        th=i
print(sec)
print(third)
print(sorted(n))