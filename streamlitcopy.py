import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/boi-andy/final_project/main/planets_data.csv'
planets_df = pd.read_csv(url)

# Streamlit app
st.title('Star Wars Planets Data Exploration')

# Plot 1: Scatter plot with circles for each planet based on diameter
st.header('Planet Diameter Comparison')

# Add a dropdown menu for selecting a specific planet
selected_planet_scatter = st.selectbox('Select a Planet:', planets_df['name'])

# Set up the plot
fig_scatter, ax_scatter = plt.subplots(figsize=(12, 8))

# Plot circles for each planet based on diameter
for index, planet in planets_df.iterrows():
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

# Plot 2: Distribution of planet diameter
st.header('Distribution of Planet Diameter')

# Add a slider for selecting the number of bins
num_bins = st.slider('Select the Number of Bins:', min_value=5, max_value=50, value=30)

# Set up the plot
fig_hist, ax_hist = plt.subplots(figsize=(10, 6))

# Visualize the distribution of diameter
sns.histplot(planets_df['diameter'].dropna(), bins=num_bins, kde=True, ax=ax_hist)

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
