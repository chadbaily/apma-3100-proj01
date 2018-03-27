import math


def callSim(uVal, count):
    count = count + 1
    if count < 5:
        temp = uVal.pop()
        if temp > 0 and temp <= 0.2:
            return callSim(uVal, count)
        elif temp > 0.2 and temp <= 0.5:
            return callSim(uVal, count)
        else:
            return -math.log(1 - temp) / 12
            # return 12 * math.exp(-12 * temp)
    else:
        return 'Unanswered'


x = 1000
a = 7893
c = 3517
K = 2**13

uVal = []
count = 0
itterations = 2000
while count < itterations:

    x = (a * x + c) % K
    uVal.append(x / K)

    count = count + 1

responses = []

# for i in uVal:
#     print(i)

for n in range(0, 500):
    responses.append(callSim(uVal, 0))

for response in responses:
    print(response)
