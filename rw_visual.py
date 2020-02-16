import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15, c=rw.y_values, cmap=plt.cm.winter)

plt.show()