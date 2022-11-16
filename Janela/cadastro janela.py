from PySimpleGUI import PySimpleGUI as sg
from time import sleep
# SELENIUM ===================================================================================
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# ==========================================================================================

#   LAYOUT
sg.theme('Reddit')
layout1 = [
    [sg.Text('BEM VINDO Á SMT STORE!!!')],
    [sg.Text('Escolha uma das opções abaixo para prosseguir')],
    [sg.Button('Cadastrar\nProdutos', size= (0,2)), sg.Button('Finalizar\nPrograma', size= (0,2))]
]

layout2 = [
    [sg.Text('Cadastro de Produtos')],
    [sg.Text('Vamos cadastrar novos produtos\napós clicar em "Abrir Navegador"\no seu navegador irá ser aberto e\nnele você irá pesquisar o produto\ncorrespondente para  cadastro.')],
    [sg.Button('Abrir \nNavegador', size= (0,2)), sg.Button('Finalizar\nPrograma', size= (0,2))]
]

botao = [
    [sg.Button('Cadastrar\nProduto', size=(12, 2)), sg.Button('Voltar', size=(12, 2)), sg.Button('Tela Inicial', size=(12, 2)), sg.Button('Finalizar Programa', size=(12, 2))],
] 
layout3 = [
    [sg.Text('                          Hora de cadastrar os produtos!')],
    [sg.Text('Nome   '), sg.Input(key='nome')],
    [sg.Text('GTIN    '), sg.Input(key='gtin')],
    [sg.Text('Peso    '), sg.Input(key='peso')],
    [sg.Text('Preço   '), sg.Input(key='preco')],
    [sg.Text('Link/Url'), sg.Input(key='url'), sg.Button('Buscar')],
    [sg.Text('                          Janela de Saída - Editar Descrição')],
    [sg.Output(size=(60,20))],
    [botao]  
]

botao = [
    [sg.Button('Cadastrar\nProduto', size=(12, 2)), sg.Button('Voltar', size=(12, 2)), sg.Button('Tela Inicial', size=(12, 2)), sg.Button('Finalizar Programa', size=(12, 2))],
] 
layout4 = [ 
    [sg.Text('                          Janela de Saída - Editar Descrição')],
    [sg.Output(size=(60,20))],
    [botao]    
]   


#   JANELA
janela1 = sg.Window('Bem Vindo', layout1)
janela2 = sg.Window('Cadastro', layout2)
janela3 = sg.Window('Hora de Cadastrar', layout3, finalize= True)
janela4 = sg.Window('Outport', layout4)



#   EVENTOS
while True:
    eventos, valores = janela1.read()
    if eventos == sg.WINDOW_CLOSED or eventos == 'Finalizar\nPrograma':
        print('Programa Finalizado')
        break

    if eventos == 'Cadastrar\nProdutos':
        janela1.Close()
        eventos, valores = janela2.read()
        if eventos == 'Abrir \nNavegador':
            nav = webdriver.Chrome(service=service)
            nav.maximize_window()
            #   ABRIR NO SITE DO MERCADO LIVRE
            nav.get('https://www.mercadolivre.com.br')
            janela2.Close()
            eventos, valores = janela3.read()
            if eventos == 'Buscar':
                try:
                    descricao = nav.find_element(By.XPATH, '//*[@id="description"]/div/p').text
                    print(descricao)
                except:
                    descricao = nav.find_element(By.XPATH, '//*[@id="description"]/div/p').text
                    print(descricao)
            
            
