import pandas as pd 
import streamlit as st 
import numpy as np

np.random.seed(42)

data = {
    "Order_ID": range(1, 101),
    "Customer_Name": np.random.choice(["Amit", "Sara", "John", "Priya", "Ali", "Ravi", "Neha", "David"], 100),
    "City": np.random.choice(["Mumbai", "Delhi", "Bangalore", "Hyderabad"], 100),
    "Category": np.random.choice(["Electronics", "Clothing", "Home", "Sports"], 100),
    "Product": np.random.choice(["Laptop", "T-shirt", "Sofa", "Cricket Bat", "Mobile", "Shoes"], 100),
    "Quantity": np.random.randint(1, 5, 100),
    "Price": np.random.randint(500, 5000, 100),
    "Order_Date": pd.date_range(start="2024-01-01", periods=100, freq="D")
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Quantity"] * df["Price"]

with st.sidebar:
    st.header('Filters')
    city = st.multiselect("Select City", options = df["City"].unique())
    category = st.multiselect("Select Category", options = df["Category"].unique())
    st.date_input(
    "Select Date Range",
    [df["Order_Date"].min(), df["Order_Date"].max()]
)
    
    
if city: 
    df = df[df["City"].isin(city)]
if category:
    df = df[df["Category"].isin(category)]
if True:
    df = df[(df["Order_Date"]>=df["Order_Date"].min()) & (df["Order_Date"]<= df["Order_Date"].max())]

st.title('Sales Dashboard')
c1 , c2 , c3 = st.columns(3)

with c1:
    total_revenue = df["Total_Sales"].sum()
    st.metric("Total Revenue", f"₹{total_revenue:,.0f}")
with c2:
    Total_orders = len(df["Order_ID"])
    st.metric('Total Orders', Total_orders)
with c3:
    average_order_value = df['Total_Sales'].sum() / df['Order_ID'].nunique()
    st.metric("Average Order Value", f"₹{average_order_value}")
st.write(df)

    
c4 , c5 = st.columns(2)
with c4:
    with st.container(border = True):
        st.subheader("Revenue by category")
        st.bar_chart(df.groupby('Category')["Total_Sales"].sum())
        
df_time = df.groupby("Order_Date")["Total_Sales"].sum().reset_index()
df_time = df_time.set_index("Order_Date")
df_time = df_time.asfreq("D", fill_value=0)
with c5: 
    with st.container(border=True):
        st.subheader('Revenue over time')
        st.line_chart(df_time)
        


