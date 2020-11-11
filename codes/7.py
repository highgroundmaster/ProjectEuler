x = int(input())
i = 2
while i < x:
    y = 4
    flag = 0
    for j in range(2,int(y**(0.5) +1)):
        if y%j==0:
            y += 1
            flag = 1
            break
    if flag == 0:
        i += 1
        y += 1
print(y)
