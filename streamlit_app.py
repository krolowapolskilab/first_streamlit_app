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

# New Section to display fruityvice api response
import streamlit as st
import pandas
import requests

st.header("Fruityvice Fruit Advice!")

# Add a text entry box for the user to input their desired fruit
fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered:', fruit_choice)

# Separate the base URL from the fruit name
base_url = "https://fruityvice.com/api/fruit/"
fruit_url = base_url + fruit_choice.lower()

# Send the API request using the fruit URL
fruityvice_response = requests.get(fruit_url)

# Normalize the JSON data and display in a dataframe
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalized)

import snowflake.connector

import snowflake.connector
import streamlit as st

# Connect to Snowflake
try:
    cnx = snowflake.connector.connect(
        user="krolowapolski",
        password="Sunny4Ever2019",
        account="jo55688.ca-central-1.aws",
        warehouse="pc_rivery_wh",
        database="pc_rivery_db",
        schema="public"
    )
    # Query the data from the fruit_load_list table
    cur = cnx.cursor()
    cur.execute("SELECT * FROM fruit_load_list")
    rows = cur.fetchall()
    
    # Display the data
    st.header("Fruit load list contains:")
    st.dataframe(rows)
    
    cnx.close()
except Exception as e:
    st.write("Connection failed: ", e)

import snowflake.connector
import streamlit as st

# Connect to Snowflake
cnx = snowflake.connector.connect(
    user="krolowapolski",
    password="Sunny4Ever2019",
    account="jo55688.ca-central-1.aws",
    warehouse="pc_rivery_wh",
    database="pc_rivery_db",
    schema="public"
)

# Add default fruits to the list
default_fruits = ["jackfruit", "papaya", "guava", "kiwi"]
with cnx.cursor() as cur:
    for fruit in default_fruits:
        cur.execute(f"INSERT INTO fruit_load_list VALUES ('{fruit}')")
    cnx.commit()

# Query the data from the fruit_load_list table
cur = cnx.cursor()
cur.execute("SELECT * FROM fruit_load_list")
rows = cur.fetchall()

# Display the data
st.header("Fruit load list contains:")
st.dataframe(rows)

# Allow the end user to add a fruit to the list
fruit_choice = st.text_input('What fruit would you like to add?', 'Kiwi')

if st.button('Add fruit'):
    try:
        with cnx.cursor() as cur:
            cur.execute(f"INSERT INTO fruit_load_list VALUES ('{fruit_choice}')")
            cnx.commit()
        
        st.success(f"Thanks for adding {fruit_choice}!")
    except Exception as e:
        st.error(f"Error adding {fruit_choice}: {e}")

cnx.close()
