import streamlit as st
import pandas as pd 
st.title("Simple Dashboard with filters")

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["Mumbai", "Delhi", "Mumbai", "Bangalore", "Delhi"],
    "Salary": [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)

st.sidebar.header('Filters')
selected_city = st.sidebar.multiselect("Select City", options = df["City"].unique())
min_age, max_age = st.sidebar.slider(
    "Select Age Range",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (25, 40)
)


st.subheader("All Data: ")
st.write(df)
st.subheader("Filtered Data: ")

st.write(df[
    (df["City"].isin(selected_city)) &
    (df["Age"]>= min_age) & 
    (df["Age"]<= max_age)   
])