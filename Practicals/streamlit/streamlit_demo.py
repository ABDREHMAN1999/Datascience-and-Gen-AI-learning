import streamlit as st
st.set_page_config(
    page_icon =  "🚀",
    page_title = "Streamlit Demo"
)
st.title("Book Your Tickets Now")
st.subheader("Welcome to tourism India")
t1 , t2 , t3 = st.tabs(["Home", "Dashboard", "Settings"])
with t1:
    st.write("Welcome to your homepage")
    c1 , c2 = st.columns(2)
    with c1:
        st.write("This is column1 in homepage")
        name= st.text_input('Enter your name: ')
        button_name = st.button("Submit", type= "primary", key = "button_name")
        if button_name:
            st.write(f"Hello {name} nice to meet you, please enter your email now.")
        
    with c2:
        st.write("This is column2 in homepage")
        email = st.text_input("Enter your email: ")
        button_email = st.button("Submit", type = "primary", key= "button_email")
        if button_email:
            st.write(f"A verification email has been sent to {email} please use the link to activate your account")
    st.divider()
    
    st.subheader("OUR TOURISM BROUCHER: ")
    with st.container(border = True, height = 200):
        st.write('List of famous places to visit: ')
        for i in range(50):
            st.write(f'Place {i}')
    st.divider()
    st.link_button('Ministry of tourism', "https://tourism.gov.in/", type = "primary")
    
    st.divider()
    import datetime
    date = datetime.date.today()
    st.subheader("Date input")
    start_date = st.date_input('start date')
    end_date = st.date_input("End date",date)
    st.divider()
    st.subheader('Enter your plan: ')
    plan = st.file_uploader("Upload your plan", type=["txt", "csv"])
    if plan:
        import pandas as pd
        df = pd.read_csv(plan)
        st.write(df)
        
        
        
