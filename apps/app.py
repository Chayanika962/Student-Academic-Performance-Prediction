# Import Streamlit to create the web application
import streamlit as st

# Import Joblib to load our saved machine learning model
import joblib

# Import Pandas to handle student data
import pandas as pd

# Import OS to work with file paths
import os
# Get the path of the saved model
model_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "best_student_performance_model.pkl"
)

# Load the trained model
model = joblib.load(model_path)

# Display a message in the terminal
print("Model loaded successfully!")
# Set the title of the web application
st.title("Student Academic Performance Prediction")

# Add a short description
st.write(
    "This application predicts whether a student will Pass or Fail "
    "based on their academic, personal and social information."
)

# Add a subheading
st.header("Enter Student Details")

# Personal information
school = st.selectbox("School", ["GP", "MS"])
sex = st.selectbox("Gender", ["F", "M"])
age = st.number_input("Age", min_value=15, max_value=22, value=17)

address = st.selectbox("Home Address Type", ["U", "R"])
famsize = st.selectbox("Family Size", ["GT3", "LE3"])
Pstatus = st.selectbox("Parents' Cohabitation Status", ["T", "A"])

# Parents' education
Medu = st.selectbox("Mother's Education", [0, 1, 2, 3, 4])
Fedu = st.selectbox("Father's Education", [0, 1, 2, 3, 4])

# Parents' jobs
Mjob = st.selectbox(
    "Mother's Job",
    ["teacher", "health", "services", "at_home", "other"]
)

Fjob = st.selectbox(
    "Father's Job",
    ["teacher", "health", "services", "at_home", "other"]
)

# Reason for choosing school
reason = st.selectbox(
    "Reason for Choosing School",
    ["home", "reputation", "course", "other"]
)

guardian = st.selectbox(
    "Student's Guardian",
    ["mother", "father", "other"]
)

# Travel and study time
traveltime = st.selectbox("Travel Time to School", [1, 2, 3, 4])

studytime = st.selectbox("Weekly Study Time", [1, 2, 3, 4])

failures = st.selectbox("Number of Past Class Failures", [0, 1, 2, 3])

# Extra educational support
schoolsup = st.selectbox("Extra School Support", ["yes", "no"])
famsup = st.selectbox("Family Educational Support", ["yes", "no"])
paid = st.selectbox("Extra Paid Classes", ["yes", "no"])

# Activities and facilities
activities = st.selectbox("Extra-curricular Activities", ["yes", "no"])
nursery = st.selectbox("Attended Nursery School", ["yes", "no"])
higher = st.selectbox("Wants Higher Education", ["yes", "no"])
internet = st.selectbox("Internet Access at Home", ["yes", "no"])
romantic = st.selectbox("In a Romantic Relationship", ["yes", "no"])

# Family and social life
famrel = st.selectbox("Family Relationship Quality", [1, 2, 3, 4, 5])
freetime = st.selectbox("Free Time After School", [1, 2, 3, 4, 5])
goout = st.selectbox("Going Out with Friends", [1, 2, 3, 4, 5])

# Alcohol consumption
Dalc = st.selectbox("Workday Alcohol Consumption", [1, 2, 3, 4, 5])
Walc = st.selectbox("Weekend Alcohol Consumption", [1, 2, 3, 4, 5])

# Health and attendance
health = st.selectbox("Current Health Status", [1, 2, 3, 4, 5])
absences = st.number_input("Number of School Absences", min_value=0, value=0)

# Store all student information in a dictionary
student_data = {
    "school": school,
    "sex": sex,
    "age": age,
    "address": address,
    "famsize": famsize,
    "Pstatus": Pstatus,
    "Medu": Medu,
    "Fedu": Fedu,
    "Mjob": Mjob,
    "Fjob": Fjob,
    "reason": reason,
    "guardian": guardian,
    "traveltime": traveltime,
    "studytime": studytime,
    "failures": failures,
    "schoolsup": schoolsup,
    "famsup": famsup,
    "paid": paid,
    "activities": activities,
    "nursery": nursery,
    "higher": higher,
    "internet": internet,
    "romantic": romantic,
    "famrel": famrel,
    "freetime": freetime,
    "goout": goout,
    "Dalc": Dalc,
    "Walc": Walc,
    "health": health,
    "absences": absences
}

# Convert the dictionary into a Pandas DataFrame
input_data = pd.DataFrame([student_data])

# Create a button for making predictions
if st.button("Predict Student Performance"):

    # Use the trained model to predict the result
    prediction = model.predict(input_data)

    # Display the prediction
    st.subheader("Prediction Result")

    if prediction[0] == "Pass":
        st.success("The student is predicted to PASS.")
    else:
        st.error("The student is predicted to FAIL.")