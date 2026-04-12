import random as rand
inSqr = 0
inCir = 0
repeatN = 0
piEstimate = 0
repeatNtimes = 800000000 #how many times do you want to repeat this for
repeatProgress = 0
while repeatN < repeatNtimes:
    while repeatProgress < 1000000: #how often should it update you on its progress
        x = rand.randint(-10000, 10000)
        y = rand.randint(-10000, 10000)
    
        if (x ** 2) + (y ** 2) <= 100000000:
            inCir = inCir + 1
        inSqr = inSqr + 1
        repeatN += 1
        repeatProgress += 1
    print("Remaining",repeatNtimes - repeatN )
    repeatProgress = 0
print("In circle was", inCir)
print("In square was", inSqr)
piEstimate = (inCir / inSqr) * 4
print("Estimated value of pi is ", piEstimate)
