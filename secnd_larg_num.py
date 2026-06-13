def second_number(s):
        p=sorted(s)
        print(set(p))
        return p[-2]
s=input()
print(second_number(s))
