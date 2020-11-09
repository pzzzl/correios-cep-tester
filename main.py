# https://pypi.org/project/selenium/

# IMPORTS
import os
import time
import json
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException



# /IMPORTS

def printlog(log):
    # datetime.datetime.now()
    print(str(datetime.datetime.now()) + " -- " + log)

# Define o local do arquivo
printlog("Definindo caminho de execução")
path = os.getcwd()
printlog("Caminho: " + path)

# Define o local do arquivo de testes
printlog("Definindo caminho do arquivo de testes")
testcasesPath = path + "/testcases.json"
printlog("Arquivo de testes: " + testcasesPath)

# Define o local do Chromedriver
printlog("Definindo caminho do Chromedriver.exe")
chromedriverPath = path + '/chromedriver.exe'
printlog("Caminho: " + chromedriverPath)

# Define as opções utilizadas no driver
# A única opção relevante para a execução é a de omitir os logs padrão da ferramenta, afinal serão gerados logs personalizados
printlog("Definindo opções do driver")
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Instancia o Google Chrome com as opções fornecidas e o caminho onde está localizado
printlog("Instanciando Google Chrome")
browser = webdriver.Chrome(options=options, executable_path=chromedriverPath)
printlog("Chrome instanciado com sucesso e opções aceitas. Continuando...")


printlog("Iniciando execução")


def procura_por(endereco):
    printlog("Iniciando consulta")
    browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
    assert 'Busca CEP' in browser.title, 'Site do Correios não carregou'
    caixa_de_busca = browser.find_element_by_id('endereco')
    printlog("Buscando por " + endereco)
    caixa_de_busca.send_keys(endereco)
    assert endereco in caixa_de_busca.get_attribute('value'), 'A busca não foi inserida corretamente'
    caixa_de_busca.send_keys(Keys.RETURN)

    

def localiza_resultado():
    logradouro_nome = "NOT FOUND"
    tentativas = 5
    while tentativas > 0:
        try:
            time.sleep(0.5)
            logradouro_nome = browser.find_element_by_xpath('//*[@id="resultado-DNEC"]/tbody/tr/td[1]')
            tentativas = 0
        except NoSuchElementException:
            tentativas -= 1
            printlog("Resultado não encontrado. Número de tentativas restantes: " + str(tentativas))
            time.sleep(0.5)
    if logradouro_nome != "NOT FOUND":
        resultado_encontrado = logradouro_nome.get_attribute('innerText')
        return resultado_encontrado
    else:
        message = "Não há dados a serem exibidos"
        return message

def verifica(test):
    procura_por(test)
    resultado = localiza_resultado()
    return resultado


printlog("Gerando dicionário de buscas...")
with open(testcasesPath, encoding='utf-8') as testcasesFile:
    testcases = json.load(testcasesFile)
    printlog("Dicionário de buscas gerado!")
    printlog("[TESTCASES.JSON]: " + str(testcases) + "\n\n")

quantidade_de_testes = 0
quantidade_de_testes_bem_sucedidos = 0
quantidade_de_testes_falhos = 0

printlog("INICIANDO BUSCA DE ENDEREÇOS...")
for case, expected_result in testcases.items():
    printlog("[CASO DE TESTE]: " + case)
    result = verifica(case)
    printlog("[RESULTADO]: " + result)
    printlog("[RESULTADO ESPERADO]: " + expected_result)
    if expected_result in result:
        printlog("[RESULTADO DO TESTE]: SUCESSO")
        quantidade_de_testes += 1
        quantidade_de_testes_bem_sucedidos += 1
    else:
        printlog("[RESULTADO DO TESTE: FALHA")
        quantidade_de_testes += 1
        quantidade_de_testes_falhos += 1
    print("\n")

def calcula_taxa_de_sucesso():
    taxa_de_sucesso = quantidade_de_testes_bem_sucedidos/quantidade_de_testes
    return taxa_de_sucesso

printlog("[TAXA DE SUCESSO]: " + str(calcula_taxa_de_sucesso()*100) + "%")

browser.quit()