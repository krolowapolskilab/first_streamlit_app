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

# Create a list of fruits to choose from
fruit_options = ['Apple', 'Banana', 'Blueberry', 'Cherry', 'Kiwi', 'Mango', 'Pineapple', 'Strawberry']

# Add a Multi-select widget to the app
selected_fruits = st.multiselect('Select your fruits:', fruit_options)

# Read CSV file into dataframe
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Filter the dataframe to show only the selected fruits
filtered_fruit_list = my_fruit_list[my_fruit_list['Fruit'].isin(selected_fruits)]

# Display the filtered dataframe
st.dataframe(filtered_fruit_list)
