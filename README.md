# 🏡 House Price Prediction Model

This is a **Machine Learning project** where I built a **House Price Prediction model** using the **Bengaluru House Price dataset** from Kaggle.  
The project covers everything from **data cleaning, exploratory data analysis (EDA), feature engineering, model training with GridSearchCV, and deployment on Streamlit Cloud**.

---

## 🔑 Project Workflow

1. **Dataset Collection**  
   - Sourced the dataset from Kaggle (Bengaluru House Price dataset).

2. **Data Cleaning**  
   - Handled missing values.  
   - Removed duplicates and irrelevant features.  
   - Converted categorical features into usable numerical format.  

3. **Exploratory Data Analysis (EDA)**  
   - Analyzed distribution of house prices, square feet, BHK, and bathrooms.  
   - Visualized outliers and patterns in the data.  

4. **Feature Engineering**  
   - Created new features like price per square foot.  
   - Removed unrealistic data points (e.g., 500 sqft house with 6 BHK).  
   - Applied dimensionality reduction for location features.  

5. **Model Development**  
   - Tried multiple regression models.  
   - Tuned hyperparameters using **GridSearchCV**.  
   - Selected the best model based on accuracy and error metrics.  

6. **Deployment**  
   - Saved the model (`house_price_model.pkl`) and column info (`columns.json`).  
   - Built a **Streamlit web app** for predictions.  
   - Deployed successfully on **Streamlit Cloud**.  

---

## 🚀 Live Demo

👉 [Check out the app here](https://house-price-prediction-nnfrwtkdr6c7uc2lzk64b3.streamlit.app/)  

---

## 🛠️ Tech Stack

- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)  
- **Streamlit** for web app development  
- **GridSearchCV** for model tuning  
- **Pickle / JSON** for saving model & metadata  

---
