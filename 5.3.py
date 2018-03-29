import math
import numpy as np


def callSim(uVal, count, time):
    count = count + 1
    if count < 5:
        temp = uVal.pop()
        if temp > 0 and temp <= 0.2:
            return callSim(uVal, count, time + 4)
        elif temp > 0.2 and temp <= 0.5:
            return callSim(uVal, count, time + 26)
        else:
            callTime = (-math.log(1 - temp) * 12)
            while callTime > 25:
                temp = uVal.pop()
                callTime = (-math.log(1 - temp) * 12)
            return time + ((-math.log(1 - temp) * 12))
            # return 12 * math.exp(-12 * temp)
    else:
        return time


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
    responses.append(callSim(uVal, 0, 6))

responseNum = 0
for response in responses:
    responseNum = responseNum + 1
    print(responseNum, ": ", response)

responses.sort()

print("First Quantile: ", np.percentile(responses, 25))
print("Median: ", np.percentile(responses, 50))
print("Second Quantile: ", np.percentile(responses, 75))

for n in responses:
    if n <= 15:
        fifteen_count+= 1.0
    if n <= 20:
        twenty_count += 1.0
    if n <= 30:
        thirty_count += 1.0
    if n < 40:
        fourty_count += 1.0


print("P(W <= 15): "+ str(fifteen_count/500.0))
print("P(W <= 20): "+ str(twenty_count/500.0))
print("P(W <= 30): "+ str(thirty_count/500.0))
print("P(W <= 40): "+ str(fourty_count/500.0))
