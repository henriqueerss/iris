from sklearn.datasets import load_iris

# Carregando o dataset;
iris = load_iris()

# Acessando dados e rótulos;
x, y, name = iris.data, iris.target, iris.feature_names

print("\n\n\n\n\n\nCaracterísticas:\n", x[:5])

print("\n\n\nRótulos:\n", y[:5])

print("\n\n\nNome das características:\n", name)

# Acessando metadados;
print("Metadados:\n\n", iris.DESCR)