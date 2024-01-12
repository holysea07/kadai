import numpy as np
import matplotlib.pyplot as plt
 
x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y, s=600, c="Yellow", marker="*", alpha=0.5,
            linewidths=2, edgecolors="orange")
plt.xlabel("x dayo")
plt.ylabel("y dayo")
plt.show()
