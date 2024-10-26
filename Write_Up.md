

# VandyDataScience EM/Dev Assessment Write-Up

## Background Information

The dataset I selected, titled **Dataset for Assessing Mathematics Learning in Higher Education**, comes from the MathE platform. This platform supports mathematics education by providing a repository of questions and answers relevant to higher education students' learning progress. The dataset includes responses from students on various mathematical topics, collected from February 2019 to December 2023, with a total of 9546 entries. Each entry records a unique question answered by a student, the type of answer given (correct or incorrect), and additional attributes like the question’s difficulty level, topic, and subtopic. This data, donated by researchers from the Polytechnic Institute of Bragança, provides valuable insights into student performance and response patterns across different mathematical topics.

Using this dataset, I aimed to predict whether a student's answer would be correct or incorrect based on features such as question difficulty level, topic, subtopic, and the student’s country. This predictive task has real-world significance, as it can offer insights into areas where students may need additional support, thus improving the learning experience in mathematics education.

## Problem Statement

The primary objective of this project is to predict the `Type of Answer` (correct or incorrect) a student will provide based on various attributes related to the question and the student's background.

## Hypothesis

I hypothesize that factors like `Question Level` (basic or advanced) and the specific `Topic` and `Subtopic` will significantly influence the likelihood of a student answering correctly. Additionally, variations in student performance may emerge across different countries, possibly due to differing educational backgrounds.

## Methods

### Data Cleaning and Preparation

The dataset was initially loaded and checked for missing values and duplicates. There were no missing values, but 2083 duplicate rows were removed to ensure data quality. To prepare the data for modeling, I standardized all categorical columns to lowercase for consistency, specifically in columns such as `Student Country`, `Question Level`, `Topic`, `Subtopic`, and `Keywords`.

### Feature Selection and Encoding

I selected `Question Level`, `Topic`, `Subtopic`, and `Student Country` as features to predict `Type of Answer`. Since these features are categorical, I applied one-hot encoding to convert them into a numerical format suitable for modeling. This transformation created a matrix of binary columns representing each possible category, allowing the model to interpret the categorical information effectively.

### Model Selection

For the initial model, I used a **Decision Tree Classifier** due to its interpretability and ability to handle categorical data. This baseline model achieved an accuracy of **57%**, which served as a starting point for further improvement. I then experimented with hyperparameter tuning, adjusting the `max_depth` and `min_samples_split` parameters to improve the model’s generalizability. 

Additionally, I tested a **Random Forest Classifier** to explore if an ensemble approach could enhance accuracy. The Random Forest model showed slight improvements, although the computational cost was higher.

### Model Evaluation

Each model was evaluated using accuracy on a hold-out test set, consisting of 20% of the data. Although accuracy provided a straightforward performance metric, further evaluation with precision and recall metrics could provide deeper insights into model performance, especially for applications where predicting incorrect answers correctly is more crucial than predicting correct answers.

## Results and Discussion

The baseline **Decision Tree Classifier** achieved an initial accuracy of 57%, which indicated room for improvement. Hyperparameter tuning and the use of a **Random Forest Classifier** led to slight improvements in accuracy, though no substantial increase was observed. The results suggest that while the chosen features provide some predictive power, additional features or advanced feature engineering (such as extracting additional patterns from keywords) might be needed to improve model performance further.

The findings indicate that while question difficulty and topic are somewhat predictive, the dataset may benefit from additional contextual information to enhance accuracy. For future improvements, exploring more complex models like gradient-boosting techniques, or implementing advanced feature engineering on the `Keywords` column, could yield better results.

## Resources

- Dataset: **Dataset for Assessing Mathematics Learning in Higher Education** from the MathE platform, hosted by the UCI Machine Learning Repository. [DOI: 10.34620/dadosipb/PW3OWY](https://doi.org/10.34620/dadosipb/PW3OWY)
- Python Libraries: `pandas` for data handling, `scikit-learn` for modeling
- **ChatGPT**: Used as a resource for understanding and implementing data science concepts and methodologies effectively throughout the project.


------
