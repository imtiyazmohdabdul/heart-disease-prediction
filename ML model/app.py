import streamlit as st 
import joblib

model = joblib.load("heart.h5")

st.title("Heart disease prediction appp")
st.header('This app predicts if aperson has heart disease')







age = st.sidebar.number_input('Enter your age: ')

sex  = st.sidebar.radio('Sex',(0,1))
cp = st.sidebar.radio('Chest pain type',(0,1,2,3))
tres = st.sidebar.number_input('Resting blood pressure: ')
chol = st.sidebar.number_input('Serum cholestoral in mg/dl: ')
fbs = st.sidebar.radio('Fasting blood sugar',(0,1))
res = st.sidebar.number_input('Resting electrocardiographic results: ')
tha = st.sidebar.number_input('Maximum heart rate achieved: ')
exa = st.sidebar.radio('Exercise induced angina: ',(0,1))
old = st.sidebar.number_input('oldpeak ')
slope = st.sidebar.number_input('he slope of the peak exercise ST segmen: ')
ca = st.sidebar.radio('number of major vessels',(0,1,2,3))
thal = st.sidebar.radio('thal',(0,1,2))


if st.button("predict"):
    st.success("Thanks ")
    prediction= model.predict([[age,sex,cp,tres,chol,fbs,res,tha,exa,old,slope,ca,thal]])
    st.success(prediction)
    