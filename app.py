import pandas as pd
from sklearn.linear_model import LinearRegression
import streamlit as st

student_data=pd.read_csv("Student_Performance.csv")

X_student=student_data[["Study_Hours_Per_Day","Attendance_Percentage","Sleep_Hours_Per_Night","Previous_Class_Score"]]
y_student=student_data["End_Examination_Mark"]

model=LinearRegression()
model.fit(X_student,y_student)

st.title("EduPredict 🎓")
st.write("Predicting Student Performance Based on Study Habits and Attendance")

study_hours=st.number_input("Study Hours Per Day",min_value=0,max_value=24,step=1)
attendance_percentage=st.number_input("Attendance Percentage",min_value=0,max_value=100,step=1)
sleep_hours=st.number_input("Sleep Hours Per Night",min_value=0,max_value=24,step=1)
Previous_class_score=st.number_input("Previous Class Score",min_value=0,max_value=100,step=1)

if study_hours==0 and attendance_percentage==0 and sleep_hours==0 and Previous_class_score==0:
    st.warning("Please enter values for all input fields to get a prediction.")

if st.button("Predict End Examination Mark"):
    input_data=[[study_hours,attendance_percentage,sleep_hours,Previous_class_score]]
    predicted_mark=model.predict(input_data)
    if predicted_mark[0]<0:
        st.error("Fail Need to improve study habits and attendance.")
    elif predicted_mark[0]>100:
        st.success("Excellent! Their are more than 90% chances to get a good mark.")
    else:
        st.success(f"Predicted End Examination Mark: {predicted_mark[0]:,.2f}")
