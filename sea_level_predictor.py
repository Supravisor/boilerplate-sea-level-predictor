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
    df_2000 = df.loc[df['Year'] >= 2000]

    prediction_x = df_2000['Year']
    prediction_y = df_2000['CSIRO Adjusted Sea Level']
    prediction_result = linregress(prediction_x, predictions_y)

    x_axis_prediction = pd.Series([i for i in range(2000,2051)])
    y_axis_prediction = x_axis_prediction * prediction_result.slope + prediction_result.intercept

    plt.plot(x_axis_prediction, y_axis_prediction)


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
