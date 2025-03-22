import pandas as pd
from sklearn.model_selection import train_test_split

# Load data
dataFrame = pd.read_csv('data/raw/apple_quality.csv')

# Convert "Quality" from categorical to numerical
dataFrame["Quality"] = dataFrame["Quality"].map({"good": 1, "bad": 0})

# Remove the last row
dataFrame = dataFrame.iloc[:-1]

# Separate independent (X) and dependent (Y) variables
indVar = dataFrame.drop('Quality', axis=1)
depVar = dataFrame['Quality']

# Split into train and test sets
X_train, X_test, Y_train, Y_test = train_test_split(indVar, depVar, test_size=0.2)

# Combine X and Y before saving
train_data = X_train.copy()
train_data["Quality"] = Y_train  # Add target column back

test_data = X_test.copy()
test_data["Quality"] = Y_test  # Add target column back

# Save the processed train and test sets
train_data.to_csv("data/processed/apple_quality_train.csv", index=False)
test_data.to_csv("data/processed/apple_quality_test.csv", index=False)
