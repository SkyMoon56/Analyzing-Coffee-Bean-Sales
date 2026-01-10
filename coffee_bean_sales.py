import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
def load_data(filepath):
    return pd.read_csv(filepath, parse_dates=['Date'])

# Data Exploration
def explore_data(df):
    print("Dataset Overview:\n", df.head())
    print("\nSummary Statistics:\n", df.describe())
    print("\nMissing Values:\n", df.isnull().sum())

# Data Cleaning
def clean_data(df):
    df.dropna(inplace=True)  # Remove missing values
    df.drop_duplicates(inplace=True)  # Remove duplicates

    # Ensure 'Discount' column exists; if not, assume 0
    if "Discount" not in df.columns:
        df["Discount"] = 0

    # Ensure correct column names for calculation
    df["Sales_Amount"] = df["Quantity"] * df["Unit Price"] - df["Discount"]
    
    return df

# Sales by City
def sales_by_city(df):
    city_sales = df.groupby("City")["Sales_Amount"].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=city_sales.index, y=city_sales.values)
    plt.xticks(rotation=45)
    plt.xlabel("City")
    plt.ylabel("Total Sales ($)")
    plt.title("Total Sales by City")
    plt.show()

# Sales by Category
def sales_by_category(df):
    category_sales = df.groupby("Category")["Sales_Amount"].sum()
    plt.figure(figsize=(10, 6))
    category_sales.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Sales Distribution by Category")
    plt.ylabel("")
    plt.show()

# Sales Trend Over Time
def sales_trend(df):
    df["Date"] = pd.to_datetime(df["Date"])
    time_series = df.groupby("Date")["Sales_Amount"].sum()
    
    plt.figure(figsize=(12, 6))
    plt.plot(time_series, marker='o')
    plt.xlabel("Date")
    plt.ylabel("Total Sales ($)")
    plt.title("Sales Trend Over Time")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    filepath = "DatasetForCoffeeSales.csv"

    # Load the data
    df = load_data(filepath)

    # Explore the data
    explore_data(df)

    # Clean the data
    df = clean_data(df)

    # Sales by City
    sales_by_city(df)

    # Sales by Category
    sales_by_category(df)

    # Sales Trend Over Time
    sales_trend(df)
