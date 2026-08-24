import numpy as np
import matplotlib.pyplot as plt

men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)

groups = ['G1', 'G2', 'G3', 'G4', 'G5']

x = np.arange(len(groups))
width = 0.35

plt.figure(figsize=(8,5))

plt.bar(x - width/2,
        men_means,
        width,
        label='Men',
        color='green')

plt.bar(x + width/2,
        women_means,
        width,
        label='Women',
        color='red')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by Person')

plt.xticks(x, groups)

plt.legend()

plt.show()
