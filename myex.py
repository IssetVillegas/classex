import streamlit as st

st.title("My New App")
st.write("This is my new Streamlit app Isset Villegas")

row1 = st.columns(3)
row2 = st.columns(3)

grid = [col.container(height=200) for col in row1 + row2]
safe_grid = [card.empty() for card in grid]