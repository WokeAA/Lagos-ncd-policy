# Lagos NCD Policy Simulator

**PhD Research Project**
**Project Owner: Oghenewoke Atariata**

A Bayesian hierarchical Poisson regression model that estimates how many
NCD cases (hypertension, CVD, diabetes) could be avoided in each Lagos LGA
if urbanization indicators (NO2, NDVI, NLR) were changed.

## How to run

```bash
cd policy_simulator
pip install -r requirements.txt
streamlit run streamlit_dashboard.py --server.port 8501
```

## What's in this folder

```
policy_simulator/
├── streamlit_dashboard.py       ← 7-page interactive dashboard
├── lagos_brand.py             ← Lagos/Nigeria branded CSS theme
├── .streamlit/config.toml     ← Streamlit theme configuration
├── requirements.txt           ← Python dependencies
├── data/                      ← ALL data files (self-contained)
│   ├── bayes_posterior_{htn,cvd,dm}.nc    Bayesian posteriors (inference)
│   ├── raw_model_{htn,cvd,dm}.nc          Bayesian posteriors (scenario)
│   ├── scenario_comparison.csv            8 scenarios × 3 diseases
│   ├── regression_panel.csv               100-row analysis dataset
│   ├── Lagos_LGA_master_harmonized.csv    440-row LGA × year panel
│   └── Nigeria_-_Local_Government_Area_Boundaries.geojson
└── README.md
```
