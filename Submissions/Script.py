import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the CSV file with a different encoding
df = pd.read_csv('../MathE dataset (4).csv', encoding='ISO-8859-1', delimiter=';')

# Display the first few rows to ensure it loaded correctly
print(df.info())  # Overview of columns, data types, and missing values
print(df.head())

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Drop duplicates if any are found
if duplicates > 0:
    df = df.drop_duplicates()

# Standardize text columns to lowercase
df['Student Country'] = df['Student Country'].str.lower()
df['Question Level'] = df['Question Level'].str.lower()
df['Topic'] = df['Topic'].str.lower()
df['Subtopic'] = df['Subtopic'].str.lower()
df['Keywords'] = df['Keywords'].str.lower()

# Define features (X) and target (y)
X = df[['Question Level', 'Topic', 'Subtopic', 'Student Country']]
y = df['Type of Answer']

# One-hot encode categorical columns
X = pd.get_dummies(X, columns=['Question Level', 'Topic', 'Subtopic', 'Student Country'])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model2 = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)
model2.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)
y_pred2 = model2.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
accuracy2 = accuracy_score(y_test, y_pred2)

print(f"Model Accuracy: {accuracy:.2f}")
print(f"Model Accuracy: {accuracy2:.2f}")

