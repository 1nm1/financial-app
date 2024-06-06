import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

import streamlit as st
import pandas as pd

# Title and description
st.title("Personal Finance Manager")
st.write("Manage your income, expenses, and budgets effectively.")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Income Tracker", "Expense Tracker", "Budget Planner", "Reports"])

# Placeholder for data storage
if 'income_data' not in st.session_state:
    st.session_state['income_data'] = pd.DataFrame(columns=['Date', 'Source', 'Amount'])

if 'expense_data' not in st.session_state:
    st.session_state['expense_data'] = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

# Dashboard
if page == "Dashboard":
    st.header("Dashboard")
    st.write("Overview of your financial status.")

    # Example charts and summaries
    st.subheader("Total Income")
    st.write(st.session_state['income_data']['Amount'].sum())
    st.subheader("Total Expenses")
    st.write(st.session_state['expense_data']['Amount'].sum())

# Income Tracker
elif page == "Income Tracker":
    st.header("Income Tracker")
    st.write("Log and view your income sources.")

    with st.form("income_form"):
        date = st.date_input("Date")
        source = st.text_input("Source")
        amount = st.number_input("Amount", min_value=0.0)
        submit = st.form_submit_button("Add Income")
        if submit:
            st.session_state['income_data'] = st.session_state['income_data'].append(
                {'Date': date, 'Source': source, 'Amount': amount}, ignore_index=True)
            st.success("Income added!")

    st.write(st.session_state['income_data'])

# Expense Tracker
elif page == "Expense Tracker":
    st.header("Expense Tracker")
    st.write("Log and categorize your expenses.")

    with st.form("expense_form"):
        date = st.date_input("Date")
        category = st.text_input("Category")
        amount = st.number_input("Amount", min_value=0.0)
        submit = st.form_submit_button("Add Expense")
        if submit:
            st.session_state['expense_data'] = st.session_state['expense_data'].append(
                {'Date': date, 'Category': category, 'Amount': amount}, ignore_index=True)
            st.success("Expense added!")

    st.write(st.session_state['expense_data'])

# Budget Planner
elif page == "Budget Planner":
    st.header("Budget Planner")
    st.write("Set and monitor your budget goals.")

    # Example budget setting
    budget = st.number_input("Set your monthly budget", min_value=0.0)
    st.write(f"Your monthly budget is set to {budget}")

# Reports
elif page == "Reports":
    st.header("Reports")
    st.write("Generate and view monthly/annual financial reports.")

    # Example report generation
    st.write("Coming soon!")
