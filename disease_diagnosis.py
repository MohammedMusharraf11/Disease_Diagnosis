import streamlit as st






# Example symptoms for diseases
symptoms = {
    "Flu": ["Fever", "Cough", "Fatigue", "Body Aches"],
    "Common Cold": ["Runny Nose", "Sneezing", "Sore Throat"],
    "COVID-19": ["Fever", "Cough", "Shortness of Breath", "Loss of Taste or Smell"],
    "Allergies": ["Sneezing", "Runny Nose", "Itchy Eyes"],
    "Asthma": ["Shortness of Breath", "Wheezing", "Chest Tightness"],
    "Diabetes": ["Increased Thirst", "Frequent Urination", "Fatigue"],
    "Heart Disease": ["Chest Pain", "Shortness of Breath", "Fatigue"],
    "Migraine": ["Headache", "Nausea", "Sensitivity to Light"],
    "Pneumonia": ["Cough", "Fever", "Shortness of Breath"],
    "Gastroenteritis": ["Diarrhea", "Nausea", "Abdominal Pain"],
    "Urinary Tract Infection (UTI)": ["Frequent Urination", "Burning Sensation", "Cloudy Urine"],
    "Anxiety": ["Restlessness", "Worrying", "Difficulty Concentrating"],
    "Depression": ["Persistent Sadness", "Loss of Interest", "Fatigue"],
    "Arthritis": ["Joint Pain", "Swelling", "Stiffness"],
    "Osteoporosis": ["Bone Pain", "Fractures", "Loss of Height"],
    # Add more diseases and symptoms as needed
}

# Disease diagnosis function
def diagnose_disease(selected_symptoms):
    matched_diseases = [disease for disease, disease_symptoms in symptoms.items() if set(selected_symptoms).issuperset(set(disease_symptoms))]
    return matched_diseases


def diagnose_disease(selected_symptoms):
    for disease, disease_symptoms in symptoms.items():
        if set(selected_symptoms).issuperset(set(disease_symptoms)):
            return [disease]
    return []

# Precaution measures function
def get_precaution_measures(disease):
    # Define precaution measures for each disease (replace with actual measures)
    precautions = {
    "Flu": ["Rest", "Stay hydrated", "Take over-the-counter medications"],
    "Common Cold": ["Rest", "Stay hydrated", "Take over-the-counter medications"],
    "COVID-19": ["Isolate yourself", "Contact healthcare provider", "Follow public health guidelines"],
    "Allergies": ["Avoid allergens", "Use air purifiers", "Take antihistamines"],
    "Asthma": ["Use inhalers as prescribed", "Avoid triggers", "Have an asthma action plan"],
    "Diabetes": ["Monitor blood sugar levels", "Follow a healthy diet", "Take medications as prescribed"],
    "Heart Disease": ["Maintain a healthy diet", "Regular exercise", "Take prescribed medications"],
    "Migraine": ["Identify and avoid triggers", "Manage stress", "Take migraine medications"],
    "Pneumonia": ["Get vaccinated", "Practice good hygiene", "Take prescribed antibiotics"],
    "Gastroenteritis": ["Stay hydrated", "Follow a bland diet", "Rest"],
    "Urinary Tract Infection (UTI)": ["Drink plenty of water", "Take prescribed antibiotics", "Avoid irritants"],
    "Anxiety": ["Practice relaxation techniques", "Seek therapy", "Stay connected with loved ones"],
    "Depression": ["Therapy", "Medications", "Regular exercise"],
    "Arthritis": ["Exercise regularly", "Use joint protection techniques", "Take medications"],
    "Osteoporosis": ["Calcium and vitamin D supplements", "Weight-bearing exercises", "Medications"],
    # Add more diseases and precautions as needed
}
    return precautions.get(disease, ["Precaution measures not available"])

# Streamlit app
def main():
    st.title("Disease Diagnosis App")

    # Get symptoms from user input
    symptoms = st.multiselect("Select your symptoms:",["Fever", "Cough", "Fatigue", "Body Aches", "Runny Nose",
                                                       "Sneezing", "Sore Throat", "Shortness of Breath", "Loss of Taste or Smell",
                                                       "Itchy Eyes", "Wheezing", "Chest Tightness", "Increased Thirst",
                                                       "Frequent Urination", "Chest Pain", "Headache", "Nausea",
                                                       "Sensitivity to Light", "Diarrhea", "Abdominal Pain", "Burning Sensation",
                                                       "Cloudy Urine", "Restlessness", "Worrying", "Difficulty Concentrating",
                                                       "Persistent Sadness", "Loss of Interest", "Joint Pain", "Swelling", "Stiffness",
                                                       "Bone Pain", "Fractures", "Loss of Height"])

    # Diagnose disease
    if st.button("Diagnose"):
        if not symptoms:
            st.warning("Please select at least one symptom.")
        else:
            matched_diseases = diagnose_disease(symptoms)

            # Display diagnosed disease and precautions
            if matched_diseases:
                disease = matched_diseases[0]
                st.success(f"Based on your selected symptoms, it could be {disease} as per my database. However for more accurate its always better to consult a doctor")
                precautions = get_precaution_measures(disease)
                st.subheader(f"Precaution Measures for {disease}:")
                for precaution in precautions:
                    st.write(f"- {precaution}")
            else:
                st.info("No specific diseases matched the selected symptoms. If you have concerns, please consult a healthcare professional.")

if __name__ == "__main__":
    main()
