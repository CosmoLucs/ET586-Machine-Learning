import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega dados e verifica 
df = pd.read_csv('data/raw/apple_quality.csv')
print('Linhas iniciais do dataset:')
# print(df.head())

# Tem um "erro" no database que é basicamente uma linha a mais no final do arquivo com a assinatura do autor
# Retirar a última linha antes de continuar o processo de análise
df = df.iloc[:-1] # Remover a última linha

# Comando para verificar o formato do dataset, mostra 4000, 9 com linhas e colunas respectivamente
print(df.shape)

df["Quality"] = df["Quality"].map({"good": 1, "bad": 0})

# Verificação de itens ausentes por coluna
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

# Cria histogramas para as variáveis numéricas
df[['Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness', 'Ripeness', 'Acidity']].hist(bins=20, figsize=(10, 8))
plt.show()

# Cria um boxplot para visualizar a distribuição das variáveis numéricas
sns.boxplot(data=df[['Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness', 'Ripeness', 'Acidity']])
plt.show()

# Calcula a matriz de correlação entre as variáveis e cria um heatmap para visualizá-la
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlação')
plt.show()

# Cria um boxplot para visualizar a distribuição de 'Sweetness' em relação à 'Quality'
sns.boxplot(x='Quality', y='Sweetness', data=df)
plt.title('Distribuição de Sweetness por Quality')
plt.show()

# Exibe informações gerais sobre o dataset, como o tipo de dados e a contagem de valores não nulos
print("\n📊 Informações do dataset:")
print(df.info())

# Exibe estatísticas descritivas das variáveis numéricas do dataset
print("\nEstatísticas descritivas:")
print(df.describe())

# Conta e exibe a quantidade de maçãs boas vs. ruins
print("\nContagem de maçãs boas vs. ruins:")
print(df['Quality'].value_counts())

# Cria um gráfico de barras para visualizar a distribuição de maçãs boas vs. ruins
sns.countplot(x=df['Quality'])
plt.title("Distribuição de Maçãs Boas vs. Ruins")
plt.xlabel("Categoria")
plt.ylabel("Quantidade")
plt.show()