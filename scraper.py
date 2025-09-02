import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

url = "http://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url)
response.encoding = "utf-8"  # força UTF-8
soup = BeautifulSoup(response.text, "html.parser")

produtos = soup.find_all("article", class_="product_pod")

dados = []
for p in produtos:
    titulo = p.h3.a["title"]
    preco = p.find("p", class_="price_color").text
    preco = re.sub(r"[^0-9.]", "", preco)  # mantém só números e ponto
    preco = float(preco)
    dados.append({"Produto": titulo, "Preço": preco})
dados.append({"Produto": titulo, "Preço": preco})


df = pd.DataFrame(dados)


preco_medio = df["Preço"].mean()
mais_caro = df.loc[df["Preço"].idxmax()]
mais_barato = df.loc[df["Preço"].idxmin()]

print("📊 Análises dos preços:")
print(f"Média dos preços: £{preco_medio:.2f}")
print(f"Mais caro: {mais_caro['Produto']} (£{mais_caro['Preço']})")
print(f"Mais barato: {mais_barato['Produto']} (£{mais_barato['Preço']})")


df.to_excel("precos.xlsx", index=False)
print("📂 Planilha 'precos.xlsx' gerada com sucesso!")


plt.figure(figsize=(10,6))
plt.bar(df["Produto"], df["Preço"])
plt.xticks(rotation=90)
plt.title("Preços dos Produtos")
plt.ylabel("Preço (£)")
plt.tight_layout()
plt.savefig("grafico_precos.png")
plt.show()
