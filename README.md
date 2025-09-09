
# 🌾 Smart MRV for Agroforestry & Rice — Hackathon Starter



![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9D%A4-red?logo=streamlit)
![Flask](https://img.shields.io/badge/Flask-API-black?logo=flask)
![NumPy](https://img.shields.io/badge/NumPy-Math-blue?logo=numpy)
![pandas](https://img.shields.io/badge/pandas-Data-green?logo=pandas)
![joblib](https://img.shields.io/badge/joblib-Model%20IO-orange)
![Replit](https://img.shields.io/badge/Replit-Cloud-blue?logo=replit)


This project is a **hackathon-ready** AI/ML solution that:
- Generates a **synthetic dataset** (2000 rows)
- Trains **3 ML models**: rice yield (t/ha), carbon stock (tCO₂e/ha), CH₄ emission (kg/ha)
- Provides a **Flask backend** for predictions
- Provides a **Streamlit frontend** for a friendly UI

## 📦 Structure
```
.
├── data/
│   └── agroforestry_rice_mrv_2000.csv
├── models/
│   ├── rice_yield_t_ha.joblib
│   ├── carbon_stock_tco2e_ha.joblib
│   └── ch4_emission_kg_ha.joblib
├── app.py                 # Flask API (localhost:8000)
├── streamlit_app.py       # Streamlit UI
├── train_summary.json     # Metrics summary (R², MAE)
└── requirements.txt
```

## 🚀 Quickstart

1) Create a virtual environment and install deps
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2) Start the Flask backend
```bash
python app.py
```

3) Run the Streamlit frontend (new terminal)
```bash
streamlit run streamlit_app.py
```
By default, the Streamlit app will call `http://localhost:8000/predict`. You can edit the URL in the UI.

## 🧪 Try a cURL request
```bash
curl -X POST http://localhost:8000/predict   -H "Content-Type: application/json"   -d '{
    "region": "Indo-Gangetic Plain",
    "latitude": 26.5,
    "longitude": 82.0,
    "farm_size_ha": 1.2,
    "soil_ph": 6.4,
    "soil_organic_carbon_pct": 1.1,
    "clay_pct": 24,
    "annual_rainfall_mm": 1200,
    "avg_temp_c": 27.0,
    "ndvi": 0.65,
    "evi": 0.55,
    "tree_density_per_ha": 40,
    "water_depth_cm": 5.0,
    "fertilizer_n_kg_ha": 90.0,
    "residue_management": "incorporated",
    "irrigation": "flood",
    "rice_variety": "IR64"
  }'
```

## 📊 Training Metrics
R² / MAE for each target are stored in `train_summary.json`.

## 🛠 Notes
- The dataset is **synthetic** (simulated) but constructed with realistic relationships.
- The models are scikit-learn RandomForests in a preprocessing Pipeline.
- Extend easily with geospatial features and remote sensing stacks.

## 🚀 Demo:

🔗 [Live App on Replit](https://4d10036b-baca-4321-a7d6-f6defa8f9760-00-29kzsbrjjaw5r.pike.replit.dev/)  

