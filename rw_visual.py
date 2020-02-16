import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    poin_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=5, c=poin_numbers, cmap=plt.cm.winter)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Emphasize the first and last points.
    ax.scatter(rw.x_values[0], rw.y_values[0], c='green', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break