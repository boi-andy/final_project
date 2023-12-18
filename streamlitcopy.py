import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data_file_path = 'planets_data.csv'
planets_df = pd.read_csv(data_file_path)

url = 'https://github.com/boi-andy/final_project/planets_data.csv'
planets_df = pd.read_csv(url)

# Streamlit app
st.title('Star Wars Planets Diameter Visualization')

# Display the DataFrame if needed
# st.dataframe(planets_df)

# Plot the graph using matplotlib in Streamlit
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(planets_df['name'], planets_df['diameter'])
plt.xticks(rotation=45, ha='right')
plt.title('Diameter of Star Wars Planets')
plt.xlabel('Planet Name')
plt.ylabel('Diameter (km)')
plt.tight_layout()

# Display the plot in Streamlit app
st.pyplot(fig)
