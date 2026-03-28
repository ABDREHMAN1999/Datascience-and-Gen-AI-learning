import streamlit as st
import pandas as pd


import pandas as pd
data = {
    "Order_ID": range(1, 21),
    "Customer": ["Amit", "Sara", "John", "Priya", "Ali", "Ravi", "Neha", "David", "Zara", "Karan",
                 "Amit", "Sara", "John", "Priya", "Ali", "Ravi", "Neha", "David", "Zara", "Karan"],
    "City": ["Mumbai", "Delhi", "Bangalore", "Mumbai", "Delhi",
             "Chennai", "Bangalore", "Mumbai", "Delhi", "Chennai",
             "Mumbai", "Delhi", "Bangalore", "Mumbai", "Delhi",
             "Chennai", "Bangalore", "Mumbai", "Delhi", "Chennai"],
    "Category": ["Electronics", "Clothing", "Electronics", "Groceries", "Clothing",
                 "Groceries", "Electronics", "Clothing", "Groceries", "Electronics",
                 "Clothing", "Electronics", "Groceries", "Clothing", "Electronics",
                 "Groceries", "Clothing", "Electronics", "Groceries", "Clothing"],
    "Amount": [1200, 800, 1500, 600, 900, 400, 2000, 1100, 700, 1300,
               1000, 1400, 500, 900, 1600, 300, 1200, 1800, 650, 950],
    "Rating": [4, 5, 3, 4, 2, 5, 4, 3, 4, 5,
               2, 4, 3, 5, 4, 3, 5, 4, 2, 5]
}
df = pd.DataFrame(data)


st.sidebar.header("Filters")
with st.sidebar:
    cities = st.multiselect("Select City", options = df["City"].unique())
    categories = st.multiselect("Select Category", options = df["Category"].unique())
    min_amount , max_amount = st.slider("Select Amount Range", df["Amount"].min(), df["Amount"].max(), (0,3000))
    sort_by = st.selectbox("Sort Data by", options= ["Lower to Higher", "Higher to lower"])
    
st.title("Sales Dashboard")
search_customer = st.text_input("Enter Customer name: ")

if cities:
    df = df[df["City"].isin(cities)]
if categories:
    df = df[df["Category"].isin(categories)]
if min_amount>=0 and max_amount<=3000:
    df = df[(df["Amount"]>= min_amount) & (df["Amount"]<=max_amount)]
if search_customer:
    df = df[df["Customer"].str.contains(search_customer, case=False)]
if sort_by=="Lower to Higher":
    df = df.sort_values(by='Amount', ascending=True)
elif sort_by=="Higher to lower":
    df = df.sort_values(by='Amount', ascending=False)
st.write(df)
    
col1 , col2 , col3 = st.columns(3)
col1.metric("Total Sales", df["Amount"].sum())
col2.metric("Total orders", len(df["Order_ID"]))
col3.metric('Average Rating', df["Rating"].mean())