import matplotlib.pyplot as plt
import numpy as np

def display_plot(km, price, theta0, theta1):
    fig = plt.gcf()
    fig.canvas.set_window_title('Results of training')

    plt.xlabel("km")
    plt.ylabel("price")

    x = np.linspace(8000, 250000, 10)
    y = theta1*x + theta0
    plt.plot(x, y, '-r')
    plt.scatter(km, price)
    plt.show()