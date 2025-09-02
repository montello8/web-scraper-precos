📦 Web Scraper de Preços
📝 Descrição

Este projeto coleta preços de produtos de um site de testes (books.toscrape.com), gera análises simples e salva os dados em planilha Excel e gráfico.
O objetivo é demonstrar habilidades em web scraping, análise de dados e visualização, perfeito para portfólio.

🚀 Tecnologias Utilizadas

Python 3

Requests → Para fazer requisições HTTP

BeautifulSoup → Para extrair informações do HTML

Pandas → Para manipulação de dados

Matplotlib → Para gerar gráficos

OpenPyXL → Para salvar arquivos Excel

📊 Funcionalidades

Coleta nome e preço de produtos

Calcula a média de preços

Identifica o produto mais caro e o mais barato

Exporta planilha Excel (precos.xlsx)

Gera gráfico de preços (grafico_precos.png)

📂 Estrutura do Projeto
WebScraperPrecos/
│
├─ scraper.py           # Código principal do web scraper
├─ precos.xlsx          # Planilha gerada (após rodar o script)
├─ grafico_precos.png   # Gráfico gerado (após rodar o script)
├─ requirements.txt     # Dependências do projeto
├─ README.md            # Documentação do projeto
└─ .gitignore           # Arquivos ignorados pelo Git

▶️ Pré-requisitos

Python 3 instalado (download aqui
)

Git instalado (download aqui
)

▶️ Como executar

Clonar o repositório

git clone https://github.com/SEU_USUARIO/web-scraper-precos.git
cd web-scraper-precos


Criar ambiente virtual

python -m venv venv


Ativar ambiente virtual

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate


Instalar dependências

pip install -r requirements.txt


Executar o script

python scraper.py

📊 Exemplos de saída

No terminal

📊 Análises dos preços:
Média dos preços: £35.79
Mais caro: Livro X (£53.74)
Mais barato: Livro Y (£21.45)
📂 Planilha 'precos.xlsx' gerada com sucesso!


Planilha Excel (precos.xlsx)

Produto	Preço
Livro A	51.77
Livro B	23.45
...	...

Gráfico (grafico_precos.png)
Gráfico de barras com preços de todos os produtos coletados.

📌 Observações

O site usado é de teste, seguro para web scraping.

Para sites reais, pode ser necessário usar Selenium se o conteúdo for carregado dinamicamente.

O projeto pode ser expandido para coletar várias páginas, gerar relatórios históricos, ou integrar com Power BI.

🛠️ Criar requirements.txt

No terminal do VS Code:

pip freeze > requirements.txt
