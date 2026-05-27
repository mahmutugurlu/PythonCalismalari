i = 10
z = 100
while i > 0:
    if i % 2 == 0:
        z = z - i
        i = i - 1
        #print(z)
    else:
        z = z + i
        i = i - 1
print(z) #95