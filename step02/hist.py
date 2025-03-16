import os
import numpy as np
import matplotlib.pyplot as plt

path = os.path.join(os.path.dirname(__file__), 'height.txt')
xs = np.loadtxt(path)
print(xs.shape)

plt.hist(xs, bins='auto', density=True)
plt.xlabel('Height(cm)')
plt.ylabel('Probability Density')
plt.savefig('hist.png')

mu = np.mean(xs)
sigma = np.std(xs)

print(f'mu: {mu:.2f}, sigma: {sigma:.2f}')