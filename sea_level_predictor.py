import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    print(df.head())
    print(df.dtypes)
    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], color='blue', s=15, label='Original Data')
    
    
    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([year for year in range(1880, 2050+1)])

    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, 'r', label="Best Fit Line (All Data)")
    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]

    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_rec = pd.Series([year for year in range(2000, 2050+1)])
    y_pred_rec = res_recent.slope * x_pred_rec + res_recent.intercept

    plt.plot(x_pred_rec, y_pred_rec, 'green', label="Best Fit Line(Year>=2000)")
    # Add labels and title

    
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
