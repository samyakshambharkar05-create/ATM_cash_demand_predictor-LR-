import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load the trained model
# Assuming 'atm_cash_predictor.pkl' is in the same directory
with open('atm_cash_predictor.pkl', 'rb') as file:
    lr = pickle.load(file)

# Re-load the original dataset to fit LabelEncoders
# This ensures the encoders have the correct mappings
# Make sure the path matches your dataset location
df_original = pd.read_csv("/content/drive/MyDrive/AI ML Projects/ATM_cash_demand/atm_cash_management_dataset.csv")

# Preprocessing steps identical to training
df_original['Date'] = pd.to_datetime(df_original['Date'])
df_original['Month'] = df_original['Date'].dt.month
df_original['Day'] = df_original['Date'].dt.day
df_original['Year'] = df_original['Date'].dt.year

categorical_cols = [
    'ATM_ID',
    'Day_of_Week',
    'Time_of_Day',
    'Location_Type',
    'Weather_Condition'
]

encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    # Fit encoder on the unique values of the original column
    le.fit(df_original[col])
    encoders[col] = le

# Define the order of features as used in training (from X_train.columns)
feature_order = ['ATM_ID', 'Day_of_Week', 'Time_of_Day', 'Total_Withdrawals', 'Total_Deposits',
                 'Location_Type', 'Holiday_Flag', 'Special_Event_Flag', 'Previous_Day_Cash_Level',
                 'Weather_Condition', 'Nearby_Competitor_ATMs', 'Month', 'Day', 'Year']

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("ATM Cash Demand Predictor"),

    html.Div([
        html.Label("ATM ID:"),
        dcc.Dropdown(
            id='atm-id-input',
            options=[{'label': i, 'value': i} for i in encoders['ATM_ID'].classes_],
            placeholder="Select ATM ID"
        )
    ], style={'width': '48%', 'display': 'inline-block', 'margin-right': '4%'}),

    html.Div([
        html.Label("Day of Week:"),
        dcc.Dropdown(
            id='day-of-week-input',
            options=[{'label': i, 'value': i} for i in encoders['Day_of_Week'].classes_],
            placeholder="Select Day of Week"
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Time of Day:"),
        dcc.Dropdown(
            id='time-of-day-input',
            options=[{'label': i, 'value': i} for i in encoders['Time_of_Day'].classes_],
            placeholder="Select Time of Day"
        )
    ], style={'width': '48%', 'display': 'inline-block', 'margin-right': '4%'}),

    html.Div([
        html.Label("Location Type:"),
        dcc.Dropdown(
            id='location-type-input',
            options=[{'label': i, 'value': i} for i in encoders['Location_Type'].classes_],
            placeholder="Select Location Type"
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Weather Condition:"),
        dcc.Dropdown(
            id='weather-condition-input',
            options=[{'label': i, 'value': i} for i in encoders['Weather_Condition'].classes_],
            placeholder="Select Weather Condition"
        )
    ], style={'width': '48%', 'display': 'inline-block', 'margin-right': '4%'}),

    html.Div([
        html.Label("Total Withdrawals:"),
        dcc.Input(id='total-withdrawals-input', type='number', value=0, placeholder="Enter Total Withdrawals")
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Total Deposits:"),
        dcc.Input(id='total-deposits-input', type='number', value=0, placeholder="Enter Total Deposits")
    ], style={'width': '48%', 'display': 'inline-block', 'margin-right': '4%'}),

    html.Div([
        html.Label("Holiday Flag (0=No, 1=Yes):"),
        dcc.Dropdown(
            id='holiday-flag-input',
            options=[{'label': 'No', 'value': 0}, {'label': 'Yes', 'value': 1}],
            value=0
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Special Event Flag (0=No, 1=Yes):"),
        dcc.Dropdown(
            id='special-event-flag-input',
            options=[{'label': 'No', 'value': 0}, {'label': 'Yes', 'value': 1}],
            value=0
        )
    ], style={'width': '48%', 'display': 'inline-block', 'margin-right': '4%'}),

    html.Div([
        html.Label("Previous Day Cash Level:"),
        dcc.Input(id='previous-day-cash-level-input', type='number', value=0, placeholder="Enter Previous Day Cash Level")
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Nearby Competitor ATMs:"),
        dcc.Input(id='nearby-competitor-atms-input', type='number', value=0, placeholder="Enter Nearby Competitor ATMs")
    ], style={'width': '48%', 'display': 'inline-block', 'margin-right': '4%'}),

    html.Div([
        html.Label("Month (1-12):"),
        dcc.Input(id='month-input', type='number', value=1, min=1, max=12, placeholder="Enter Month")
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Day (1-31):"),
        dcc.Input(id='day-input', type='number', value=1, min=1, max=31, placeholder="Enter Day")
    ], style={'width': '48%', 'display': 'inline-block', 'margin-right': '4%'}),

    html.Div([
        html.Label("Year:"),
        dcc.Input(id='year-input', type='number', value=2024, min=2000, max=2050, placeholder="Enter Year")
    ], style={'width': '48%', 'display': 'inline-block'}),

    html.Button('Predict Cash Demand', id='predict-button', n_clicks=0, style={'margin-top': '20px'}),

    html.Div(id='prediction-output', style={'margin-top': '20px', 'font-size': '20px'})
])

# Define the callback function
@app.callback(
    Output('prediction-output', 'children'),
    [Input('predict-button', 'n_clicks')],
    [
        State('atm-id-input', 'value'),
        State('day-of-week-input', 'value'),
        State('time-of-day-input', 'value'),
        State('total-withdrawals-input', 'value'),
        State('total-deposits-input', 'value'),
        State('location-type-input', 'value'),
        State('holiday-flag-input', 'value'),
        State('special-event-flag-input', 'value'),
        State('previous-day-cash-level-input', 'value'),
        State('weather-condition-input', 'value'),
        State('nearby-competitor-atms-input', 'value'),
        State('month-input', 'value'),
        State('day-input', 'value'),
        State('year-input', 'value')
    ]
)
def update_prediction(
    n_clicks,
    atm_id,
    day_of_week,
    time_of_day,
    total_withdrawals,
    total_deposits,
    location_type,
    holiday_flag,
    special_event_flag,
    previous_day_cash_level,
    weather_condition,
    nearby_competitor_atms,
    month,
    day,
    year
):
    if n_clicks > 0:
        # Encode categorical features using the fitted encoders
        try:
            encoded_atm_id = encoders['ATM_ID'].transform([atm_id])[0]
            encoded_day_of_week = encoders['Day_of_Week'].transform([day_of_week])[0]
            encoded_time_of_day = encoders['Time_of_Day'].transform([time_of_Day])[0]
            encoded_location_type = encoders['Location_Type'].transform([location_type])[0]
            encoded_weather_condition = encoders['Weather_Condition'].transform([weather_condition])[0]
        except ValueError as e:
            return f"Error encoding categorical features: {e}. Please ensure all dropdowns are selected."

        # Create a DataFrame for prediction, ensuring column order matches training data
        input_data = pd.DataFrame([[encoded_atm_id,
                                      encoded_day_of_week,
                                      encoded_time_of_day,
                                      total_withdrawals,
                                      total_deposits,
                                      encoded_location_type,
                                      holiday_flag,
                                      special_event_flag,
                                      previous_day_cash_level,
                                      encoded_weather_condition,
                                      nearby_competitor_atms,
                                      month,
                                      day,
                                      year]], columns=feature_order)

        # Make prediction
        prediction = lr.predict(input_data)[0]
        return f"Predicted Cash Demand Next Day: ${prediction:,.2f}"
    return "Enter values and click 'Predict Cash Demand'"

if __name__ == '__main__':
    # Use mode='inline' for running directly in Google Colab
    # For local execution, remove mode='inline' or set to None
    app.run_server(debug=True, mode='inline', port=8050)
