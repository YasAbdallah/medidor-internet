import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
from PIL import ImageGrab

links = ['https://www.speedtest.net/', 'https://www.minhaconexao.com.br/']
caminho_root = f'C:\\Users\\{os.getlogin()}\\Desktop\\internet'
caminho_data = f'{datetime.now().year}\\{datetime.now().month}\\{datetime.now().day}'
if not os.path.exists(os.path.join(caminho_root, caminho_data)):
    os.makedirs(os.path.join(caminho_root, caminho_data))
opcoes = webdriver.EdgeOptions()
driver = webdriver.Edge(options=opcoes)
driver.maximize_window()

try:
    for link in links:
        driver.get(link)
        sleep(3)
        if link == links[0]:
            if driver.find_element(By.XPATH, '//button[text() = "Aceitar cookies" or text() = "Continue"]'):
                driver.find_element(By.XPATH, '//button[text() = "Aceitar cookies" or text() = "Continue"]').click()
            driver.find_element(By.XPATH, '//span[@class="start-text"]').click()
            sleep(45)
            if driver.find_element(By.XPATH, '//button[text() = "Close"]'):
                driver.find_element(By.XPATH, '//button[text() = "Close"]').click()
            sleep(3)
            imagem = ImageGrab.grab()
            imagem.save(os.path.join(caminho_root, caminho_data, 'speedTeste.png'))
        else:
            driver.find_element(By.XPATH, '//button[@type="button" and text()="Iniciar"]').click()
            sleep(60)
            driver.refresh()
            sleep(3)
            imagem = ImageGrab.grab()
            imagem.save(os.path.join(caminho_root, caminho_data, 'minhaConexao.png'))
except Exception as e:
    print(e)
    driver.close()
else:
    driver.close()