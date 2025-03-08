import streamlit as st 

def convert_unit(value, unit_from, unit_to, category):
    conversions = {
        "length": {
            "meter_kilometer": 0.001,
            "kilometer_meter": 1000,
            "centimeter_meter": 0.01,
            "meter_centimeter": 100
        },
        "weight": {
            "gram_kilogram": 0.001,
            "kilogram_gram": 1000,
            "pound_kilogram": 0.453592,
            "kilogram_pound": 2.20462
        },
        "volume": {
            "liter_milliliter": 1000,
            "milliliter_liter": 0.001,
            "gallon_liter": 3.78541,
            "liter_gallon": 0.264172
        },
        "temperature": {
            "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
            "fahrenheit_celsius": lambda f: (f - 32) * 5/9,
            "celsius_kelvin": lambda c: c + 273.15,
            "kelvin_celsius": lambda k: k - 273.15
        }
    }

    key = f"{unit_from}_{unit_to}"
    
    if category in conversions and key in conversions[category]:
        conversion = conversions[category][key]
        return round(conversion(value), 6) if callable(conversion) else round(value * conversion, 6)
    return "Conversion not supported"
    
st.title("Unit Converter")    

categories = {
    "Length": ["meter", "kilometer", "centimeter"],
    "Weight": ["gram", "kilogram", "pound"],
    "Volume": ["liter", "milliliter", "gallon"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"]
}

category = st.selectbox("Select Category:", categories.keys())
units = categories[category]

value = st.number_input("Enter the value:")
unit_from = st.selectbox("Convert from:", units)
unit_to = st.selectbox("Convert to:", [u for u in units if u != unit_from])

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to, category.lower())
    st.write(f"Converted value: {result}")
