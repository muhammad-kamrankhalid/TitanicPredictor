import pickle
import streamlit as st
import numpy as np
with open('titanic.pkl','rb') as file:
    model = pickle.load(file)
print(model)

st.set_page_config(page_title="Titanic Survival Predictor", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRADSslXCJcp6j2TbtmiBspCycaG_KSINg9JUcNEUghpj_ezUlEAjvnLarUORl_Om0cUqo&usqp=CAU");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    h1 {
      color: #FF5733 !important;   /* your desired title color */
    }

    /* Change all <p> (st.write/plain text) color */
    p {
      color: blue !important;   /* your desired paragraph color */
    }
    /* Optional: Add white background to the form area for readability */
    div[data-testid="stForm"] {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)




# Input form
with st.form("titanic_form"):
    col1, col2 = st.columns(2)

    with col1:
        st.title("🚢 Titanic Survival Predictor")
        # st.write("Enter passenger details to predict survival probability.")
        pclass = st.selectbox("Passenger Class (Pclass) Ticket class (A or B or C)", [1, 2, 3])
        age = st.number_input("Age", min_value=0.0, max_value=100.0, value=25.0)
        sibsp = st.number_input("Number of Siblings/Spouses Aboard (SibSp)", min_value=0, step=1)
        parch = st.number_input("Number of Parents/Children Aboard (Parch)", min_value=0, step=1)

    with col2:
        fare = st.number_input("Fare Paid", min_value=0.0)
        gender = st.radio("Gender", ["Male", "Female"])
        embarked = st.selectbox("Port of Embarkation (Queesntown, Southampton, Cherbourg)", ["Q", "S", "C"])

    submitted = st.form_submit_button("Predict")

if submitted:
    # Convert categorical to numerical (one-hot encoding)
    male = 1 if gender == "Male" else 0
    Q = 1 if embarked == "Q" else 0
    S = 1 if embarked == "S" else 0

    # Final input format for model
    input_data = np.array([[pclass, age, sibsp, parch, fare, male, Q, S]])

    # Load model and predict (replace with your actual model)
    # model = joblib.load("your_model.joblib")
    prediction = model.predict(input_data)

    # st.success(f"Input vector: {input_data.tolist()[0]}")
    if prediction[0] == 1:
        st.success('Survived')
    else:
        st.error('Not survived')

