import streamlit as st

# Title of the app
st.title("Simple Calculator by Ihsan Ullah")

# Input numbers
num1 = st.number_input("Enter the first number:", value=0)
num2 = st.number_input("Enter the second number:", value=0)

# Select operation
operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Perform the calculation
if operation == "Add":
    result = num1 + num2
    st.write(f"**Result: {num1} + {num2} = {result}**")
elif operation == "Subtract":
    result = num1 - num2
    st.write(f"**Result: {num1} - {num2} = {result}**")
elif operation == "Multiply":
    result = num1 * num2
    st.write(f"**Result: {num1} * {num2} = {result}**")
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
        st.write(f"**Result: {num1} / {num2} = {result}**")
    else:
        st.write("**Error: Cannot divide by zero.**")


