__author__ = 'Alicia'
# Part 1 and 2
n = [2, 9, 23, 15, 15, 10, 1, 3, 3, 5]

for j in range(len(n)):
    for i in range(len(n)-1):
        temp = n[i]
        if temp > n[i+1]:
            n[i] = n[i+1]
            n[i+1] = temp
    print(n)

#Using the two for loops it will run till the entire list is in order.