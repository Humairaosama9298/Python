import streamlit as st
import random
import string
import re

# Page styling
st.set_page_config(page_title="Password Generator & Strength Meter")

# Custom CSS
st.markdown("""
    <style>
        html, body, .main {
            background-color: #000f00;
            color: white;
            text-align: center;
        }
        .stTextInput {
            width: 60% !important;
            margin: auto;
        }
        .stButton button {
            width: 30%;
            background-color: #000f00;
            color: white;
            font-size: 18px;
            display: block;
            margin: 20px auto;
        }
        .stButton button:hover {
            background-color: #0000ff;
            color: white;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the Streamlit app
st.title("🔐 Password Generator and Strength Checker")

# Slider to select password length
length = st.slider("Select Password Length", min_value=8, max_value=35, value=12)

# Checkbox to include digits and special characters
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

# Function to generate the password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Include letters

    # Add digits if selected
    if use_digits:
        characters += string.digits

    # Add special characters if selected
    if use_special:
        characters += string.punctuation

    # Generate the password by randomly choosing characters
    return ''.join(random.choice(characters) for _ in range(length))

# Generate password on button click
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")

# Function to check password strength
def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both uppercase and lowercase letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*()]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one special character (!@#$%^&*())**.")

    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

    if feedback:
        with st.expander("**Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Input for password strength check
st.write("\n")
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong")

# Button to check password strength
if st.button("Check Strength"):
    if password:
        check_password(password)
    else:
        st.write("⚠️ Please enter a password first!")

# Footer
st.write("---------------------")
st.write("Build with 💖 by [Humaira Osama](https://github.com/Humairaosama9298)")
