

x = 1000
a = 7893
c = 3517
K = 2**13

uVal = []
count = 0
itterations = 10000
while count < itterations:

    x = (a * x + c) % K
    uVal.append(x / K)

    count = count + 1

sum = 0
u = 7
output = 0
for i in uVal:
    sum = sum + i
    if sum >= u:
        output = uVal.index(i)
        break

print(output)
