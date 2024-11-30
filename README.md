# Walmart Sales Analysis and Big Data Insights

## Overview

This project explores the use of **Big Data** to analyze **Walmart's sales data** and provides insights to enhance
business decision-making. The dataset includes various features such as store number, weekly sales, temperature, fuel
prices, consumer price index (CPI), unemployment rate, and holiday flag. The goal is to demonstrate how Big Data can
help retail businesses, like Walmart, navigate post-pandemic challenges and optimize operations through data-driven
decision support.

## Dataset

The dataset used in this project is the **Walmart Sales dataset**, which contains the following fields:

- **Store**: Store number
- **Date**: Sales week start date
- **Weekly_Sales**: Weekly sales value for the store
- **Holiday_Flag**: Indicator of whether a holiday falls within the week
- **Temperature**: Air temperature in the region
- **Fuel_Price**: Fuel cost in the region
- **CPI**: Consumer Price Index
- **Unemployment**: Unemployment rate in the region

### Link to Dataset:

[Download Walmart Sales Dataset](https://www.kaggle.com/datasets/mikhail1681/walmart-sales)

## Objective

The primary objectives of this project are:

- To **visualize** the impact of various factors (e.g., temperature, fuel price, CPI, and unemployment) on Walmart's
  sales.
- To **predict** future sales trends using machine learning techniques such as **Linear Regression**.
- To explore how **Big Data** can assist businesses in the **post-pandemic era** by enhancing decision-making processes
  related to sales forecasting, inventory management, and market trends.

## Analysis Steps

1. **Data Preprocessing**
    - Load and clean the dataset
    - Handle missing data and incorrect data types
    - Feature engineering (e.g., convert `Date` to datetime format)

2. **Exploratory Data Analysis (EDA)**
    - Perform initial exploratory data analysis to understand trends, correlations, and potential outliers in the data.
    - Create visualizations like line charts for sales trends, bar charts for holiday impact, and scatter plots to
      explore relationships between temperature, fuel price, and sales.

3. **Predictive Analysis**
    - Use machine learning models (e.g., **Linear Regression**) to predict future sales based on features like **fuel
      price**, **temperature**, **CPI**, and **unemployment**.
    - Evaluate the model performance using metrics like **Mean Absolute Error (MAE)** and **Root Mean Squared Error (
      RMSE)**.

## Key Insights

- **Sales Trends Over Time**: Understanding the seasonal variation in sales, including the effects of holidays and
  temperature fluctuations.
- **Impact of Economic Indicators**: Analyzing how CPI and fuel price affect consumer purchasing behavior and sales.
- **Effect of Unemployment**: Assessing how changes in the unemployment rate can correlate with changes in sales.

## Technologies and Libraries Used

- **Python** for data analysis and modeling
- **Pandas** for data manipulation
- **Matplotlib & Seaborn** for data visualization
- **Scikit-learn** for building predictive models

## How to Run

To run the analysis and reproduce the results:

1. Clone this repository.
2. Ensure you have the required libraries installed by running:
   ```bash
   pip install -r requirements.txt
    ```
3. Run the Jupyter notebook `Walmart_Sales_Analysis.ipynb` to see the analysis and insights.
    ```bash
    jupyter notebook Walmart_Sales_Analysis.ipynb
    ```

Feel free to explore the dataset and code to adapt the analysis to your specific needs.
