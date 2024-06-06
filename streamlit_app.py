import streamlit as st
import pandas as pd

# Title and description
st.title("Personal Finance Manager")
st.write("Manage your income, debits, and monthly budget effectively.")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Income & Debits", "Monthly Planner", "Reports"])

# Placeholder for data storage
if 'income_data' not in st.session_state:
    st.session_state['income_data'] = pd.DataFrame(columns=['Date', 'Description', 'Amount'])

if 'debit_data' not in st.session_state:
    st.session_state['debit_data'] = pd.DataFrame(columns=['Date', 'Description', 'Amount'])

# Dashboard
if page == "Dashboard":
    st.header("Dashboard")
    st.write("Overview of your financial status.")

    # Summary of income and debits
    st.subheader("Total Income")
    st.write(st.session_state['income_data']['Amount'].sum())
    
    st.subheader("Total Debits")
    st.write(st.session_state['debit_data']['Amount'].sum())

    # Display data
    st.subheader("Income Data")
    st.write(st.session_state['income_data'])
    
    st.subheader("Debit Data")
    st.write(st.session_state['debit_data'])

# Income & Debits
elif page == "Income & Debits":
    st.header("Income & Debits")
    st.write("Log your income and debits.")

    # Income Form
    with st.form("income_form"):
        st.subheader("Log Income")
        income_date = st.date_input("Date", key="income_date")
        income_desc = st.text_input("Description", key="income_desc")
        income_amount = st.number_input("Amount", min_value=0.0, key="income_amount")
        income_submit = st.form_submit_button("Add Income")
        if income_submit:
            new_income = {'Date': income_date, 'Description': income_desc, 'Amount': income_amount}
            st.session_state['income_data'] = st.session_state['income_data'].append(new_income, ignore_index=True)
            st.success("Income added!")

    # Debit Form
    with st.form("debit_form"):
        st.subheader("Log Debit")
        debit_date = st.date_input("Date", key="debit_date")
        debit_desc = st.text_input("Description", key="debit_desc")
        debit_amount = st.number_input("Amount", min_value=0.0, key="debit_amount")
        debit_submit = st.form_submit_button("Add Debit")
        if debit_submit:
            new_debit = {'Date': debit_date, 'Description': debit_desc, 'Amount': debit_amount}
            st.session_state['debit_data'] = st.session_state['debit_data'].append(new_debit, ignore_index=True)
            st.success("Debit added!")

# Monthly Planner
elif page == "Monthly Planner":
    st.header("Monthly Planner")
    st.write("Plan your monthly finances.")

    if 'monthly_budget' not in st.session_state:
        st.session_state['monthly_budget'] = 0.0
    
    budget = st.number_input("Set your monthly budget", min_value=0.0, value=st.session_state['monthly_budget'])
    st.session_state['monthly_budget'] = budget
    st.write(f"Your monthly budget is set to {budget}")

    st.subheader("Monthly Summary")
    total_income = st.session_state['income_data']['Amount'].sum()
    total_debits = st.session_state['debit_data']['Amount'].sum()
    net_savings = total_income - total_debits
    budget_balance = budget - total_debits
    
    st.write(f"Total Income: {total_income}")
    st.write(f"Total Debits: {total_debits}")
    st.write(f"Net Savings: {net_savings}")
    st.write(f"Budget Balance: {budget_balance}")

# Reports
elif page == "Reports":
    st.header("Reports")
    st.write("Generate and view monthly/annual financial reports.")
    
    # Placeholder for future implementation
    st.write("Coming soon!")