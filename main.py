import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from PIL import ImageGrab

links = ['https://www.speedtest.net/', 'https://www.minhaconexao.com.br/']
caminho_root = f'C:\\Users\\{os.getlogin()}\\Desktop\\internetVett'
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
            driver.find_element(By.XPATH, '//span[@class="start-text"]').click()
            sleep(45)
            imagem = ImageGrab.grab()
            imagem.save(os.path.join(caminho_root, caminho_data, 'speedTeste.png'))
        else:
            driver.find_element(By.XPATH, '//button[@type="button" and text()="Iniciar"]').click()
            sleep(45)
            imagem = ImageGrab.grab()
            imagem.save(os.path.join(caminho_root, caminho_data, 'minhaConexao.png'))
except Exception as e:
    print(e)
    driver.close()
    driver.quit()
else:
    driver.close()
    driver.quit()
