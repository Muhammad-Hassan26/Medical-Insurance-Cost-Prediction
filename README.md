# 🏥 Medical Insurance Cost Prediction

A complete End-to-End Machine Learning project that predicts individual medical insurance costs based on demographic attributes, health parameters, and lifestyle factors.

## 🔍 Project Overview
Healthcare costs are influenced by multiple variables, including age, body mass index (BMI), smoking habits, and geographic location. This project analyzes the Medical Cost Personal Datasets to uncover key cost drivers, build a robust regression model, and deploy it as an interactive web application.

## 📊 Dataset Features
* **age**: Age of primary beneficiary (numeric)
* **sex**: Contractor gender (`female`, `male`)
* **bmi**: Body mass index, providing an understanding of body weights relative to height ($\text{kg/m}^2$)
* **children**: Number of children/dependents covered by insurance
* **smoker**: Smoking status (`yes`, `no`)
* **region**: Beneficiary's residential area in the US (`northeast`, `southeast`, `northwest`, `southwest`)
* **charges**: Individual medical costs billed by health insurance (**Target Variable**)
  

## 📈 Exploratory Data Analysis (EDA) Insights
* **Smoking Impact**: Smoking is the single strongest driver of high medical insurance charges. Smokers experience significantly higher median costs compared to non-smokers.
* **BMI & Age Correlation**: Medical charges scale upward proportionally with advancing age and higher BMI thresholds, particularly for individuals with high BMI who also smoke.


## ⚙️ Data Preprocessing & Modeling
1. **Cleaning**: Handled missing values and removed duplicate records.
2. **Encoding**: 
   * Binary mapping for `sex` (Female: 0, Male: 1) and `smoker` (No: 0, Yes: 1).
   * One-Hot Encoding for `region` with drop-first configuration to prevent multicollinearity.
3. **Model Training**: Trained regression models (Linear Regression, Random Forest, and Gradient Boosting) and evaluated them using **R² Score** and **Root Mean Squared Error (RMSE)**.
   

