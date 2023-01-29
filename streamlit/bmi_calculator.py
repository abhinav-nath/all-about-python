import streamlit as st

# BMI Formula
# weight in kilograms divided by the square of height in meters

st.title('BMI Calculator')

weight = st.number_input('Enter your weight (in kgs)')

status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))

if (status == 'cms'):
    height = st.number_input('Centimeters')
    height = height / 100

elif (status == 'feet'):
    height = st.number_input('Feet')
    height = height / 3.28

else:
    height = st.number_input('Meters')

try:
    bmi = weight / (height ** 2)
except:
    st.text("Enter some value of height")


# check if the button is pressed or not
if (st.button('Calculate BMI', disabled=weight <= 0 or height <= 0)):
    # print the BMI INDEX
    st.markdown("Your BMI Index is **{}**".format(str(round(bmi, 2))))

    # give the interpretation of BMI index
    if (bmi < 16):
        st.error("You are Extremely Underweight")
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif (bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif (bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif (bmi >= 30):
        st.error("Extremely Overweight")
