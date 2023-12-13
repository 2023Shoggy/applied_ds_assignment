import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import stats
from scipy.stats import skew, kurtosis
import seaborn as sns


# define function which takes a filename as argument, reads a dataframe in World-
# bank format and returns two dataframes: one with years as columns and one with
# countries as columns.

def read_worldbank_data(filename):
    # Read Data from File
    df = pd.read_csv(filename)

    # Extract Columns
    df = df[['Series Name', 'Country Name', 'Country Code',
             '1990 [YR1990]', '2000 [YR2000]', '2013 [YR2013]', '2014 [YR2014]']]

    # Dataframe for Years as Columns
    df_years = df.melt(id_vars=['Series Name', 'Country Name',
                       'Country Code'], var_name='Year', value_name='Value')

    # Dataframe for Country as Columns
    df_count = df_years.pivot_table(
        index=['Series Name', 'Year'], columns='Country Name', values='Value').reset_index()

    # Cleaned Transposed Dataframes
    df_years['Year'] = df_years['Year'].str.extract(r'(\d+)')
    df_years['Year'] = pd.to_numeric(df_years['Year'])
    df_count.columns.name = None

    return df_years, df_count


filename = r'C:\Users\Owner\Downloads\Gab_dataset\ADS_assignment2_Data.csv'
df_years, df_count = read_worldbank_data(filename)

print(df_years.head(44))
print(df_count.head(44))


# statistical properties of a few indicators, that are of interest, and
# cross-compare between individual countries and produce appropriate summary statistics.


# series of interest
series_of_inter = ['Electric power consumption (kWh per capita)',
                   'Electricity production from renewable sources, excluding hydroelectric (kWh)', 'Population, total']

# Filtered Data for series
df_selected = df_years[df_years['Series Name'].isin(series_of_inter)]

# Exploring statistics for individual countries
individual_count = df_selected.groupby(['Series Name', 'Country Name'])[
    'Value'].describe()

# use region data provided for countries in the dataset
region_data = df_years[['Country Name', 'Country Code']].drop_duplicates()
selected_regions = pd.merge(df_selected, region_data, on='Country Name')

# Display Head for Years Column
print(df_years.columns)

# Display Head for countries Column
print(df_count.columns)


# use aggregated data for regions and other categories by
# using describe() method to explore the data

# Statistics for Regions
summary_regions = selected_regions.groupby(
    ['Series Name', 'Country Name'])['Value'].describe()

# Display Results
print("Summary Statistics for Individual Countries:")
print(individual_count)

print("\nSummary Statistics for Regions:")
print(summary_regions)


# other statistical methods to explore

# Summary Statistics for Individual Countries
individual_count = df_selected.groupby(['Series Name', 'Country Name'])['Value'].agg(
    ['count', 'mean', 'std', 'min', lambda x: x.quantile(0.25), 'median', lambda x: x.quantile(0.75), 'max'])

# Summary Statistics for Regions
summary_regions = selected_regions.groupby(['Series Name', 'Country Name'])['Value'].agg(
    ['count', 'mean', 'std', 'min', lambda x: x.quantile(0.25), 'median', lambda x: x.quantile(0.75), 'max'])

# Rename the functions for better readability
individual_count.columns = ['count', 'mean',
                            'std', 'min', '25%', 'median', '75%', 'max']
summary_regions.columns = ['count', 'mean',
                           'std', 'min', '25%', 'median', '75%', 'max']

# Display Results
print("Summary Statistics for Individual Countries:")
print(individual_count)

print("\nSummary Statistics for Regions:")
print(summary_regions)


# Explore and understand any correlations (or lack of) between indicators


# Relevant series
series_of_inter = ['Electric power consumption (kWh per capita)',
                   'Electricity production from renewable sources, excluding hydroelectric (kWh)', 'Population, total']

# Filter selected series
df_selected = df_years[df_years['Series Name'].isin(series_of_inter)]

# Correlation Matrix for series
correlation_matrix = df_selected.pivot_table(
    index='Country Name', columns='Series Name', values='Value').corr()

# Visualizing Correlations using heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap between Selected Series')
plt.show()

# Correlation Over Time
correlation_over_time = df_selected.pivot_table(
    index='Year', columns='Series Name', values='Value').corr()

# Heatmap Correlations Over Time
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_over_time, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap Correlation Over Time')
plt.show()

# Selected Relevant series
series_of_inter = ['Electric power consumption (kWh per capita)',
                   'Electricity production from renewable sources, excluding hydroelectric (kWh)']

# Filter Data for Selected Indicators
df_selected = df_years[df_years['Series Name'].isin(series_of_inter)]

# Creating Line Plot for Electric Power Consumption Over Time for Countries
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Value', hue='Country Name',
             data=df_selected[df_selected['Series Name'] == 'Electric power consumption (kWh per capita)'])
plt.title('Electric Power Consumption (kWh per capita) Over Time')
plt.xlabel('Year')
plt.ylabel('Electric Power Consumption (kWh per capita)')
plt.legend(title='Country')
plt.show()

# Creating Line plot for Electricity Production from Renewable sources Over Time for Countries
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Value', hue='Country Name',
             data=df_selected[df_selected['Series Name'] == 'Electricity production from renewable sources, excluding hydroelectric (kWh)'])
plt.title('Electricity Production from Renewable Sources Over Time')
plt.xlabel('Year')
plt.ylabel('Electricity Production (kWh)')
plt.legend(title='Country')
plt.show()

# Selected Relevant Indicators
indicators_of_interest = [
    'Electric power consumption (kWh per capita)', 'Electricity production from renewable sources, excluding hydroelectric (kWh)']

# Filter Data for Selected Indicators
df_selected = df_years[df_years['Series Name'].isin(indicators_of_interest)]

# Creating Bar Chart for Electric Power Consumption Over Time for few Countries
plt.figure(figsize=(12, 8))
sns.barplot(x='Year', y='Value', hue='Country Name',
            data=df_selected[df_selected['Series Name'] == 'Electric power consumption (kWh per capita)'])
plt.title('Electric Power Consumption (kWh per capita) Over Time')
plt.xlabel('Year')
plt.ylabel('Electric Power Consumption (kWh per capita)')
plt.legend(title='Country')
plt.show()


# Years of interest
years_of_interest = [1990, 2000, 2013, 2014]

# Creating Pie charts for Electricity Production from Renewable sources for each year
for year in years_of_interest:
    data_for_selected_year = df_selected[(
        df_selected['Series Name'] == 'Electricity production from renewable sources, excluding hydroelectric (kWh)') & (df_selected['Year'] == year)]

    plt.figure(figsize=(12, 8))
    plt.pie(data_for_selected_year['Value'],
            labels=data_for_selected_year['Country Name'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Electricity Production from Renewable Sources in {year}')
    plt.show()
