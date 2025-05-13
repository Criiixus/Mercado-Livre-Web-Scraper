# 🛒 Mercado Livre Web Scraper

Um projeto em Python com Flask para automatizar a coleta de dados de produtos no site Mercado Livre, utilizando Web Scraping com Selenium. O sistema permite buscar qualquer item, exibir os resultados em uma interface web interativa, calcular o preço médio e salvar os dados em um banco de dados SQLite.

## 📌 Funcionalidades

- 🔎 Busca de produtos por nome
- 📄 Exibição dos resultados em uma tabela dinâmica
- 💰 Cálculo do valor médio dos produtos encontrados
- 🛍️ Coleta de informações como:
  - Nome do produto
  - Preço
  - Vendedor
  - Quantidade de parcelas
  - Avaliação
  - Cupom de desconto (se houver)
- 🗃️ Armazenamento em banco de dados SQLite
- 👨‍💻 Interface web simples e funcional
- ⚙️ Seleção da quantidade de itens a capturar

## 🧰 Tecnologias Utilizadas

- Python 3.x
- Flask
- Selenium
- SQLite
- HTML/CSS
- Bootstrap (opcional)

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python instalado na máquina
- Google Chrome + ChromeDriver compatível
- Instalar as dependências com:

```bash
pip install -r requirements.txt
