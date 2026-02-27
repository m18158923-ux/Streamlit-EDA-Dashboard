# Streamlit AI Dashboard for EDA 📊

A professional, interactive data dashboard built entirely in Python using Streamlit. This project allows users to upload any `.csv` dataset and instantly get powerful Exploratory Data Analysis (EDA) insights.

## ✨ Features

- **Upload Zone**: Drag and drop any `.csv` file directly from your browser.
- **Instant Insights**: Automatically generates statistical summaries of the uploaded data.
- **Interactive Visualizations**:
  - **Distributions**: Select any numeric column to view its interactive histogram.
  - **Relationships**: Choose X and Y axes to plot an interactive scatterplot.
  - **Correlations**: View a dynamic Seaborn Heatmap showing feature correlations.
- **Premium Design**: Built-in dark mode with aesthetic red styling.

## 🚀 Getting Started

### Prerequisites
You need Python installed. Then, make sure to install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the App
Once dependencies are installed, start the local Streamlit server:

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`.

## 🛠 Built With

* **[Streamlit](https://streamlit.io/)** - For the web app framework
* **[Pandas](https://pandas.pydata.org/)** - For data manipulation
* **[Seaborn](https://seaborn.pydata.org/) & [Matplotlib](https://matplotlib.org/)** - For data visualization
