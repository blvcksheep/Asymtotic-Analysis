import math
import time
import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.15


def logi(n):
    return math.log(n)


def linearithmic(n):
    return n*(math.log(n))


def linear(n):
    return n


def quadratic(n):
    return n**2


def polynomial(n):
    return n**3


def exponential(n):
    return 2**n


listing = []
runTime = []
runTime2 = []
runTime3 = []
runTime4 = []
runTime5 = []
runTime6 = []

elem = int(input("Number of element: "))
for i in range(0, elem):
    num = int(input("Enter the number: "))
    listing.append(num)
    starTime = time.time()
    print(f'log{num} is {logi(num)}')
    starTimeTwo = time.time()
    print(f'{num}(log({num})) is {linearithmic(num)}')
    starTimeThree = time.time()
    print(linear(num))
    starTimeFour = time.time()
    print(f'{num}^2 is {quadratic(num)}')
    starTimeFive = time.time()
    print(f'{num}^3 is {polynomial(num)}')
    starTimeSix = time.time()
    print(f'2^{num} is {exponential(num)}')

    runTime.append(time.time() - starTime)
    runTime2.append(time.time() - starTimeTwo)
    runTime3.append(time.time() - starTimeThree)
    runTime4.append(time.time() - starTimeFour)
    runTime5.append(time.time() - starTimeFive)
    runTime6.append(time.time() - starTimeSix)

    bars1 = runTime
    bars2 = runTime2
    bars3 = runTime3
    bars4 = runTime4
    bars5 = runTime5
    bars6 = runTime6

    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]
    r5 = [x + barWidth for x in r4]
    r6 = [x + barWidth for x in r5]

    plt.bar(r1, bars1, color='darkgray', width=barWidth,
            edgecolor='white', label='logaritmic')
    plt.bar(r2, bars2, color='lightcoral', width=barWidth,
            edgecolor='white', label='linearithmic')
    plt.bar(r3, bars3, color='lightgreen', width=barWidth,
            edgecolor='white', label='linear')
    plt.bar(r4, bars4, color='peachpuff', width=barWidth,
            edgecolor='white', label='quadratic')
    plt.bar(r5, bars5, color='lightpink', width=barWidth,
            edgecolor='white', label='polynomial')
    plt.bar(r6, bars6, color='lightskyblue', width=barWidth,
            edgecolor='white', label='exponential')

    plt.xlabel('group', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))], listing)
    plt.legend()
    plt.show()

print('Numbers - {}'.format(listing))
print('Runtime of logirithmic - {}'.format(runTime))
print('Runtime of linearithmic - {}'.format(runTime2))
print('Runtime of linear - {}'.format(runTime3))
print('Runtime of quadratic - {}'.format(runTime4))
print('Runtime of polynomial - {}'.format(runTime5))
print('Runtime of exponential - {}'.format(runTime6))
