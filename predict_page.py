import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary """)

    countries = (
            "United States of America",
            "India",
            "Germany",
            "United Kingdom of Great Britain and Northern Ireland",
            "Canada",
            "France",
            "Brazil",
            "Spain",
            "Netherlands",
            "Australia",
            "Poland",
            "Italy",
            "Russian Federation",
            "Sweden",
            "Turkey",
            "Switzerland",
            "Israel",
            "Norway",
            "Other",
    )

    education = (
            "Less than a Bachelors",
            "Bachelor’s degree",
            "Master’s degree",
            "Post grad",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)

    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, experience]])
        X[:,0] = le_country.transform(X[:,0])
        X[:,1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:2f}")
