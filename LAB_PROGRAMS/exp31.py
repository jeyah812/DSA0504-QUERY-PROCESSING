import numpy as np
import matplotlib.pyplot as plt

men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)

men_std = (4, 3, 4, 1, 5)
women_std = (3, 5, 2, 3, 3)

groups = ['Group1',
          'Group2',
          'Group3',
          'Group4',
          'Group5']

x = np.arange(len(groups))

plt.figure(figsize=(8,5))

plt.bar(x,
        men_means,
        yerr=men_std,
        label='Men',
        color='red')

plt.bar(x,
        women_means,
        bottom=men_means,
        yerr=women_std,
        label='Women',
        color='green')

plt.xlabel('Groups')
plt.ylabel('Scores')

plt.title('Scores by Group and Gender')

plt.xticks(x, groups)

plt.legend()

plt.show()
