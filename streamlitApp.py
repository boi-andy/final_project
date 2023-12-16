import streamlit as st
import requests

# Function to fetch planet data from SWAPI
def get_planet_data(planet_id):
    api_url = f'https://swapi.dev/api/planets/{planet_id}/'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit app
def main():
    st.title('Star Wars Planet Information')

    # Sidebar with user input
    planet_id = st.sidebar.number_input('Enter Planet ID:', min_value=1, max_value=61, value=1)

    # Fetch planet data
    planet_data = get_planet_data(planet_id)

    # Display planet information
    if planet_data:
        st.subheader(f"Planet Information for ID {planet_id}")
        st.write("Name:", planet_data['name'])
        st.write("Climate:", planet_data['climate'])
        st.write("Diameter:", planet_data['diameter'])
        st.write("Gravity:", planet_data['gravity'])
        st.write("Orbital Period:", planet_data['orbital_period'])
        st.write("Population:", planet_data['population'])
        st.write("Residents:", planet_data['residents'])
    else:
        st.error(f"Failed to retrieve planet information for ID {planet_id}")

if __name__ == '__main__':
    main()
