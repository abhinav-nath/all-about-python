import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("This is a Title")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("This is a text")

# Markdown
st.markdown("### This is a markdown")

# success
st.success("Success")

# success
st.info("Information")

# success
st.warning("Warning")

# success
st.error("Error")

# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)


st.markdown("""---""")


# Write text
st.subheader("Write text")
st.write("Text with write")

# Using write function, we can also display code in coding format.
# This is not possible using st.text().
st.write(range(10))


st.markdown("""---""")


# Check box
# A checkbox returns a boolean value. When the box is checked, it returns a True value else returns a False value.
st.subheader("st.checkbox")

st.write('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great! Here's some more 🍦")

if coffee:
    st.write("Okay, here's some coffee ☕")

if cola:
    st.write("Here you go 🥤")


st.markdown("""---""")


# Radio button
st.subheader("st.radio - Radio button")
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")


st.markdown("""---""")


# Selection box
st.subheader("st.selectbox - Selection box")
# first argument takes the title of the selection box
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])

# print the selected hobby
st.write("Your hobby is: ", hobby)


st.markdown("""---""")


# Multi-Select box
st.subheader("st.multiselect - Multi-Select box")
# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])

# write the selected options
st.write("You selected", len(hobbies), 'hobbies')


st.markdown("""---""")


# Button
st.subheader("st.button")
# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if (st.button("Click me!")):
    st.text("Button clicked!!!")


# Text Input
st.subheader("st.text_input")
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if (st.button('Submit')):
    result = name.title()
    st.success(result)


st.markdown("""---""")


# Slider
st.subheader("st.slider")
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)

# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))


st.markdown("""---""")


# Display a static table
st.subheader("st.table - Static table")
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)


st.markdown("""---""")


# Display JSON content
st.subheader("st.json - JSON content")
st.json({
    'fruit': 'apple',
    'book': 'maths',
    'game': 'football'
})
