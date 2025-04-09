import streamlit as st

# App Title and Subtitle
st.title("🌍 Unit Converter App")
st.markdown("### ⚡ Instantly Convert Length, Weight, and Time")
st.write("Welcome to the **Ultimate Unit Converter**! Just choose a category, enter a value, and get your answer right away.")

# Select conversion category
category = st.selectbox("🔘 Select a Conversion Category", ["Length", "Weight", "Time"])

# Select unit conversion based on category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion Type", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion Type", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏲️ Select Conversion Type", [
        "Seconds to Minutes", "Minutes to Seconds",
        "Minutes to Hours", "Hours to Minutes",
        "Hours to Days", "Days to Hours"
    ])

# Input field
value = st.number_input("🧮 Enter the value to convert", min_value=0.0, format="%.2f")

# Conversion Logic
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return None

# Display Result
if value > 0:
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"✅ Successfully Converted!\n\n**{value:.2f}** {unit.split(' to ')[0]} is equal to **{result:.2f}** {unit.split(' to ')[1]}")
    else:
        st.error("❌ Oops! Something went wrong with the conversion.")
else:
    st.info("ℹ️ Please enter a value greater than 0 to start the conversion.")
