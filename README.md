
---

# VandyDataScience EM/Dev Assessment 2024


👋 **Welcome!** This repository contains my submission for the VandyDataScience (VDS) 2024 EM/Dev assessment, where I used data science techniques to analyze and model a real-world dataset. I'm excited to contribute to the VDS community by exploring impactful ways to utilize data!

---

## Project Overview

The purpose of this project is to showcase my comfort with data science tools and techniques through an end-to-end analysis. By exploring, cleaning, and modeling a dataset, I demonstrate my skills in tackling a real-world problem and using data science to gain meaningful insights. The project consists of three levels that build upon each other:

1. **Level 1:** Data Cleaning and Exploration
2. **Level 2:** Model Creation
3. **Level 3:** Model Evaluation and Improvement

This README provides a summary of the project, its objectives, and the steps taken to complete each level.

---

## Dataset Information

I chose the **Dataset for Assessing Mathematics Learning in Higher Education** from the MathE platform, containing **9546 entries**. This dataset includes data on students' answers to math questions, categorized by:

- **Student ID** and **Country**
- **Question ID**, **Type of Answer** (correct or incorrect), and **Question Level** (basic or advanced)
- **Topic**, **Subtopic**, and **Keywords**

The dataset spans from **February 2019 to December 2023** and is well-suited for a classification task, specifically predicting whether a student’s answer is correct or incorrect based on various factors.

---

## Project Steps

### Level 1: Data Cleaning and Exploration

1. **Loaded the Dataset:** Imported the data and explored its structure and features.
2. **Checked for Duplicates and Missing Values:** Removed 2083 duplicate rows and confirmed no missing values.
3. **Standardized Text Columns:** Converted text columns (e.g., country, topic) to lowercase for consistency.

### Level 2: Model Creation

1. **Defined Features and Target Variable:** Selected relevant features to predict the `Type of Answer`.
2. **One-Hot Encoding of Categorical Data:** Transformed categorical variables into numerical format for modeling.
3. **Initial Model Training:** Used a `DecisionTreeClassifier` to establish a baseline model, achieving an initial accuracy of 57%.

### Level 3: Model Evaluation and Improvement

1. **Hyperparameter Tuning and Testing Different Models:** Experimented with various configurations of the Decision Tree and tested alternative models like `RandomForestClassifier`.
2. **Final Model Evaluation:** Documented model performance, strengths, and areas for improvement.

---

## Results and Discussion

The baseline model achieved an accuracy of **57%**, indicating that initial feature selection and model choice could be improved. After testing various models and tuning parameters, I observed slight accuracy improvements. Additional steps could involve deeper feature engineering or advanced algorithms to further optimize accuracy.

---

## Repository Contents

- **Script.py**: Contains the main code for loading, cleaning, and modeling the dataset.
- **Write-Up.pdf**: A comprehensive report summarizing the project’s background, methodology, results, and conclusions.

---

## Submission Checklist

- [x] All code files are committed and pushed to this repository.
- [x] The write-up is included as a PDF in the repository.
- [x] Application form is completed with this GitHub repository link submitted.

---

## Resources

Dataset: [Dataset for Assessing Mathematics Learning in Higher Education](https://doi.org/10.34620/dadosipb/PW3OWY)  
Python Libraries: `pandas`, `scikit-learn`

---

**Thank you, VDS team, for this opportunity! I look forward to the possibility of contributing to VandyDataScience!**

--- 

