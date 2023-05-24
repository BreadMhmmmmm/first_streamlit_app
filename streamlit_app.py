import streamlit

streamlit.title('My Parents new and healthy dinner')

streamlit.header('Healthy Breakfast menu ;)')
streamlit.text('🥣Strawberry Protein Pancakes')
streamlit.text(' 🥗 Kale smoothie')
streamlit.text('🍞Eggs on toast')
streamlit.text('🍞Carror ommelete')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
