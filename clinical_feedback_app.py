
import streamlit as st

# Clinical case details
clinical_case = '''
Patient: Jane Doe, 45-year-old female
Chief Complaints:
1. Abdominal pain: Severe, cramping pain in the upper abdomen for the past 2 days.
2. Nausea and vomiting: Started 1 day ago.
3. Fever: Low-grade fever for the past 1 day.
History of Present Illness (Narrative): "I've been having this really bad cramping pain in my upper abdomen for the past 2 days. It started suddenly and has been getting worse. Yesterday, I started feeling nauseous and threw up a couple of times. I also noticed that I have a slight fever. The pain is constant and doesn't seem to go away no matter what I do. I haven't had any issues like this before, and I'm really worried because it's getting worse.
Looking back, I think I might have had some mild discomfort in my abdomen about a week ago, but I didn't pay much attention to it because it wasn't too bad. I thought it was just something I ate. Over the past few months, I've been feeling more tired than usual and sometimes a bit bloated after meals, but I didn't think much of it. I haven't had any major health problems before, except for my hypertension, which has been well-controlled with medication.
I don't drink much alcohol, maybe a glass of wine occasionally, and I don't smoke. My diet is pretty balanced, but I do enjoy fatty foods now and then. I work as an office manager, so I spend a lot of time sitting at my desk. I haven't traveled recently, and I haven't been around anyone who's been sick. My father had a heart attack when he was 55, and my mother has hypertension, but there's no history of diabetes or gastrointestinal issues in my family."
Summarized History of Present Illness: Jane Doe, a 45-year-old female with a history of hypertension, presents with severe, cramping abdominal pain for 2 days, nausea and vomiting for 1 day, and a low-grade fever for 1 day. She reports mild abdominal discomfort about a week ago and has felt more tired and bloated after meals over the past few months. The pain is constant and worsening, and she has no previous history of similar symptoms.
Past Medical History:
• Hypertension for 10 years, well-controlled with medication.
• No history of diabetes, asthma, or chronic obstructive pulmonary disease (COPD).
Social History:
• Non-smoker.
• Occasional alcohol consumption.
• Works as an office manager.
• No recent travel history.
Family History:
• Father had a myocardial infarction at age 55.
• Mother has hypertension.
Medications:
• Amlodipine 5 mg daily.
Allergies:
• No known drug allergies.
'''

model_answer = '''
A 45-year-old female with a history of hypertension presents with severe, cramping abdominal pain for 2 days, nausea and vomiting for 1 day, and a low-grade fever for 1 day, with a background of mild abdominal discomfort a week ago and fatigue and bloating after meals over the past few months.
'''

# Function to provide feedback
def provide_feedback(student_answer):
    feedback = ""
    
    # Check for person details
    if "45-year-old female" in student_answer:
        feedback += "✅ Person details included.
"
    else:
        feedback += "❌ Person details missing.
"
    
    # Check for time frame
    if "2 days" in student_answer and "1 day" in student_answer:
        feedback += "✅ Time frame included.
"
    else:
        feedback += "❌ Time frame missing.
"
    
    # Check for symptoms/syndrome
    symptoms = ["abdominal pain", "nausea", "vomiting", "fever"]
    symptoms_included = [symptom for symptom in symptoms if symptom in student_answer]
    if len(symptoms_included) == len(symptoms):
        feedback += "✅ Symptoms/syndrome included.
"
    else:
        feedback += f"❌ Symptoms/syndrome missing: {', '.join(set(symptoms) - set(symptoms_included))}.
"
    
    return feedback

# Streamlit app layout
st.title("Clinical Reasoning Feedback Chatbot")
st.write("### Clinical Case")
st.write(clinical_case)

st.write("### Your Problem Representation")
student_answer = st.text_area("Enter your problem representation here:")

if st.button("Submit"):
    if student_answer:
        feedback = provide_feedback(student_answer)
        st.write("### Feedback")
        st.write(feedback)
    else:
        st.write("Please enter your problem representation.")
