import streamlit
import pandas

streamlit.title("My Mom's New Healthy Diner")

# Breakfast menu
streamlit.header("Breakfast Menu")
streamlit.write("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.write("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.write("🐔 Hard-Boiled Free-Range Egg")
streamlit.write("🥑🍞 Avocado Toast 🥑🍞")

# Special menu item
streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.

# Read CSV file into dataframe
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Display dataframe
streamlit.dataframe(my_fruit_list)


