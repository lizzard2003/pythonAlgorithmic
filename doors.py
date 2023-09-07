doors= [False] *101
print(doors)
for i in range(1,101): # we start at 1 and not position 0
    doors[i] = not doors[i]
print("---", doors)

for i in range(1,101):
    for j in range(i,101,i): # this is the using the outter loop counter (i) and the second (i) as the step value
       doors[j] = not doors[j]

for i in range(1,101): # these are the open doors at the end of the process 
    if doors[i] is True:
        print (i, end= " ,")