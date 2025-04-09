import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set page config with unique theme
st.set_page_config(page_title="Data Sweeper", page_icon="💿", layout='wide')

# Custom CSS for better styling
st.markdown(
    """
    <style>
    .stApp {
        background-color:rgb(175, 175, 235);
        color: white;
    }
    .css-1d391kg { color: #f0db4f; }
    .stButton>button { background-color: #5e60ce; color: white; border-radius: 8px; padding: 10px 20px; }
    .stDownloadButton>button { background-color: #4caf50; color: white; }
    .stCheckbox>div { color: #f0db4f; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title & Description
st.title("💿 Data Sweeper - Sterling Integrator By Iffat Mumtaz")
st.write("Convert & clean CSV/Excel files with powerful data transformation tools!")

# File uploader
uploaded_files = st.file_uploader("📂 Upload your file (CSV or Excel)", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for idx, file in enumerate(uploaded_files):
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"❌ Unsupported file type: {file_ext}")
            continue

        st.markdown("---")
        st.subheader(f"📊 Preview of `{file.name}`")
        st.dataframe(df.head())

        # Create a copy for modifications
        processed_df = df.copy()

        # Data Cleaning Options
        st.subheader("🧼 Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}", key=f"clean_{idx}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"🗑 Remove Duplicates from {file.name}", key=f"dup_{idx}"):
                    processed_df.drop_duplicates(inplace=True)
                    st.success("✅ Duplicates Removed!")

            with col2:
                if st.button(f"🛠 Fill Missing Values for {file.name}", key=f"fillna_{idx}"):
                    numeric_cols = processed_df.select_dtypes(include=['number']).columns
                    processed_df[numeric_cols] = processed_df[numeric_cols].fillna(processed_df[numeric_cols].mean())
                    st.success("✅ Missing Values Filled!")

            st.subheader("✅ Cleaned Preview")
            st.dataframe(processed_df.head())

        # Column Selection
        st.subheader("📌 Select Columns to Keep")
        selected_columns = st.multiselect(f"Select Columns for {file.name}", processed_df.columns, default=processed_df.columns, key=f"columns_{idx}")
        filtered_df = processed_df[selected_columns]

        # Data Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"📈 Show Visualization for {file.name}", key=f"viz_{idx}"):
            st.bar_chart(filtered_df.select_dtypes(include='number'))

        # Conversion Options
        st.subheader("🔄 File Conversion")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=f"convert_{idx}")

        if st.button(f"💾 Convert {file.name}", key=f"download_btn_{idx}"):
            buffer = BytesIO()

            if conversion_type == "CSV":
                filtered_df.to_csv(buffer, index=False)
                download_file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            else:
                filtered_df.to_excel(buffer, index=False)
                download_file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)
            st.download_button(
                label=f"⬇️ Download {download_file_name}",
                data=buffer,
                file_name=download_file_name,
                mime=mime_type,
                key=f"download_{idx}"
            )

        st.success(f"🎉 `{file.name}` processed successfully!")

