# Dash Airbnb

[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)

## Table of Contents

- [Context](#-context)
- [Software features](#-software-features)
- [Technologies and tools](#-technologies-and-tools)
- [Architecture](#-architecture)
- [Repository structure](#-repository-structure)
- [Requirements](#-requirements)
- [How to run](#-how-to-run)
- [Author](#-author)

# 📌 Context 

This project contains 2 interactive analyses:
- **Sales Analysis**: An interactive sales analysis using the Pygwalker library in a Jupyter Notebook.
- **Airbnb Rio de Janeiro Dashboard**: An interactive dashboard analyzing Airbnb data in Rio de Janeiro, using Pygwalker, Streamlit, and Plotly.

## 🚀 Software features

- **Configured base structure**: Ready-to-use environment templates.
- **Modular repository layout**: Clean separation of raw data, Jupyter notebooks, and deployment scripts.
- **Automated Python scripts**: Ready-to-run scripts for Streamlit applications.
- **Interactive notebook analysis**: Exploratory data analysis with visual query execution.

## 🛠️ Technologies and tools

- **Python**: Core programming language for processing.
- **Pandas**: Data manipulation and analysis library.
- **Jupyter Notebook**: Interactive environment for exploratory data analysis.
- **Streamlit**: Web application framework to share data scripts.
- **Pygwalker**: Interactive UI for exploratory data analysis.
- **Plotly**: Data visualization library for interactive plotting and mapping.

## 📋 Architecture

```mermaid
graph LR
    A[📦 listings.csv & vendas.csv] -->| Ingestion & Processing | B(⚡Python / Pandas) 
    B -->|Interactive UI| C[📊 Streamlit / Pygwalker]
    
    style A fill:#134647,stroke:#333,stroke-width:2px
    style B fill:#0074b4,stroke:#333,stroke-width:2px
    style C fill:#69b,stroke:#333,stroke-width:2px
```

## 📂 Repository structure

```text
- 📂 analytics-airbnb-data/
  - 📄 requirements.txt
  - 📂 .devcontainer/
    - 📄 devcontainer.json
  - 📂 data/
    - 📄 listings.csv
    - 📄 vendas.csv
  - 📂 notebooks/
    - 📄 main_airbnb.ipynb
    - 📄 main_vendas.ipynb
    - 📄 setup.ipynb
  - 📂 scripts/
    - 📄 dash_airbnb_v1.py
    - 📄 dash_airbnb_v2.py
    - 📄 streamlit_config.json
```

## 📦 Requirements

- **Python 3.10+**
- **IDE** (e.g., VS Code with Jupyter extension, or JupyterLab/Jupyter Notebook installed)

## ⚙️ How to run

### 1. Clone the repository
```bash
git clone https://github.com/MatheusRodri/analytics-airbnb-data.git
cd analytics-airbnb-data
```

### 2. Set up a virtual environment (Recommended)
**On Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the analyses

#### Using Jupyter Notebooks
Navigate to the `notebooks` directory in your IDE/Jupyter instance and run:
- `main_airbnb.ipynb`
- `main_vendas.ipynb`

#### Running the Streamlit dashboards
Because of relative data paths in the code, navigate to the `scripts` folder first before executing Streamlit:
```bash
cd scripts
```

To run version 1 (Pygwalker Renderer):
```bash
streamlit run dash_airbnb_v1.py
```

To run version 2 (Plotly/Mapbox Map):
```bash
streamlit run dash_airbnb_v2.py
```

## 👤 Author

Matheus Rodrigues 
[LinkedIn](https://linkedin.com/in/matheus-rodrigues-mrj) [GitHub](https://github.com/MatheusRodri)

