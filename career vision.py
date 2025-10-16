import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="AI CareerVision", page_icon="ðŸŽ¯", layout="centered")
st.title("ðŸŽ¯ AI CareerVision â€“ Smarter Career Decisions Through Data & AI")
st.write("Find your best-fit career using your skills, interests, and logic levels.")

st.header("ðŸ§© Enter Your Skill Ratings (0 - 10)")
python = st.slider("Python / Programming Skill", 0, 10, 5)
communication = st.slider("Communication Skill", 0, 10, 5)
creativity = st.slider("Creativity", 0, 10, 5)
logic = st.slider("Logical Thinking", 0, 10, 5)

st.header("ðŸŽ¯ Choose Your Area of Interest")
interest = st.selectbox(
    "Select Interest Area",
    ["Data", "AI", "Design", "Management"]
)

data = {
    "Python": [9, 7, 2, 3, 5, 4, 8, 1],
    "Communication": [6, 5, 8, 9, 7, 4, 3, 8],
    "Creativity": [5, 4, 9, 8, 6, 7, 3, 9],
    "Logic": [9, 8, 3, 4, 6, 5, 9, 2],
    "Interest": ["Data", "AI", "Design", "Management", "AI", "Data", "Design", "Management"],
    "Career": [
        "Data Scientist",
        "AI Engineer",
        "UI/UX Designer",
        "Business Analyst",
        "AI Researcher",
        "Data Analyst",
        "Product Designer",
        "Project Manager"
    ]
}

df = pd.DataFrame(data)
le = LabelEncoder()
df["Interest"] = le.fit_transform(df["Interest"])

X = df[["Python", "Communication", "Creativity", "Logic", "Interest"]]
y = df["Career"]

model = RandomForestClassifier()
model.fit(X, y)

input_data = pd.DataFrame({
    "Python": [python],
    "Communication": [communication],
    "Creativity": [creativity],
    "Logic": [logic],
    "Interest": [le.transform([interest])[0]]
})

if st.button("ðŸ” Predict My Career"):
    prediction = model.predict(input_data)[0]
    st.success(f"ðŸ’¡ Based on your profile, your best-fit career is: *{prediction}*")

    st.subheader("âœ¨ Career Insights")
    if prediction == "Data Scientist":
        st.write("- Strong in logic and programming. Learn Python, SQL, and ML.")
    elif prediction == "AI Engineer":
        st.write("- Focus on AI models, neural networks, and real-world applications.")
    elif prediction == "UI/UX Designer":
        st.write("- Improve visual creativity and user research skills.")
    elif prediction == "Business Analyst":
        st.write("- Enhance data interpretation and communication.")
    elif prediction == "AI Researcher":
        st.write("- Study advanced AI concepts and pursue research opportunities.")
    elif prediction == "Data Analyst":
        st.write("- Work on Excel, Power BI, and data visualization.")
    elif prediction == "Product Designer":
        st.write("- Combine creativity with problem-solving.")
    elif prediction == "Project Manager":
        st.write("- Focus on leadership, communication, and organization skills.")

st.write("---")
st.caption("Created by *Nirmala S* | Built with ðŸ’» Streamlit, Scikit-learn & ChatGPT")
