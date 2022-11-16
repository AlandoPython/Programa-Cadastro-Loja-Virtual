from time import sleep
# SELENIUM ===================================================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys
# ==========================================================================================
#   ABRIR NAVEGADOR
nav = webdriver.Chrome(service=service)
#   ENTRANDO NO SITE DA REVAL
nav.get('https://www.mercadolivre.com.br')
#   DESCRIÇÃO =======================================================================================
descricao = nav.find_element(By.XPATH, '//*[@id="description"]/div/p').text

