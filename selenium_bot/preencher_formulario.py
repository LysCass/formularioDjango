from selenium import webdriver
from selenium.webdriver.common.by import By
import time

dados = [
    {"nome": "João Silva", "email": "joao@email.com", "mensagem": "Olá, isso é um teste."},
    {"nome": "Maria Oliveira", "email": "maria@email.com", "mensagem": "Mensagem automatizada 2."},
    {"nome": "Carlos Santos", "email": "carlos@email.com", "mensagem": "Mensagem automatizada 3."}
]

for entrada in dados:
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/")
    time.sleep(1)
    driver.find_element(By.NAME, "nome").send_keys(entrada["nome"])
    driver.find_element(By.NAME, "email").send_keys(entrada["email"])
    driver.find_element(By.NAME, "mensagem").send_keys(entrada["mensagem"])
    driver.find_element(By.XPATH, '//button[text()="Enviar"]').click()
    time.sleep(2)
    driver.quit()
