import streamlit

streamlit.title ("My Mom's New Healthy Diner")
streamlit.header ('Breakfast Menu')
streamlit.text ('🥣Omega 3 and Blueberry Oatmeal')
streamlit.text ('🥗Kale, Spinach and Rocket Smoothie')
streamlit.text ('🐔Hard-boiled Free Range Egg')
streamlit.text ('🥑Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_imdex ('Fruit') 
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)), (['Avacado', 'Strawberries'])
streamlit.dataframe(my_fruit_list)
