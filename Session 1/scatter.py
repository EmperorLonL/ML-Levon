import matplotlib.pyplot as plt
import random

random.seed(42)
x = [random.random()*100 for _ in range(150)]
y = [random.random()*100 for _ in range(150)]
colors = [random.random() for _ in range(150)]
sizes = [random.random() for _ in range(150)]
plt.scatter(x, y, c = colors, s = sizes, marker = 'o')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.grid(True)
plt.show()

