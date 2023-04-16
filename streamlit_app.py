import streamlit as st
import pandas as pd

st.title("My Mom's New Healthy Diner")

# Breakfast menu
st.header("Breakfast Menu")
st.write("🥣 Omega 3 & Blueberry Oatmeal")
st.write("🥗 Kale, Spinach & Rocket Smoothie")
st.write("🐔 Hard-Boiled Free-Range Egg")
st.write("🥑🍞 Avocado Toast 🥑🍞")

# Special menu item
st.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

# Read CSV file into dataframe
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Create a list of fruits to choose from
fruit_options = list(my_fruit_list.index)

# Add a Multi-select widget to the app
selected_fruits = st.multiselect('Select your fruits:', fruit_options)

# Filter the dataframe to show only the selected fruits
filtered_fruit_list = my_fruit_list.loc[selected_fruits, :]

# Display the filtered dataframe
st.dataframe(filtered_fruit_list)

import requests
import streamlit as st

# Make the API request
response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# Parse the JSON response
data = response.json()

# Display the fruit information
st.write("Name:", data["name"])
st.write("Genus:", data["genus"])
st.write("Family:", data["family"])
st.write("Nutrition:", data["nutritions"])
st.write("Image:", data["image"])
