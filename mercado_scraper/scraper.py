from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def buscar_produtos(termo, quantidade):
    options = Options()
    options.add_argument("--headless")
    navegador = webdriver.Chrome(options=options)
    url = f"https://www.mercadolivre.com.br/"
    navegador.get(url)
    time.sleep(2)

    barra_pesquisa = navegador.find_element(By.NAME, "as_word")
    barra_pesquisa.send_keys(termo)
    barra_pesquisa.submit()
    time.sleep(3)

    produtos = []
    itens = navegador.find_elements(By.CSS_SELECTOR, ".ui-search-result__wrapper")[:quantidade]

    for item in itens:
        try:
            nome = item.find_element(By.CSS_SELECTOR, "h2").text
            preco = item.find_element(By.CSS_SELECTOR, ".price-tag .price-tag-fraction").text
            produtos.append({"nome": nome, "preco": preco})
        except:
            continue

    navegador.quit()
    return produtos
