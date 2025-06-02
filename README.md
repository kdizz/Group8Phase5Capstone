# Group8Phase5Capstone

## DATA-DRIVEN STUDY OF KENYA’S EXCHANGE RATE DYNAMICS UNDERSTANDING THE FORCES SHAPING KENYA’S CURRENCY VALUATIONS

![image](https://github.com/user-attachments/assets/365825c9-11de-477f-a715-a436cd14d563)

## Navigating the Repository

There are a total of 6 branches (main, saron, bruce, audrey, patience, Khadija). The entire and final complete project is in the main branch. The other branches were created for task allocation for the group members; however due to constraints, we abandoned the branches and worked together fully on the main branch. 

The models are connencted to the notebook containing EDA; i.e. any notebook that is titled 'Main project plus...' will include similar work on the inital pages, however the models shall be towards the bottom, this was done due to compatibility issues brought about by tensorflow and other package incompatibilities, thus we couldn't run the notebooks when merged into a single notebook. ARIMA is the only model that was hosted separately.

*********************************************************************************

## Project Introduction

Exchange rates play a critical role in shaping the economic landscape of nations, influencing trade, investment, and overall economic stability. This project adopts an exploratory approach to examine how various factors impact the movements of Kenya’s exchange rate, specifically focusing on the USD/KES pair. The primary objective is to conduct a comprehensive exploratory data analysis (EDA) of the USD/KES exchange rate from 2003 to 2023, with the aim of identifying significant trends, seasonal patterns, and decomposing the time series to understand underlying structures. Additionally, the project seeks to develop and compare time series forecasting models to predict exchange rate movements for the year 2024 and validate these predictions against actual data from the same year. Another key objective is to apply supervised learning techniques to detect distinct volatility or trend regimes within the USD/KES exchange rate data, enabling a more nuanced understanding of its behavior over time. Finally, the study aims to identify and analyze macroeconomic indicators that have the most significant influence on exchange rate fluctuations, offering insights into the key drivers of currency dynamics in the Kenyan context.

## Packages used

EDA : numpy, pandas, matplotlib, seaborn, warnings, 

Modelling : sklearn.metrics, ExponentialSmoothing from statsmodels.tsa.holtwinters, MinMaxScaler from sklearn.preprocessing, Sequential from tensorflow.keras.models, Dense, LSTM, Dropout from tensorflow.keras.layers, SARIMAX from statsmodels.tsa.statespace.sarimax, adfuller from statsmodels.tsa.stattools, pmdarima, Prophet, plot_acf, plot_pacf from statsmodels.graphics.tsaplots. 

Deployment : Streamlit

*********************************************************************************

## KEY INSIGHTS (GRAPHS SHOWING KEY RELATIONSHIPS)

![image](https://github.com/user-attachments/assets/9fb17af5-f078-4b4e-8bb6-26a9b5e7073c)

![image](https://github.com/user-attachments/assets/ea9b1d30-5682-468d-8748-780a3a4f8d6c)

![image](https://github.com/user-attachments/assets/28e8956e-eb4c-49e3-8ef4-22f6fda9bfa7)

![image](https://github.com/user-attachments/assets/e9a93bbd-d226-45ea-9072-4e0fc387211e)

![image](https://github.com/user-attachments/assets/558c0304-db31-4c7c-a6d9-e2c5b4beffd3)

![image](https://github.com/user-attachments/assets/9e1b219c-eda8-44aa-8a3e-f11c5df3913e)

Correlation matrix showing how all selected features are interrelated.

*********************************************************************************

## MODEL RESULTS PLOTTED

## PROPHET 

![image](https://github.com/user-attachments/assets/34570a22-a91a-4372-baa4-2d4d406d5913)

## MOVING AVERAGE

![image](https://github.com/user-attachments/assets/4b8917e9-01b6-4f68-a3aa-bec567a68037)

## LSTM

![image](https://github.com/user-attachments/assets/e145b1ca-ebee-4970-b5bd-0f0ce51204f9)

## EXPONENTIAL SMOOTHING

![image](https://github.com/user-attachments/assets/3ad28341-0f9b-45fa-a2e6-0b06579d9d6b)

## ARIMA

![image](https://github.com/user-attachments/assets/32f6c4e5-239e-485a-9db1-19a8bf78d8a0)

*********************************************************************************

## CONCLUSION

From our exploratory analysis, we came to the conclusion that the following features have the most influence on/are influenced by the exchange rate;

i. Imports & Exports

ii. IBRD Loans & IDA Credits

iii. Unemployment

iv. Bank Deposit Rate

v. Savings

vi. Total Debt

vii. Total Remittances

For a future and ongoing analysis after this one, the above would be the key features to consider in the analysis. 

Models

We have deployed links for all the models, however, we highly suggest using the LSTM and Moving Average models as these had the best forecasts. They are hosted on Streamlit.

*********************************************************************************
