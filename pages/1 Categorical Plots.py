# Import Libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Import data, this has already been done in the home page.
if "data" in st.session_state:
    df = st.session_state["data"]

# Set page layout to wide for the graphs
st.set_page_config(layout='wide')

# Writing headings and description
st.header('Categorical Plots.')
st.write('Our data is the recorded sales at specific times over the last few years. The data can be classified into various categories such as the Retailer, Region, Product and Sales method. We can visualize these aspects easily according to financial aspects such as Units Sold, Total Sales and Operating Profit.')

# Initialize columns
business_aspect, financial_aspect = st.columns([5,5])

# Create select boxes
with business_aspect:
        business_choice = st.selectbox(
        "Select Business Aspect",
            ('Retailer','Region', 'Product', 'Sales Method')
        )
        
with financial_aspect:
        financial_choice = st.selectbox(
        "Select Financial Aspect",
            ('Units Sold','Total Sales','Operating Profit')
        )

# Create a figure to plot
fig = px.histogram(df, x=business_choice, y=financial_choice, text_auto=True)

# Plot the figure
st.plotly_chart(fig, use_container_width=True)