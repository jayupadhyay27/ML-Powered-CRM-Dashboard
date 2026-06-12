# ML-Powered-CRM-Dashboard

## Problem Statement

Businesses often struggle to identify potential customers, forecast future sales, and understand customer behavior. This project provides an ML-powered CRM dashboard that helps organizations make data-driven decisions through customer analytics, lead conversion prediction, sales forecasting, and customer segmentation.

---

## Dataset Details

Dataset: CRM Customer Dataset

Features include:

* Customer Age
* Annual Income
* Purchase Frequency
* Spending Score
* Engagement Metrics
* Lead Information
* Sales Data

The dataset was preprocessed using data cleaning, handling missing values, feature selection, and normalization techniques.

---

## Machine Learning Approach

### 1. Lead Conversion Prediction

Objective: Predict whether a lead will convert into a customer.

* Algorithm: Logistic Regression
* Input Features: Customer demographics and engagement metrics
* Output: Converted / Not Converted

### 2. Sales Forecasting

Objective: Forecast future sales trends.

* Algorithm: Linear Regression
* Input Features: Historical sales data
* Output: Predicted Sales

### 3. Customer Segmentation

Objective: Group customers into different segments.

* Algorithm: K-Means Clustering
* Segments:

  * High Value Customers
  * Medium Value Customers
  * Low Value Customers

---

## Model Performance

### Lead Conversion Prediction

* Accuracy: 85%
* Precision: 82.98%
* Recall: 63.93%
* F1 Score: 72.22%

### Sales Forecasting

* R² Score: 1
* Mean Absolute Error (MAE):  5.95 × 10⁻²²

### Customer Segmentation

* Number of Clusters: 3
* Business Categories:

  * High Value
  * Medium Value
  * Low Value

---

## Technology Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Plotly
* Streamlit
* Joblib

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/jayupadhyay27/ML-Powered-CRM-Dashboard.git
cd ML-Powered-CRM-Dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app/app.py
```

---

## Screenshots

### Home Dashboard

![Home Dashboard](Screenshots/Home_dashboard.png)

### Lead Conversion Prediction

![Lead Conversion](Screenshots/lead_conversion_prediction.png)

### Sales Forecasting

![Sales Forecasting](Screenshots/sales_forecasting_prediction.png)

### Customer Segmentation

![Customer Segmentation](Screenshots/customer_segmentation_prediction.png)

---

## Live Demo

Streamlit Deployment:
https://ml-powered-crm-dashboard.streamlit.app

---

## Author

Jay Upadhyay

Computer Science Student

Interested in Machine Learning, AI, and Software Development
