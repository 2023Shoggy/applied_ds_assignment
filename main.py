# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

"""
Data source: https://www.kaggle.com/datasets/asaniczka/median-and-avg-hourly-wages-in-the-usa-1973-2022
"""
# Read the CSV file into a pandas DataFrame
df = pd.read_csv('median_average_wages.csv')


def draw_bar_chart():
    """ Draw bar chart distribution for different working groups """

    # Extract the required columns
    columns_to_plot = ['men_average', 'women_average',
                       'white_average', 'black_average', 'hispanic_average']

    # Create a bar chart
    plt.figure(figsize=(14, 7))

    for column in columns_to_plot:
        plt.bar(df['year'], df[column], label=column, alpha=0.7)

    # Add labels and legend
    plt.xlabel('Year')
    plt.ylabel('Average Income')
    plt.title('Average Income from 1973 to 2022')
    plt.legend(loc='upper left')

    # Show the chart
    plt.grid(True)
    return plt.show()


def draw_pie_chart():
    """
      Draw pie Chart for average salaries in 1973 and 2022
    """

    # Extract the required columns for 1973
    values_1973 = [
        df.iloc[0, 2],  # Men Average
        df.iloc[0, 4],  # Women Average
        df.iloc[0, 8],  # White Average
        df.iloc[0, 10],  # Black Average
        df.iloc[0, 12],  # Hispanic Average
    ]

    # Extract the required columns for 2022
    values_2022 = [
        df.iloc[3, 2],  # Men Average
        df.iloc[3, 4],  # Women Average
        df.iloc[3, 8],  # White Average
        df.iloc[3, 10],  # Black Average
        df.iloc[3, 12],  # Hispanic Average
    ]

    # Labels for the categories
    labels = ['Men Average', 'Women Average', 'White Average', 'Black Average', 'Hispanic Average']

    # Create two pie charts (for 1973 and 2022)
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # Plot the pie chart for 1973
    axes[0].pie(values_1973, labels=labels, autopct='%1.1f%%', startangle=140)
    axes[0].set_title('Year 1973')

    # Plot the pie chart for 2022
    axes[1].pie(values_2022, labels=labels, autopct='%1.1f%%', startangle=140)
    axes[1].set_title('Year 2022')

    # Create a single legend for both charts
    fig.legend(labels, loc='upper right')

    # Add chart title
    fig.suptitle('Pie Chart for average salaries in 1973 and 2022')

    # Show the pie charts
    return plt.show()


def draw_line_chart():
    """
      Draw average Income from 1973 to 2022
    """

    # Extract the required columns
    columns_to_plot = ['men_average', 'women_average', 'white_average', 'black_average', 'hispanic_average']

    # Create a line chart
    plt.figure(figsize=(14, 7))

    for column in columns_to_plot:
        plt.plot(df['year'], df[column], label=column)

    # Add labels and legend
    plt.xlabel('Year')
    plt.ylabel('Average Income')
    plt.title('Average Income Over the Years')
    plt.legend(loc='upper right')

    # Show the chart
    plt.grid(True)
    return plt.show()


if _name_ == "_main_":
    # Call the functions to draw line, pie and bar charts
    draw_line_chart()
    draw_pie_chart()
    draw_bar_chart()
