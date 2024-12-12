import streamlit as st

st.title("My New App")
st.write("This is my new Streamlit app Isset Villegas")

st.write("This is a change")

row1 = st.columns(3)
row2 = st.columns(3)

grid = [col.container(height=200) for col in row1 + row2]
safe_grid = [card.empty() for card in grid]

def black_cats():
    time.sleep(1)
    st.title("🐈‍⬛ 🐈‍⬛")
    st.markdown("🐾 🐾 🐾 🐾")


def orange_cats():
    time.sleep(1)
    st.title("🐈 🐈")
    st.markdown("🐾 🐾 🐾 🐾")

def cats():
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        black_cats()
    with container_b:
        black_cats()
    with container_c:
        black_cats()

