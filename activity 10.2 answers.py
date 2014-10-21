__author__ = 'Alicia'

n = [2, 9, 23, 15, 15, 10, 1, 3, 3, 5]

print(n)

#print(n[0])
s =[]
i = 0
while i != len(n):
    if i != len(n)-1:
        if n[i] > n[i+1]:
            s.append(n[i+1])
            s.append(n[i])
            i += 2
        elif n[i] < n[i+1]:
            s.append(n[i])
            i += 1
        else:
            s.append(n[i])
            i += 1
    else:
        s.append(n[len(n)-1])
        i += 1
print(s)
