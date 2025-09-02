# 📦 Web Scraper de Preços

Este projeto coleta preços de produtos de um site de testes (books.toscrape.com), 
gera análises simples e salva os dados em Excel + gráfico.

## 🚀 Tecnologias
- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib

## 📊 Funcionalidades
- Coleta nome e preço de produtos
- Calcula média de preços
- Identifica produto mais caro e mais barato
- Exporta planilha Excel (`precos.xlsx`)
- Gera gráfico de preços (`grafico_precos.png`)

## ▶️ Como executar
1. Clone o repositório
   ```bash
   git clone https://github.com/SEU_USUARIO/web-scraper-precos.git
   cd web-scraper-precos
Crie ambiente virtual

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale dependências

bash
Copiar código
pip install -r requirements.txt
Rode o script

bash
Copiar código
python scraper.py
📂 Saídas
precos.xlsx → Planilha com dados

grafico_precos.png → Gráfico dos preços

yaml
Copiar código

---

## 4. Criar requirements.txt
No terminal:
```bash
pip freeze > requirements.txt