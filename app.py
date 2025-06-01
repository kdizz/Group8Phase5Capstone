
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import warnings
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error

warnings.filterwarnings('ignore')

st.title("Time Series Forecasting with LSTM")

# Load datasets
st.subheader("Loading Datasets")

dfmonthly = pd.read_csv("final_a.csv")
dfclosing = pd.read_csv("Closing_date.csv")
dfopening = pd.read_excel("yearly opening.xlsx")
dfaverage = pd.read_csv("Yearly_ava.csv")

# Show dataset shapes
st.write("Monthly Data Shape:", dfmonthly.shape)
st.write("Yearly Average Data Shape:", dfaverage.shape)

# Display info
buffer = io.StringIO()
dfmonthly.info(buf=buffer)
st.text("Monthly Data Info:")
st.text(buffer.getvalue())

buffer = io.StringIO()
dfaverage.info(buf=buffer)
st.text("Yearly Average Data Info:")
st.text(buffer.getvalue())

# Check for missing values
st.subheader("Missing Values")
st.write("Monthly:", dfmonthly.isnull().sum())
st.write("Yearly Average:", dfaverage.isnull().sum())

# Check for duplicates
st.subheader("Duplicate Rows")
for name, df in zip(['dfmonthly', 'dfaverage', 'dfclosing', 'dfopening'],
                    [dfmonthly, dfaverage, dfclosing, dfopening]):
    st.write(f"{name}: {df.duplicated().sum()} duplicate rows")

# Modeling section
st.subheader("LSTM Modeling on Monthly Data")

# Assume target column is 'Total_cases' and date column is 'Month'
df = dfmonthly.copy()
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)

# Select target column
target_column = 'Total_cases'
if target_column not in df.columns:
    st.error(f"Column '{target_column}' not found in dataset.")
else:
    series = df[[target_column]]
    st.line_chart(series)

    # Normalize
    scaler = MinMaxScaler()
    scaled_series = scaler.fit_transform(series)

    # Create sequences
    def create_dataset(data, time_step=12):
        X, y = [], []
        for i in range(len(data) - time_step):
            X.append(data[i:i+time_step])
            y.append(data[i+time_step])
        return np.array(X), np.array(y)

    time_step = 12
    X, y = create_dataset(scaled_series, time_step)

    # Split
    train_size = int(len(X) * 0.8)
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Reshape for LSTM
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

    # Build model
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(time_step, 1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')

    # Train model
    model.fit(X_train, y_train, epochs=10, batch_size=1, verbose=0)

    # Predict and inverse transform
    y_pred = model.predict(X_test)
    y_pred_inv = scaler.inverse_transform(y_pred)
    y_test_inv = scaler.inverse_transform(y_test)

    # Plot predictions
    fig, ax = plt.subplots()
    ax.plot(y_test_inv, label='Actual')
    ax.plot(y_pred_inv, label='Predicted')
    ax.set_title('Actual vs Predicted')
    ax.legend()
    st.pyplot(fig)

    # Show RMSE
    rmse = np.sqrt(mean_squared_error(y_test_inv, y_pred_inv))
    st.write("Root Mean Squared Error:", rmse)
