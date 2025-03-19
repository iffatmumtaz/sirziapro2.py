from unittest import result
import streamlit as st 
st.title("🌍Unit Converter App")

st.markdown("### Convert Length Weight And Time Instantly")
st.write("Wellcome! Select a category, enter a value and get the converter result in real-time")
category = st.selectbox("Choose a category", ["Length" , "Weight" , "Time"])

def convert_units(category, value ,unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
        
        elif category == "  Weight":
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
            
            if category =="Length":
                unit =st.selectbox("📏 Select Conversation", ["Kilometers to Miles" , "Miles to Kilometers"])
    elif category =="Weight":
        unit = st.selectbox("⚖  Select Conversation", ["Kilograms to pounds" , "Pounds to kilograms"])
    elif category == "Time":
        unit = st.selectbox("⏲ Select Conversation", ["Seconds to minutes" , "Minutes to seconds" , "Hours to minutes" , "Hours to days" , "Days to hours"])
        value  = st.numbers_input("Enter the value to Convert")
            
    st.success(f"The result is {result:.2f}")
                
            
