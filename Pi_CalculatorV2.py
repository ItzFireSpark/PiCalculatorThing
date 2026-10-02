import random as rand
inSqr = 0
inCir = 0
piEstimate = 0
c = int(input("Enter the radius of circle:\n"))
d = int(input("Enter the amount of points to plot:\n")) 

def plot(a , b):
    linSqr = 0
    linCir = 0
    for _ in range(b):
        x = rand.randint(-a, a)
        y = rand.randint(-a, a)
    
        if ((x ** 2) + (y ** 2)) <= (a ** 2):
            linCir += 1
        linSqr += 1
    return linSqr, linCir

inSqr, inCir = plot(c , d)
print("In circle was", inCir)
print("Total was", inSqr)
piEstimate = (inCir / inSqr) * 4
print("Estimated value of pi is ", piEstimate)
