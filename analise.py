import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = {
    "mes": ["jan", "fev", "mar", "abr", "maio", "jun", "jul", "ago", "set", "out"],
    "total_vendas": [150, 178, 300, 456, 400, 588, 671, 898, 1053, 1295]
}
df_mensal = pd.DataFrame(data)

plt.figure(figsize=(6,4))
sns.barplot(x="mes", y="total_vendas", data=df_mensal, palette="flare")
plt.title("Total de vendas por mês")
plt.ylabel("Total de Vendas")
plt.xlabel("Meses")
plt.savefig("img/total_vendas")
plt.show()

category_data = pd.DataFrame({
    "categoria": ["Eletrônicos", "Maquiagem", "Vestuário"],
    "vendas": [23000, 11000, 19000]
})

plt.figure(figsize=(6,4))
sns.barplot(x="categoria", y="vendas", data=category_data, palette="rocket")
plt.title("Vendas de produtos por categoria")
plt.ylabel("Total de vendas")
plt.xlabel("Categorias")
plt.savefig("img/produtos_categoria")
plt.show()

dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
avg_vendas = [430, 460, 490, 540, 530, 580, 620]
df_dias = pd.DataFrame({"Dia": dias, "Vendas": avg_vendas})

plt.figure(figsize=(6,4))
sns.lineplot(x="Dia", y="Vendas", data=df_dias, marker="o", color="green")
plt.title("Vendas por dia da semana")
plt.ylabel("Média das vendas")
plt.xlabel("Dias da Semana")
plt.savefig("img/vendas_semana")
plt.show()