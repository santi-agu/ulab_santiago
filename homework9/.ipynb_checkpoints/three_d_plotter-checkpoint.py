import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def create_plot():
    # Creates a 3 dimensional graph of the equation z = e^(-x^2-y^2), along with color-coding its z values.
    # Inputs: None
    # Outputs: None
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    x = np.linspace(-2, 2, 101)
    y = np.linspace(-2, 2, 101)
    x, y = np.meshgrid(x, y) #turns x and y arrays into 2d arrays
    z = np.exp(-(x ** 2 + y ** 2))
    
    surface = ax.plot_surface(x, y, z, cmap = cm.viridis, label = 'Graph')

    fig.colorbar(surface, shrink= 0.5, aspect = 2) # shrink variable is height of the rectangular bar, aspect is aspect ratio

    ax.set_title("Graph of z = e^-(x^2+y^2)")
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    ax.set_zlabel("z axis")
    ax.zaxis.labelpad= - 16.9 #z axis label was originally under color bar, this line moves it

    plt.legend()
    plt.show()