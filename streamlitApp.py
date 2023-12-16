import streamlit as st
import requests

# Function to fetch planet data from SWAPI
def get_planet_data(planet_name):
    api_url = f'https://swapi.dev/api/planets/'
    params = {'search': planet_name}
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]
        else:
            return None
    else:
        return None

# Streamlit app
def main():
    st.title('Star Wars Planet Information')

    # Fetch all planet names
    api_url = 'https://swapi.dev/api/planets/'
    all_planets = requests.get(api_url).json()['results']
    planet_names = [planet['name'] for planet in all_planets]

    # Dropdown list to select a planet by name
    selected_planet_name = st.selectbox('Select a Planet:', planet_names, index=0)

    # Fetch planet data
    planet_data = get_planet_data(selected_planet_name)

    # Display planet information
    if planet_data:
        st.subheader(f"Planet Information for {selected_planet_name}")
        st.write("Climate:", planet_data['climate'])
        st.write("Diameter:", planet_data['diameter'])
        st.write("Gravity:", planet_data['gravity'])
        st.write("Orbital Period:", planet_data['orbital_period'])
        st.write("Population:", planet_data['population'])
    else:
        st.error(f"Failed to retrieve planet information for {selected_planet_name}")

if __name__ == '__main__':
    main()
