
from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load models
yield_model = joblib.load("models/rice_yield_t_ha.joblib")
carbon_model = joblib.load("models/carbon_stock_tco2e_ha.joblib")
ch4_model = joblib.load("models/ch4_emission_kg_ha.joblib")

# Define expected columns/order
NUMERIC_COLS = [
  "latitude",
  "longitude",
  "farm_size_ha",
  "soil_ph",
  "soil_organic_carbon_pct",
  "clay_pct",
  "annual_rainfall_mm",
  "avg_temp_c",
  "ndvi",
  "evi",
  "tree_density_per_ha",
  "water_depth_cm",
  "fertilizer_n_kg_ha"
]
CATEGORICAL_COLS = [
  "region",
  "residue_management",
  "irrigation",
  "rice_variety"
]
ALL_COLS = NUMERIC_COLS + CATEGORICAL_COLS

def to_dataframe(payload):
    # Accept both list (multiple records) or dict (single)
    rows = payload if isinstance(payload, list) else [payload]
    df = pd.DataFrame(rows)
    # Ensure all columns exist
    for c in ALL_COLS:
        if c not in df.columns:
            df[c] = np.nan if c in NUMERIC_COLS else None
    # Order columns
    df = df[ALL_COLS]
    return df

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json(force=True)
    df = to_dataframe(payload)

    yield_pred = yield_model.predict(df)[0] if len(df)==1 else yield_model.predict(df).tolist()
    carbon_pred = carbon_model.predict(df)[0] if len(df)==1 else carbon_model.predict(df).tolist()
    ch4_pred = ch4_model.predict(df)[0] if len(df)==1 else ch4_model.predict(df).tolist()

    return jsonify({
        "rice_yield_t_ha": yield_pred,
        "carbon_stock_tco2e_ha": carbon_pred,
        "ch4_emission_kg_ha": ch4_pred
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
