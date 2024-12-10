import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define a function to process inputs and return outputs
def compute_outputs(data, slider1, slider2):
    # Example calculation
    data['Processed Value'] = data['Value'] * slider1 + slider2
    summary = data['Processed Value'].sum()
    return data, summary

# Streamlit app
st.set_page_config(layout="wide")
st.title("Interactive Table and Sliders")

cols = st.columns(2)

# Editable table
cols[0].header("Editable Table")
default_data = {
    "Category": ["A", "B", "C"],
    "Value": [10, 20, 30],
}
df = pd.DataFrame(default_data)

edited_data = cols[0].data_editor(df, num_rows="dynamic", use_container_width=True)

# Sliders for additional input
cols[1].header("Sliders")
slider1 = cols[1].slider("Multiplier (Slider 1)", min_value=0.0, max_value=5.0, value=1.0)
slider2 = cols[1].slider("Offset (Slider 2)", min_value=0, max_value=20, value=0)

# Compute and display outputs
if st.button("Compute Outputs"):
    processed_data, total = compute_outputs(edited_data, slider1, slider2)

    st.subheader("Processed Data")
    st.dataframe(processed_data)

    st.subheader("Summary Output")
    st.write(f"Total Processed Value: {total}")

    # Visualization
    st.subheader("Visualization")
    fig, ax = plt.subplots()
    ax.bar(processed_data["Category"], processed_data["Processed Value"], color='skyblue')
    ax.set_title("Processed Values by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Processed Value")
    st.pyplot(fig)
