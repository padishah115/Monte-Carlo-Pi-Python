import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

trials = 10000

fig, ax = plt.subplots()
count = 0

for j in range(0, trials):
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)

    r = np.sqrt(x**2 + y**2)
        
    if r <= 1:
        count += 1
        plt.plot(x, y, 'bo')
    else:
        plt.plot(x,y, 'ro')



x_circle = np.linspace(0,1)
y_circle = np.sqrt(1-x_circle**2)
plt.plot(x_circle, y_circle, 'k-')
plt.xlim(0,1)
plt.ylim(0,1)
pi = 4*count/trials
plt.title(f"Estimate of pi is {pi}.")
plt.show()