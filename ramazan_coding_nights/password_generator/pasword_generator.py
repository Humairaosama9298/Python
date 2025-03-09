import streamlit as st 
import random
import string

# Function to generate the password
def generate_pasword(length, use_digits, use_special):    
    character = string.ascii_letters    # Include letters with this method

    # Add digits if selected
    if use_digits:    
        character += string.digits

    # Add special characters if selected
    if use_special:     
        character += string.punctuation

    # Generate the password by randomly choosing characters
    return ''.join(random.choice(character) for _ in range(length)) 

# Title of the Streamlit app
st.title("Password Generator") 

# Slider to select password length
length = st.slider("Select Password Length", min_value=8, max_value=35, value=12)

# Checkbox to include digits
use_digits = st.checkbox("Include Digits")

# Checkbox to include special characters
use_special = st.checkbox("Include Special Characters")

# Generate password on button click
if st.button("Generate Password"):
    password = generate_pasword(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")

st.write("---------------------")



st.write("Build With 💖 by [Humaira Osama](https://github.com/Humairaosama9298)")
