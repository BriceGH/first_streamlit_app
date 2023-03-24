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
#fruits_to_show = my_fruit_list.loc[fruits_selected]
my_fruit_list = my_fruit_list.set_index('Fruit')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
#streamlit.dataframe(my_fruit_list)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())
streamlit.header("Fruityvice fruits Advice!")
   
#fruit_choice = streamlit.text_input('What fruit would you like information about?')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')         
streamlit.write('The user entered ', fruit_choice)
  
streamlit.error("Please select a fruit to get information.")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_rows)

add_myfruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('Thanks for addingjackfruit', add_myfruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
