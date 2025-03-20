import pandas as pd

dataFrame = pd.read_csv('data/raw/apple_quality.csv') 

# Altera o último valor da coluna 'Quality' colocando números para melhor identificação
dataFrame["Quality"] = dataFrame["Quality"].map({"good": 1, "bad": 0})

dataFrame = dataFrame.iloc[:-1] # Remover a última linha 

indVar = dataFrame.drop('Quality', axis=1)
depVar = dataFrame['Quality']

from sklearn.model_selection import train_test_split
dataFrame_train, dataFrame_test, Y_train, Y_test = train_test_split(indVar, depVar, test_size = 0.2, random_state = 42)

dataFrame_test.to_csv("data/processed/apple_quality_test.csv", index=False)
dataFrame_train.to_csv("data/processed/apple_quality_train.csv", index=False)