import numpy as np
import matplotlib.pyplot as plt

def vertical_plot(x_values):
    # Given an array of x values, creates two graphs stacked vertically. the top graph is defined by h(x) = cos x and the bottom one is defined by k(x) = sin x.
    # Input: An array of x values to be plotted
    # Output: none
    fig, axes = plt.subplots(2, 1)
    h_of_x = np.cos(x_values)
    k_of_x = np.sin(x_values)

    top_plot = axes[0]
    bottom_plot = axes[1]
    
    top_plot.set_xlabel("x axis")
    top_plot.set_ylabel("y axis")
    top_plot.plot(x_values, h_of_x, color = 'blue')
    top_plot.title.set_text("Plot of h(x) = cos x")
    top_plot.grid()
    
    bottom_plot.set_xlabel("x axis")
    bottom_plot.set_ylabel("y axis")
    bottom_plot.plot(x_values, k_of_x, color = 'red')
    bottom_plot.title.set_text("Plot of k(x) = sin x")
    bottom_plot.grid()

    plt.tight_layout(pad=1.0) # the x axis label of the top graph was overlapping with the bottom graph, so I found this function on the internet to make my graph look cleaner.
    plt.show()

def side_by_side(x_values):
    # Given an array of x values, creates two graphs that are side-by-side. the top graph is defined by h(x) = cos x and the bottom one is defined by k(x) = sin x.
    # Input: An array of x values to be plotted
    # Output: none
    fig, axes = plt.subplots(1, 2)
    h_of_x = np.cos(x_values)
    k_of_x = np.sin(x_values)

    left_plot = axes[0]
    right_plot = axes[1]
    
    left_plot.set_xlabel("x axis")
    left_plot.set_ylabel("y axis")
    left_plot.plot(x_values, h_of_x, color = 'blue')
    left_plot.title.set_text("Plot of h(x) = cos x")
    left_plot.grid()
    
    right_plot.set_xlabel("x axis")
    right_plot.set_ylabel("y axis")
    right_plot.plot(x_values, k_of_x, color = 'red')
    right_plot.title.set_text("Plot of k(x) = sin x")
    right_plot.grid()

    plt.tight_layout(pad=1.0) # the x axis label of the top graph was overlapping with the bottom graph, so I found this function on the internet to make my graph look cleaner.
    plt.show()