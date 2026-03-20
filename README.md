# ☕ Coffee Bean Sales Analysis

A Python data analysis project that cleans, aggregates, and visualizes coffee sales data to uncover geographic trends, category performance, and time-series patterns. Built as a portfolio demonstration of end-to-end data wrangling and visualization.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![pandas](https://img.shields.io/badge/pandas-Data%20Wrangling-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

This project walks through a complete EDA (Exploratory Data Analysis) pipeline on a coffee sales dataset — from raw CSV ingestion through cleaning, aggregation, and three distinct visualization outputs. It demonstrates practical data engineering skills including handling missing values, computing derived metrics, and generating publication-quality charts.

---

## ✨ Features

- **Data Loading & Exploration** — reads CSV with automatic date parsing, prints summary statistics and missing value counts
- **Data Cleaning** — removes duplicates, fills nulls, and computes `Sales_Amount = Quantity × Unit Price − Discount`
- **Sales by City** — ranked bar chart showing top-performing markets
- **Sales by Category** — pie chart showing revenue distribution across coffee types
- **Sales Trend Over Time** — line chart showing daily/weekly revenue patterns

---

## 📊 Sample Visualizations

| Chart | Description |
|-------|-------------|
| `Figure_1.png` | Total sales by city (bar chart) |
| `Figure_2.png` | Sales distribution by category (pie chart) |
| `Figure_3.png` | Sales trend over time (line chart) |

---

## 🛠️ Tech Stack

| Library | Purpose |
|---------|---------|
| `pandas` | Data ingestion, cleaning, and aggregation |
| `matplotlib` | Base charting and figure customization |
| `seaborn` | Statistical bar chart styling |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+

### Installation

```bash
git clone https://github.com/SkyMoon56/Analyzing-Coffee-Bean-Sales.git
cd Analyzing-Coffee-Bean-Sales
pip install pandas matplotlib seaborn
```

### Run

```bash
python coffee_bean_sales.py
```

Outputs three chart windows and prints dataset statistics to the console.

---

## 📂 Project Structure

```
Analyzing-Coffee-Bean-Sales/
├── coffee_bean_sales.py        # Main analysis script
├── DatasetForCoffeeSales.csv   # Source dataset
├── Figure_1.png                # Sales by city chart
├── Figure_2.png                # Sales by category chart
├── Figure_3.png                # Sales trend over time chart
└── README.md
```

---

## 🔍 How It Works

The script is structured as a series of modular functions:

```python
load_data(filepath)       # Read CSV with parse_dates
explore_data(df)          # Print head, describe, null counts
clean_data(df)            # Drop nulls/dupes, compute Sales_Amount
sales_by_city(df)         # Seaborn bar chart grouped by City
sales_by_category(df)     # Pie chart grouped by Category
sales_trend(df)           # Time-series line chart by Date
```

---

## 💡 Key Decisions

- **Derived metric** — `Sales_Amount` is computed at runtime rather than assumed present, with a fallback `Discount = 0` if the column is missing
- **Modular design** — each analysis step is a standalone function, making it easy to extend or swap out individual charts
- **Graceful handling** — the script does not crash if the `Discount` column is absent in a new dataset

---

## 📝 License

MIT — free to use, fork, and adapt.

---

## 🤝 Contact

**Sky Moon** — [sky.moon7567@gmail.com](mailto:sky.moon7567@gmail.com) | [LinkedIn](https://linkedin.com/in/sky-moon/)
