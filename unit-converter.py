import streamlit as st  

# Title and Introduction
st.title("🌍 Unit Converter App")  
st.markdown("### Convert Length, Weight, and Time Instantly")  
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")  

# Select conversion category
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])  

# Select unit conversion based on category
if category == "Length":  
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to miles", "Miles to kilometers"])  
elif category == "Weight":  
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])  
elif category == "Time":  
    unit = st.selectbox("⏲ Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])  

# Input field for value
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")  

# Conversion function
def convert_units(category, value, unit):  
    if category == "Length":  
        if unit == "Kilometers to miles":  
            return value * 0.621371  
        elif unit == "Miles to kilometers":  
            return value / 0.621371  

    elif category == "Weight":  
        if unit == "Kilograms to pounds":  
            return value * 2.20462  
        elif unit == "Pounds to kilograms":  
            return value / 2.20462  

    elif category == "Time":  
        if unit == "Seconds to minutes":  
            return value / 60  
        elif unit == "Minutes to seconds":  
            return value * 60  
        elif unit == "Minutes to hours":  
            return value / 60  
        elif unit == "Hours to minutes":  
            return value * 60  
        elif unit == "Hours to days":  
            return value / 24  
        elif unit == "Days to hours":  
            return value * 24  

    return None  # In case of an unexpected input  

# Perform conversion and display result  
if value > 0:  
    result = convert_units(category, value, unit)  
    if result is not None:  
        st.success(f"The result is {result:.2f}")  
    else:  
        st.error("Invalid conversion. Please check your inputs.")  

            
