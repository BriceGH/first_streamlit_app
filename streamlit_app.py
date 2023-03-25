import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
   
streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Cours  Lesson 3: A Quick and Easy Streamlit App!  🥋 Importing pandas
#Cours  Lesson 3: A Quick and Easy Streamlit App!  🥋 Importing pandas 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.text(fruityvice_response)

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice fruits Advice!')

try:
fruit_choice = streamlit.text_input('What fruit would you like information about?')  

if not fruit_choice:
   fruit_choice = streamlit.error("Please select a fruit to get information.")

else:   
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

except URLError as e:
streamlit.error()
