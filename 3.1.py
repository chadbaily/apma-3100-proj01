

x = 1000
a = 7893
c = 3517
K = 2**13

uVal = []
count = 0
itterations = 53
while count < itterations:

    x = (a * x + c) % K
    uVal.append(x / K)

    count = count + 1

