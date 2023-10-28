import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

trials = 10000
dt = 10
fig, ax = plt.subplots()

x_inside = []
y_inside = []

x_outside = []
y_outside = []

count = 0
total_trials = 0

def animate(i):
    global count, total_trials
    total_trials += 1

    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)

    r = np.sqrt(x**2 + y**2)
        
    if r <= 1:
        count += 1
        x_inside.append(x)
        y_inside.append(y)

    else:
        x_outside.append(x)
        y_outside.append(y)

    ax.clear()

    plt.scatter(x_inside, y_inside, c="b")
    plt.scatter(x_outside, y_outside, c="r")
    x_circle = np.linspace(0,1)
    y_circle = np.sqrt(1-x_circle**2)
    plt.plot(x_circle, y_circle, 'k-')

    plt.xlim(0,1)
    plt.ylim(0,1)
    pi = 4*count/total_trials

    plt.title(f"Estimate of pi is {pi:.5f}.")

    return 0,

anim = animation.FuncAnimation(fig, animate, frames = trials, interval = dt)



plt.show()