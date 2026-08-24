import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(200)

y = np.random.randn(200)

plt.figure(figsize=(8,5))

plt.scatter(x,
            y,
            color='red')

plt.xlabel('X')
plt.ylabel('Y')

plt.title('Scatter Plot of Random Distribution')

plt.show()
