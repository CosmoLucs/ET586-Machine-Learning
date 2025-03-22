import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# 1️⃣ Carregar os dados processados
train_data = pd.read_csv("data/processed/apple_quality_train.csv")
test_data = pd.read_csv("data/processed/apple_quality_test.csv")

# 2️⃣ Separar X e Y
X_train = train_data.drop("Quality", axis=1)
Y_train = train_data["Quality"]

X_test = test_data.drop("Quality", axis=1)
Y_test = test_data["Quality"]

# 3️⃣ Criar o modelo Naïve Bayes
nb_model = GaussianNB()

# Treinar o modelo
nb_model.fit(X_train, Y_train)

# Fazer previsões no conjunto de teste
predictions = nb_model.predict(X_test)

# Avaliar o modelo
accuracy = accuracy_score(Y_test, predictions)
print(f"Acurácia: {accuracy}\n")
print("Relatório de classificação:\n", classification_report(Y_test, predictions))
