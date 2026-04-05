import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Expense Tracker")
if "expenses" not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=["Amount","Category","Date"])
amount = st.number_input("Enter amount")
category = st.selectbox("Select category",["Food","Travel","Shopping","Entertainment","Bill"])
date = st.date_input("Select date")
if st.button("Add Expenses"):
    new_data = pd.DataFrame({
        "Amount":[amount],
        "Category":[category],
        "Date":[date]
    })
    st.session_state.expenses = pd.concat(
        [st.session_state.expenses,new_data],
        ignore_index=True
    )
st.subheader("All Expenses")
st.dataframe(st.session_state.expenses)
st.subheader("Delete Expenses")
if not st.session_state.expenses.empty:
    index = st.number_input("Enter index to delete",min_value=0,step=1)
    if st.button("Delete"):
        st.session_state.expenses = st.session_state.expenses.drop(index).reset_index(drop=True)
        st.success("Deleted succesfully")
total = st.session_state.expenses["Amount"].sum()
st.subheader(f"Total Spending:{total}")
if not st.session_state.expenses.empty:
    category_sum = st.session_state.expenses.groupby("Category")["Amount"].sum()
    fig, ax = plt.subplots()
    category_sum.plot(kind="bar",ax=ax)
    st.subheader("Expenses by Category")
    st.pyplot(fig)