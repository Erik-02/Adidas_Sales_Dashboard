# Import libraries
import streamlit as st
import pandas as pd

# Set page layout to wide for the graphs
st.set_page_config(layout='wide')

# Writing headings and description
st.header('Adidas Sales Dataset analysis and Prediction.')
st.write('Main page')

# create function to read the data in
@st.cache_data
def read_data():
    # Read in data
    df = pd.read_csv('https://raw.githubusercontent.com/Erik-02/Adidas_Sales_Dashboard/main/Adidas%20US%20Sales%20Data.csv')
    # Data preprocessing
    # Drop unnnecessary columns
    df.drop(columns=['Unnamed: 0','Retailer ID'], inplace=True)

    # Create a dataframe for time series plots
    ts_df = df.groupby(['Retailer','Invoice Date'])[['Total Sales', 'Units Sold', 'Operating Profit']].sum()
    ts_df = ts_df.reset_index()

    return df, ts_df

df, ts_df = read_data()

# Set data variable to be used across all pages
st.session_state["data"] = df
st.session_state["ts_data"] = ts_df
