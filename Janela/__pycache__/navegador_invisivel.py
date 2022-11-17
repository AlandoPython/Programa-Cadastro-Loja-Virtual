from PySimpleGUI import PySimpleGUI as sg
from time import sleep
import os
# SELENIUM ===================================================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--headless")
# ==========================================================================================
from bs4 import BeautifulSoup
import requests

# ==========================================================================================

#   LAYOUT
sg.theme('Reddit')
botao = [
    [sg.Button('Cadastrar\nProduto', size=(16, 2)), sg.Button('Novo\nProduto', size=(16, 2)),
     sg.Button('Finalizar\nPrograma', size=(16, 2))],
]
layout1 = [
    [sg.Text('                          Hora de cadastrar os produtos!')],
    [sg.Text('Nome   '), sg.Input(key='nome')],
    [sg.Text('GTIN    '), sg.Input(key='gtin')],
    [sg.Text('Peso    '), sg.Input(key='peso')],
    [sg.Text('Preço   '), sg.Input(key='preco')],
    [sg.Text('Link/Url'), sg.Input(key='url'), sg.Button('Buscar')],
    [sg.Text('                          Janela de Saída - Editar Descrição')],
    [sg.Output(size=(60, 20), key='descricao')],
    [botao]
]

#   JANELA
janela1 = sg.Window('Cadastro', layout1)

#   EVENTOS
sg.popup('Atenção!!! O navegador será aberto!')
nav = webdriver.Chrome(service=service, options=options)
nav.get('https://www.mercadolivre.com.br/')
sleep(5)
# ------------------------------------------------------------------------
eventos, valores = janela1.read()
while not eventos == sg.WINDOW_CLOSED or eventos == 'Finalizar\nPrograma':
    eventos, valores = janela1.read()
    if eventos == sg.WINDOW_CLOSED or eventos == 'Finalizar\nPrograma':
        print('Programa Finalizado')
        nav.close()
        break

    if eventos == 'Buscar':
        while True:
            if not 'https://' in valores['url'] :
                sg.popup('ERRO!!! Insira um Link para iniciar uma busca.')
                eventos, valores = janela1.read()
            if eventos == 'Novo\nProduto':
                janela1['nome']('')
                janela1['gtin']('')
                janela1['peso']('')
                janela1['preco']('')
                janela1['url']('')
                janela1['descricao']('')
                os.system('cls')
                eventos, valores = janela1.read()
            if eventos == sg.WINDOW_CLOSED or eventos == 'Finalizar\nPrograma':
                print('Programa Finalizado')
                nav.close()
                break
            if 'https://' in valores['url']:
                nav.get(valores['url'])
                break


        #   DESCRIÇÃO =====================================================================================
        try:
            dsc = nav.find_element(By.XPATH, '//*[@id="description"]/div/p').text
            janela1['descricao']('')
            # print(dsc)
        except:
            dsc = nav.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[1]/div/div[6]/div/div/p').text
            janela1['descricao']('')
            # print(dsc)

        #   FOTOS =========================================================================================
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
        url = valores['url']
        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        # -------------------------------------------------------------------------------------
        fotos = []
        elemento = soup.find_all('div', class_='ui-pdp-thumbnail__picture')
        os.system('cls')
        if len(elemento) > 8:
            elemento = elemento[:7]
        try:
            for c in range(1, len(elemento)):
                elm = str(elemento[c])
                url = elm[elm.index('data-srcset="') + 13:]
                url = url[:url.index('"', 2)]
                print(f'Foto {c} - {url}')
                fotos.append(url)
        except:
            c += 1
        foto_capa = elemento[0]
        #   PRINT DOS RESULTADOS
        if len(fotos) > 0:
            print(f'Fotos: OK! - {len(fotos)} Fotos.')
        else:
            print('Fotos: FALHA!')
        print('=' * 52)
        print('Descrição:')
        print('')
        print(dsc)

    if eventos == 'Novo\nProduto':
        janela1['nome']('')
        janela1['gtin']('')
        janela1['peso']('')
        janela1['preco']('')
        janela1['url']('')
        janela1['descricao']('')
        os.system('cls')


