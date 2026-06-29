import streamlit as st
password = st.text_input("enter password",type="password")

if st.button("Validate"):
    upper=lower=digit=special=False
    for ch in password:
        if ch.isupper():
            upper=True
        elif ch.islower():
            lower=True
        elif ch.isdigit():
            digit=True
        else:
            special=True
    if len(password)>=8 and upper and lower and digit and special:
        
        st.success("Strong password...Thank you!")
    else: 
        st.error("Invalid password...Sorry!")
        if len(password)<0:
            st.write("password must contain atleast 8 characters")
        if not upper:
            st.write(" It should contain upper case ")
        if not lower:
            st.write("It should contain lower case")
        if not digit:
            st.write(" It should contain digit")
        if not special:
            st.write(" It should contain special characters")
        