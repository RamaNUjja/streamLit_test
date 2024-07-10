import streamlit as st
st.write("Hello world")

st.title('Uber pickups in NYC')
st.header('This is a header with a divider', divider='green')
st.subheader('This is a subheader with a divider', divider='rainbow')
st.subheader('_Streamlit_ is :blue[soo cool] :sunglasses:')

agree = st.checkbox("I consent")

if agree:
    st.write("Access Granted!")

genre = st.radio(
    "What's your favorite movie's genre",
    [":rainbow[Comedy]", "*Drama*", "Documentary :movie_camera:"],
    captions = ["Thahaaka Laga ke", "Saas, Bahu and sajish", "100% Gyan."])

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
elif genre == "*Drama*":
    st.write("You selected Drama")
else:
    st.success("You selected Documentary") # This will reflect different output UI

st.button("Reset", type="primary")
if st.button("Say Hello"):
    st.write("Stay away from 'Hello'")
else:
    st.write("That's Good")

def cube(num):
    return num**3
num= st.number_input("Insert a number")
if(st.button("cube")):
    st.text(cube(num))
if(st.button("Square")):
    st.text(num**2)

