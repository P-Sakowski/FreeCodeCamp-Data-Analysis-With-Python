import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df_year = df['Year']
    df_level = df['CSIRO Adjusted Sea Level']
    plt.scatter(df_year, df_level)

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(df_year, df_level)

    x1 = np.arange(df['Year'].min(), 2051, 1)
    y1 = intercept + slope * x1

    plt.plot(x1, y1)

    # Create second line of best fit

    df2 = df[df['Year'] >= 2000]
    df_year2 = df2['Year']
    df_level2 = df2['CSIRO Adjusted Sea Level']
  
    slope2, intercept2, r2, p2, se2 = linregress(df_year2, df_level2)

    x2 = np.arange(df_year2.min(), 2051, 1)
    y2 = intercept2 + slope2 * x2
  
    plt.plot(x2, y2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
  