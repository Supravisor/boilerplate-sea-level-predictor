import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]


    # Create scatter plot
    plt.scatter(x,y)

    # Create first line of best fit
    result = linregress(x, y)

    x_axis = pd.Series([i for i in range(1880,2051)])
    y_axis = x_axis * result.slope + result.intercept

    plt.plot(x_axis, y_axis)


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
