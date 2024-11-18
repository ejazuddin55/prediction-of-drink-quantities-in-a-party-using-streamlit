# Prediction of  drink quantities in a party using streamlit

This Streamlit app serves as a tool to predict optimal drink quantities for events, leveraging a machine learning model. Here's an overview of its structure and functionality:

Key Features:
User Inputs:

Budget: Total event budget.
Number of Guests: Number of attendees.
# Demographics:
Gender distribution, percentage of non-drinkers, age range.
Event Duration: Hours for which the event will last.
Event Type: Weekend or not, style of the event, type of event (wedding or other).
Backend Processing:

# Scaling:
Uses scaler.pkl to standardize inputs before feeding them into the model.
Prediction: A pre-trained model (trained_model.pkl) predicts drink quantities based on the input features.
One-Hot Encoding: Encodes categorical variables like style_of_event and type_of_event for model compatibility.
# Output:

Predicted quantities of various drinks, displayed as a DataFrame.
Option to download predictions in CSV format for further analysis or record-keeping.
User Experience:

# Responsive UI: 
Uses a form for user input and a spinner for processing, enhancing usability.
Data Download: Provides a button to download predictions as a CSV file.
# Improvements to Consider:

Validation: Add validation to ensure consistent logic (e.g., min_age ≤ max_age).
Dynamic Input Handling: Make event-specific fields appear dynamically based on type of event.
Error Handling: Handle scenarios where input data fails to scale or predict due to unseen categories or missing data.
Enhanced Outputs: Include visuals like bar charts or pie charts for drink distribution.
