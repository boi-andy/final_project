import streamlit as st
import requests

# Function to fetch all planets from SWAPI
def get_all_planets():
    api_url = 'https://swapi.dev/api/planets/'
    all_planets = []
    next_page = api_url

    while next_page:
        response = requests.get(next_page)
        data = response.json()
        all_planets.extend(data['results'])
        next_page = data['next']

    return all_planets

# Function to fetch planet data from SWAPI by name
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

# Function to fetch people from a planet
def get_people_from_planet(planet_data):
    people_list = []
    for resident in planet_data['residents']:
        person_data = requests.get(resident).json()
        people_list.append(person_data['name'])
    return people_list

# Function to fetch detailed information about a person
def get_person_details(person_name):
    api_url = f'https://swapi.dev/api/people/'
    params = {'search': person_name}
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

    # Fetch all planets
    all_planets = get_all_planets()
    planet_names = [planet['name'] for planet in all_planets]

    # Dropdown list to select a planet by name
    selected_planet_name = st.selectbox('Select a Planet:', planet_names, index=0)

    # Fetch planet data
    planet_data = get_planet_data(selected_planet_name)

    # Display planet information
    if planet_data:
        st.subheader(f"Planet Information for {selected_planet_name}")
        st.write("Climate (C):", planet_data['climate'])
        st.write("Diameter (km):", planet_data['diameter'])
        st.write("Gravity:", planet_data['gravity'])
        st.write("Orbital Period:", planet_data['orbital_period'])
        st.write("Population:", planet_data['population'])

        # Fetch and display people from the planet
        people_list = get_people_from_planet(planet_data)
        if people_list:
            st.subheader("People from this Planet:")
            selected_person_name = st.selectbox('Select a Person:', people_list, index=0)
            
            # Fetch and display details about the selected person
            person_details = get_person_details(selected_person_name)
            if person_details:
                st.subheader(f"Details for {selected_person_name}")
                st.write("Birth Year:", person_details['birth_year'])
                st.write("Gender:", person_details['gender'])
                st.write("Height (m):", person_details['height'])
                st.write("Mass:", person_details['mass'])
                # Add more details as needed
            else:
                st.write("No information available for the selected person.")
        else:
            st.write("No information about residents available.")
    else:
        st.error(f"Failed to retrieve planet information for {selected_planet_name}")

if __name__ == '__main__':
    main()
