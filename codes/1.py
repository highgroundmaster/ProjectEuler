x = open("../inputs/1.txt", 'r').read().split('\n')
for num in x[:-1]:
    sum = 0
    for i in range(int(num)):
        if i%3==0 or i%5==0:
            sum += i
    print(sum)

