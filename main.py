import os

from lib.navegacao import Navegar
from time import sleep
from datetime import datetime
from PIL import ImageGrab

LINKS = ['https://www.speedtest.net/', 'https://www.minhaconexao.com.br/']
CAMINHO_USUARIO = f'C:\\Users\\{os.getlogin()}\\Desktop\\internet'
PASTA_DATA_ATUAL = f'{datetime.now().year}\\{datetime.now().month}\\{datetime.now().day}'

if not os.path.exists(os.path.join(CAMINHO_USUARIO, PASTA_DATA_ATUAL)):
    os.makedirs(os.path.join(CAMINHO_USUARIO, PASTA_DATA_ATUAL))
    
driver = Navegar("D:\scripts\webDriver")
try:
    for link in LINKS:
        driver.abrirSite(link)
        sleep(3)
        if link == LINKS[0]:
            driver.navegar('//button[text() = "Aceitar cookies" or text() = "Continue"]')
            sleep(3)
            driver.navegar('//span[@class="start-text"]')
            sleep(45)
            driver.navegar('//button[text() = "Close"]')

            sleep(3)
            imagem = ImageGrab.grab()
            imagem.save(os.path.join(CAMINHO_USUARIO, PASTA_DATA_ATUAL, 'speedTeste.png'))
        else:
            driver.navegar('//button[@type="button" and text()="Iniciar"]')
            sleep(60)
            imagem = ImageGrab.grab()
            imagem.save(os.path.join(CAMINHO_USUARIO, PASTA_DATA_ATUAL, 'minhaConexao.png'))
except Exception as e:
    driver.fecharNavegador()
else:
    driver.fecharNavegador()