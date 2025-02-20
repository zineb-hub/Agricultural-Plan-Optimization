import matplotlib.pyplot as plt
import numpy as np
import time

''' This class implements the search visualization and plots changes in data 
    while searching for the solution  '''

class DynamicPlot:
    def __init__(self, fig, num_products, products):
        self.num_products = num_products
        self.fig = fig
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel('Time (ms)')
        self.ax.set_ylabel('Value')
        self.ax.set_title('Dynamic Plot')
        self.x_data = []
        self.all_production_data = [[] for _ in range(num_products)]
        self.lines = [self.ax.plot([], [], label=products[i])[0] for i in range(num_products)]
        self.ax.legend()
        plt.ion()  # Turn on interactive mode
        self.fig.show()

    def add_data(self, x, production_values):
        self.x_data.append(x)
        for i in range(self.num_products):
            self.all_production_data[i].append(production_values[i])

    def update_plot(self):
        for i, line in enumerate(self.lines):
            line.set_data(self.x_data, self.all_production_data[i])
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.flush_events()