# Import libraries
import streamlit as st
import plotly.express as px

# Import data, this has already been done in the home page.
if "ts_data" in st.session_state:
    ts_df = st.session_state["ts_data"]

# Set page layout to wide for the graphs
st.set_page_config(layout='wide')

# Writing headings and description
st.header('Time-Series Plots.')
st.write('This dataset contains the dates of all the sales. These dates make it easy for us to visualize financial aspects such as the Total Sales, Units Sold and Operating profit.')

# create a selectbox to decide what aspect to display
financial_choice = st.selectbox(
        "Select Financial Aspect",
            ('Total Sales','Units Sold','Operating Profit')
        )

fig = px.line(ts_df, x='Invoice Date', y=financial_choice, color='Retailer')

# Plot the figure
st.write("Click on a Supplier name to disable their data. Double-click to only show the specific supplier's data")
st.plotly_chart(fig, use_container_width=True)