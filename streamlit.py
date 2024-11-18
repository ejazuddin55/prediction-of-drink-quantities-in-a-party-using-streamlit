import pandas as pd
import streamlit as st
import joblib
import time

# Load the model and scaler
model = joblib.load('trained_model')
scaler = joblib.load('scaler')

# Streamlit app
st.set_page_config(page_title="Party Planner | Drink Quantity Predictor", layout="wide")
st.title("🎉 Party Planner | Drink Quantity Predictor 🎉")
st.markdown("Welcome to the **Party Planner**! Use this tool to predict the optimal quantities of drinks for your upcoming events.")

# Input fields for user data
with st.form(key='input_form'):
    total_prices = st.number_input("Budget ($)", min_value=0.0, format="%.2f")
    number_of_guests = st.number_input("Number of Guests", min_value=1)
    male_percentage = st.number_input("Male Percentage", min_value=0, max_value=100)
    non_drinkers_perc = st.number_input("Non-drinkers Percentage", min_value=0, max_value=100)
    event_duration = st.number_input("Event Duration (hours)", min_value=1)
    min_age = st.number_input("Max Age", min_value=0)
    max_age = st.number_input("Min Age", min_value=0)

    # Weekend input
    is_weekend = st.selectbox("Is it a Weekend?", options=["No", "Yes"])
    weekend_value = 1 if is_weekend == "Yes" else 0

    # Style of event input
    style_of_event = st.selectbox("Style of Event", [
        "Casual", "Corporate", "Elegant", "Formal", "None specified",
        "Normal style", "Personal", "Pick-up style", "Sit down style",
        "Stylish", "Traditional", "Wedding"
    ])

    # Type of event input
    type_of_event = st.selectbox("Type of Event", ["Wedding", "Other"])
    type_of_event_value = 1 if type_of_event == "Wedding" else 0

    # Submit button for recommendations
    submit_button = st.form_submit_button("Get Recommendations")

# Prepare the input data when the button is clicked
if submit_button:
    # Show a loading spinner while processing
    with st.spinner("Generating recommendations..."):
        time.sleep(2)  # Simulating processing time
        input_data = {
            'total_prices': [total_prices],
            'Number of guests': [number_of_guests],
            'male_percentage': [male_percentage],
            'non_drinkers_perc': [non_drinkers_perc],
            'event_duration': [event_duration],
            'max_age': [max_age],
            'min_age': [min_age],
            'Weekend': [weekend_value],
        }

        # One-hot encode style of event
        style_of_event_dict = {
            'Style of event_Casual': 1 if style_of_event == "Casual" else 0,
            'Style of event_Corporate': 1 if style_of_event == "Corporate" else 0,
            'Style of event_Elegant': 1 if style_of_event == "Elegant" else 0,
            'Style of event_Formal': 1 if style_of_event == "Formal" else 0,
            'Style of event_None specified': 1 if style_of_event == "None specified" else 0,
            'Style of event_Normal style': 1 if style_of_event == "Normal style" else 0,
            'Style of event_Personal': 1 if style_of_event == "Personal" else 0,
            'Style of event_Pick-up style': 1 if style_of_event == "Pick-up style" else 0,
            'Style of event_Sit down style': 1 if style_of_event == "Sit down style" else 0,
            'Style of event_Stylish': 1 if style_of_event == "Stylish" else 0,
            'Style of event_Traditional': 1 if style_of_event == "Traditional" else 0,
            'Style of event_Wedding': 1 if style_of_event == "Wedding" else 0,
        }

        # Add to input data
        input_data.update(style_of_event_dict)
        input_data['Type of event_Wedding'] = [type_of_event_value]

        # Convert to DataFrame
        input_df = pd.DataFrame(input_data)

        # Scale the input features
        input_scaled = scaler.transform(input_df)

        # Make prediction
        predicted_quantities = model.predict(input_scaled)

        # Create a DataFrame to display the results
        predictions_df = pd.DataFrame(predicted_quantities, columns=[
            'SPARKLING CHAMPAGNE', 'PROSECCO', 'SAV & SEM SAV BLANC',
            'PINOT GRIS GRIGIO', 'CHARDONNAY', 'RIESLING', 'MOSCATO',
            'ROSE', 'PINOT NOIR', 'SHIRAZ', 'CAB SAV', 'MERLOT',
            'RED BLENDS', 'Beers', 'Cider', 'Spirits', 'NON ALC'
        ])

        # Display the predicted quantities
        st.write("### Predicted Drink Quantities:")
        st.dataframe(predictions_df)

        # Button to download predictions as CSV
        csv = predictions_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Predictions as CSV",
            data=csv,
            file_name='predicted_drink_quantities.csv',
            mime='text/csv',
            key='download-csv'
        )
