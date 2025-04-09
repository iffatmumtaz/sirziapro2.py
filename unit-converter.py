import streamlit as st

# Title and Subtitle
st.title("🌍 Unit Converter App")
st.markdown("### ⚡ Instantly Convert Length, Weight, and Time")
st.write("Welcome! Select a category, enter a value, and get the converted result instantly.")

# Category selection
category = st.selectbox("🔘 Choose a category", ["Length", "Weight", "Time"])

# Unit selection based on category
if category == "Length":
    unit = st.selectbox("📏 Select conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏲️ Select conversion", [
        "Seconds to Minutes", "Minutes to Seconds",
        "Minutes to Hours", "Hours to Minutes",
        "Hours to Days", "Days to Hours"
    ])

# Input value
value = st.number_input("🧮 Enter the value to convert", min_value=0.0, format="%.2f")

# Conversion function
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

# Show result
if value > 0:
    result = convert_units(category, value, unit)
    if result is not None:
        from_unit, to_unit = unit.split(" to ")
        st.success(f"✅ Successfully Converted!\n\n**{value:.2f} {from_unit}** is equal to **{result:.2f} {to_unit}**")
    else:
        st.error("❌ Invalid conversion. Please check your input.")
else:
    st.info("ℹ️ Please enter a value greater than 0 to perform conversion.")
