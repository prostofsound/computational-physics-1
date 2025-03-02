import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.01)
plt.plot(x, np.sin(x))
plt.title("My first plot using the terminal")

plt.show()
