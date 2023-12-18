import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

url = 'https://raw.githubusercontent.com/boi-andy/final_project/main/data/planets_data.csv'
planets_df = pd.read_csv(url)

# Streamlit app
st.title('Star Wars Planets Data Exploration')

st.text('My analysis and explanation for each of these visuals can be found on my blog post:') 
st.markdown('[EDA for Star Wars Planets and People](https://boi-andy.github.io/my-blog/2023/11/14/EDA.html)')


# Plot 1: Scatter plot with circles for each planet based on diameter
st.header('Planet Diameter Comparison')

# Add a slider for selecting the minimum diameter size
min_diameter_size = st.slider('Select Minimum Diameter Size (km):', min_value=0, max_value=30000, value=5000)

# Set up the plot
fig_scatter, ax_scatter = plt.subplots(figsize=(10, 6))

# Plot circles for each planet based on diameter
for index, planet in planets_df.iterrows():
    if planet['diameter'] >= min_diameter_size:
        ax_scatter.scatter(
            x=index,
            y=planet['diameter'],
            s=planet['diameter'] / 20,
            alpha=0.5,
            label=planet['name']
        )

# Set axis labels and title
ax_scatter.set_title('Planet Diameter Comparison')
ax_scatter.set_xlabel('Planet Name')
ax_scatter.set_ylabel('Diameter (km)')

# Set x-axis ticks and labels
ax_scatter.set_xticks(range(len(planets_df)))
ax_scatter.set_xticklabels(planets_df['name'], rotation=45, ha='right')

# Set the y-axis limit dynamically
ax_scatter.set_ylim(0, planets_df['diameter'].max() + 15000)

# Display the plot in Streamlit app
st.pyplot(fig_scatter)

# Plot 1.5: Bar chart for each planet based on diameter

# Filter the DataFrame based on the selected minimum diameter size
filtered_planets_df = planets_df[planets_df['diameter'] >= min_diameter_size]

# Set up the plot
fig_bar, ax_bar = plt.subplots(figsize=(10, 6))

# Plot a bar chart for each planet based on diameter
ax_bar.bar(filtered_planets_df['name'], filtered_planets_df['diameter'])

# Set axis labels and title
ax_bar.set_title('Planet Diameter Comparison')
ax_bar.set_xlabel('Planet Name')
ax_bar.set_ylabel('Diameter (km)')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the plot in Streamlit app
st.pyplot(fig_bar)

# plot 2
st.header('Distribution of Planet Diameter')

# Add an input field for manually typing the number of bins
num_bins = st.number_input('Enter the Number of Bins:', min_value=5, max_value=50, value=30)

# Add a slider for selecting the maximum diameter
max_diameter = st.slider('Select Maximum Diameter (km):', min_value=0, max_value=30000, value=20000)

# Filter the DataFrame based on the selected maximum diameter
filtered_planets_df = planets_df[planets_df['diameter'] <= max_diameter]

# Set up the plot
fig_hist, ax_hist = plt.subplots(figsize=(10, 6))

# Visualize the distribution of diameter
sns.histplot(filtered_planets_df['diameter'].dropna(), bins=num_bins, kde=True, ax=ax_hist)

# Set axis labels and title
ax_hist.set_title('Distribution of Planet Diameter')
ax_hist.set_xlabel('Diameter')
ax_hist.set_ylabel('Frequency')

# Display the plot in Streamlit app
st.pyplot(fig_hist)

# Plot 3: Scatter plot with regression line (Diameter vs Population)
st.header('Planet Diameter vs Population (Excluding Outliers)')

# Add sliders for selecting the diameter and population thresholds
diameter_threshold = st.slider('Select Diameter Threshold:', min_value=0, max_value=30000, value=20000)
population_threshold = st.slider('Select Population Threshold:', min_value=0, max_value=20000000000, value=10000000000)

# Remove outliers based on selected thresholds
filtered_planets_df = planets_df[(planets_df['diameter'] < diameter_threshold) & (planets_df['population'] < population_threshold)]

# Set up the plot
fig_regplot, ax_regplot = plt.subplots(figsize=(12, 8))

# Create a scatter plot with a red regression line, 95% confidence interval, and label
sns.regplot(x='diameter', y='population', data=filtered_planets_df, scatter_kws={'s': filtered_planets_df['diameter'] / 500}, line_kws={'color': 'red'}, ax=ax_regplot)

# Add a separate line without markers for the legend
ax_regplot.plot([], [], color='red', label=f'Regression Line (Corr: {filtered_planets_df["diameter"].corr(filtered_planets_df["population"]):.2f})')

# Set axis labels and title
ax_regplot.set_title('Planet Diameter vs Population (Excluding Outliers)')
ax_regplot.set_xlabel('Diameter (km)')
ax_regplot.set_ylabel('Population (millions)')

# Add legend
ax_regplot.legend()

# Display the plot in Streamlit app
st.pyplot(fig_regplot)



# Load data from the provided URL
url = 'https://raw.githubusercontent.com/boi-andy/final_project/main/data/people_data.csv'
characters_df = pd.read_csv(url)

# Streamlit app
st.title('Star Wars Characters Height Box Plot')

# Add input fields for manually typing the height range
min_height = st.number_input('Enter Minimum Height (cm):', min_value=0, max_value=300, value=0)
max_height = st.number_input('Enter Maximum Height (cm):', min_value=0, max_value=300, value=300)

# Filter the DataFrame based on the selected height range
filtered_characters_df = characters_df[(characters_df['Height'] >= min_height) & (characters_df['Height'] <= max_height)]

# Set up the plot
fig_boxplot, ax_boxplot = plt.subplots(figsize=(10, 6))

# Create a box plot of height by gender
sns.boxplot(x='Gender', y='Height', data=filtered_characters_df, order=['male', 'female', 'Unidentified'], palette='Set2', ax=ax_boxplot)

# Set title and labels
ax_boxplot.set_title('Box Plot of Height by Gender in Star Wars Characters')
ax_boxplot.set_ylabel('Height (cm)')

# Display the plot in Streamlit app
st.pyplot(fig_boxplot)

# Final Plot
# Filter numeric columns
numeric_columns = characters_df.select_dtypes(include=['number']).columns

# Streamlit app
st.title('Scatter Plot and Regression Analysis')

# Add dropdown menu for selecting variables
x_variable = st.selectbox('Select X Variable:', numeric_columns)
y_variable = st.selectbox('Select Y Variable:', numeric_columns)

# Add input field for confidence level
confidence_level = st.number_input('Enter Confidence Level (%):', min_value=1, max_value=100, value=95)

# Scatter plot
fig_scatter, ax_scatter = plt.subplots(figsize=(10, 6))
sns.scatterplot(x=x_variable, y=y_variable, data=characters_df, ax=ax_scatter)

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(characters_df[x_variable], characters_df[y_variable])

# Add regression line to the plot
ax_scatter.plot(characters_df[x_variable], slope * characters_df[x_variable] + intercept, color='red', label=f'Regression Line (R-Squared: {r_value**2:.2f})')

# Set axis labels and title
ax_scatter.set_xlabel(x_variable)
ax_scatter.set_ylabel(y_variable)
ax_scatter.set_title(f'Scatter Plot of {y_variable} vs {x_variable}')

# Add legend
ax_scatter.legend()

# Display the plot in Streamlit app
st.pyplot(fig_scatter)

# Plot of people
st.title('Character Details Search')

# Create a dropdown menu for character selection
selected_character = st.selectbox('Select a Character:', characters_df['name'])

# Display details of the selected character
if st.button('Show Details'):
    character_details = characters_df[characters_df['name'] == selected_character]
    st.write(character_details)
