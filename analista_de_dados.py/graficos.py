import pandas as pd
import matplotlib.pyplot as plt
dados = {
    "Produto":["Celular", "Videogame", "Fone de ouvido", "Mouse", "Teclado"],
    "Preço":[700, 1200, 245, 60, 125],
    "Quantidade Vendida":[65, 56, 42, 37, 72]

}

df = pd.DataFrame(dados)


df["Faturamento"] = df["Preço"] * df["Quantidade Vendida"]

plt.figure(figsize=(8,5))
plt.bar(df["Produto"], df['Faturamento'], color="purple")

plt.title("Faturamento")
plt.xlabel("Produto")
plt.ylabel("Faturamento em dinheiro")
plt.show()