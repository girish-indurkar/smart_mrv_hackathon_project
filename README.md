# Smart MRV Hackathon Project

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9D%A4-red?logo=streamlit)
![Flask](https://img.shields.io/badge/Flask-API-black?logo=flask)
![NumPy](https://img.shields.io/badge/NumPy-Math-blue?logo=numpy)
![pandas](https://img.shields.io/badge/pandas-Data-green?logo=pandas)
![joblib](https://img.shields.io/badge/joblib-Model%20IO-orange)
![Replit](https://img.shields.io/badge/Replit-Cloud-blue?logo=replit)


## Table of Contents

- [Description](#description)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [File Structure Overview](#file-structure-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Contact](#contact)

## Description

This project appears to be a hackathon-ready AI/ML solution focused on Measurement, Reporting, and Verification (MRV) for agroforestry and rice cultivation. It includes data generation, model training, a Flask backend, and a Streamlit frontend.

## Features

- Generates synthetic datasets for agroforestry and rice MRV.
- Trains machine learning models for rice yield, carbon stock, and CH₄ emission prediction.
- Provides a Flask API for serving predictions.
- Includes a Streamlit UI for user interaction.

## Tech Stack

- Python
- Streamlit
- Flask
- NumPy
- Pandas
- Joblib
- Scikit-Learn 

## File Structure Overview

```
.
├── .gitattributes
├── .idea
├── README.md
├── app.py
├── data
│   └── ...
├── models
│   └── ...
├── requirements.txt
├── streamlit_app.py
└── train_summary.json
```

## Prerequisites

- Python 3.9+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/girish-indurkar/smart_mrv_hackathon_project
   cd smart_mrv_hackathon_project
   ```
2. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask backend:
   ```bash
   python app.py
   ```
2. Run the Streamlit frontend (in a separate terminal):
   ```bash
   streamlit run streamlit_app.py
   ```

The Streamlit app will call `http://localhost:8000/predict` by default.  You can adjust this URL within the Streamlit interface.

**Example cURL Request:**

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
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

## API Reference

The Flask API provides a `/predict` endpoint for making predictions. It expects a JSON payload with the following keys:

- `region` (string): Region name.
- `latitude` (float): Latitude of the farm.
- `longitude` (float): Longitude of the farm.
- `farm_size_ha` (float): Farm size in hectares.
- `soil_ph` (float): Soil pH.
- `soil_organic_carbon_pct` (float): Soil organic carbon percentage.
- `clay_pct` (int): Clay percentage in the soil.
- `annual_rainfall_mm` (int): Annual rainfall in millimeters.
- `avg_temp_c` (float): Average temperature in Celsius.
- `ndvi` (float): Normalized Difference Vegetation Index.
- `evi` (float): Enhanced Vegetation Index.
- `tree_density_per_ha` (int): Tree density per hectare.
- `water_depth_cm` (float): Water depth in centimeters.
- `fertilizer_n_kg_ha` (float): Fertilizer nitrogen application in kg/ha.
- `residue_management` (string): Residue management practice (e.g., "incorporated").
- `irrigation` (string): Irrigation method (e.g., "flood").
- `rice_variety` (string): Rice variety.

The API returns a JSON response containing predicted values for rice yield, carbon stock, and CH₄ emission.

##  Demo
[screen-capture.webm](https://github.com/user-attachments/assets/8cc73013-5bae-4f21-90b7-8b2a0deee721)
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

<!-- TODO: Add author details -->

## Contact

 [https://github.com/girish-indurkar/smart_mrv_hackathon_project](https://github.com/girish-indurkar/smart_mrv_hackathon_project) 
