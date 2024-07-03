from matplotlib import pyplot as plt
from random import choice

dice = lambda n: choice(range(1, n + 1))
N = 400  # how many times to roll the dice?
n = 6  # number of dice's faces

much = [0] * 11
plt.title('Dice Animator')
plt.xlabel('Result')
plt.ylabel('Frequency of Result')
plt.grid(axis='y', ls=':', color='k')
for _ in range(N):
    x = dice(n) + dice(n)
    much[x - 2] += 1
    plt.bar(range(2, n + n + 1), much, color='y')
    plt.pause(0.005)
plt.show()
