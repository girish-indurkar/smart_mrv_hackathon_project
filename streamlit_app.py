
import streamlit as st
import pandas as pd
import requests
import json

st.set_page_config(page_title="Agroforestry & Rice MRV", layout="centered")

st.title("🌾 Smart MRV for Agroforestry & Rice")
st.caption("Hackathon-ready demo: predicts rice yield, carbon stock, and CH₄ emissions.")

with st.expander("ℹ️ How to use", expanded=False):
    st.write(
        "Fill farm details below and click **Predict**. "
        "This app calls the Flask backend at `http://localhost:8000/predict`. "
        "Run backend separately: `python app.py`."
    )

# Backend URL
backend_url = st.text_input("Flask Backend URL", "http://localhost:8000/predict")

# Input form
with st.form("input_form"):
    c1, c2 = st.columns(2)

    with c1:
        region = st.selectbox("Region", ['Indo-Gangetic Plain', 'Coastal Andhra', 'Eastern UP', 'Terai Nepal', 'Mekong Delta'])
        farm_size_ha = st.number_input("Farm size (ha)", 0.1, 50.0, 1.0, 0.1)
        soil_ph = st.number_input("Soil pH", 4.0, 9.0, 6.5, 0.1)
        soil_organic_carbon_pct = st.number_input("Soil Organic Carbon (%)", 0.1, 5.0, 1.2, 0.1)
        clay_pct = st.number_input("Clay (%)", 0.0, 80.0, 25.0, 0.1)
        annual_rainfall_mm = st.number_input("Annual Rainfall (mm)", 0, 5000, 1200, 10)
        avg_temp_c = st.number_input("Average Temp (°C)", 10.0, 45.0, 27.0, 0.1)
        ndvi = st.number_input("NDVI", 0.0, 1.0, 0.65, 0.01)

    with c2:
        evi = st.number_input("EVI", 0.0, 1.0, 0.55, 0.01)
        tree_density_per_ha = st.number_input("Tree Density (per ha)", 0, 500, 40, 1)
        water_depth_cm = st.number_input("Water Depth (cm)", 0.0, 40.0, 5.0, 0.1)
        fertilizer_n_kg_ha = st.number_input("Fertilizer N (kg/ha)", 0.0, 400.0, 90.0, 1.0)
        residue_management = st.selectbox("Residue Management", ['removed', 'incorporated', 'mulched'])
        irrigation = st.selectbox("Irrigation", ['flood', 'alternate_wetting_drying', 'drip'])
        rice_variety = st.selectbox("Rice Variety", ['Swarna', 'IR64', 'MTU1010', 'Samba Mahsuri', 'Naveen'])
        latitude = st.number_input("Latitude", -90.0, 90.0, 26.5, 0.000001, format="%.6f")
        longitude = st.number_input("Longitude", -180.0, 180.0, 82.0, 0.000001, format="%.6f")

    submitted = st.form_submit_button("Predict")

if submitted:
    payload = {
        "region": region,
        "latitude": latitude,
        "longitude": longitude,
        "farm_size_ha": farm_size_ha,
        "soil_ph": soil_ph,
        "soil_organic_carbon_pct": soil_organic_carbon_pct,
        "clay_pct": clay_pct,
        "annual_rainfall_mm": int(annual_rainfall_mm),
        "avg_temp_c": avg_temp_c,
        "ndvi": ndvi,
        "evi": evi,
        "tree_density_per_ha": int(tree_density_per_ha),
        "water_depth_cm": water_depth_cm,
        "fertilizer_n_kg_ha": fertilizer_n_kg_ha,
        "residue_management": residue_management,
        "irrigation": irrigation,
        "rice_variety": rice_variety
    }
    try:
        resp = requests.post(backend_url, json=payload, timeout=10)
        if resp.status_code == 200:
            preds = resp.json()
            st.success("Prediction complete!")
            st.metric("Rice Yield (t/ha)", round(preds["rice_yield_t_ha"], 3))
            st.metric("Carbon Stock (tCO₂e/ha)", round(preds["carbon_stock_tco2e_ha"], 3))
            st.metric("CH₄ Emission (kg/ha)", round(preds["ch4_emission_kg_ha"], 1))
        else:
            st.error(f"Backend error: {resp.status_code} — {resp.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")

st.divider()
st.write("Sample data CSV is included with the project. You can also batch-predict using cURL or Postman by sending a list of records to the same endpoint.")
