import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.pkl')

st.title("🏥 Medical Insurance Cost Prediction App")
st.write("Enter patient details below to estimate expected medical insurance charges.")

st.sidebar.header("Patient Parameters")

def user_input_features():
    age = st.sidebar.slider('Age', 18, 64, 30)
    sex = st.sidebar.selectbox('Sex', ('male', 'female'))
    bmi = st.sidebar.slider('BMI (Body Mass Index)', 15.0, 53.0, 25.0)
    children = st.sidebar.selectbox('Number of Children', (0, 1, 2, 3, 4, 5))
    smoker = st.sidebar.selectbox('Smoker', ('no', 'yes'))
    region = st.sidebar.selectbox('Region', ('southwest', 'southeast', 'northwest', 'northeast'))

    # Encode inputs to match training mapping
    sex_val = 1 if sex == 'male' else 0
    smoker_val = 1 if smoker == 'yes' else 0
    
    region_northwest = 1 if region == 'northwest' else 0
    region_southeast = 1 if region == 'southeast' else 0
    region_southwest = 1 if region == 'southwest' else 0

    data = {
        'age': age,
        'sex': sex_val,
        'bmi': bmi,
        'children': children,
        'smoker': smoker_val,
        'region_northwest': region_northwest,
        'region_southeast': region_southeast,
        'region_southwest': region_southwest
    }
    
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

st.subheader("📋 Patient Profile Summary")
st.write(input_df)

if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Medical Insurance Cost: **${prediction[0]:,.2f}**")