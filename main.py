# Projeto Integrado - Análise e Desenvolvimento de Sistemas
# 4º Semestre
# 2020.2

# Andrei Amorim de Santana - 711835-9
# Bruno Peselli Piazzi - 711575-1
# Luan Cuba - 711798-9
# Luciano Feliciano Junior - 710889-7
# Michaelly Fernanda - 712136-1
# Steffany Candalaft Duram - 713653-4

# ESCOPO DO TESTE
# • Informar um valor correto ou incorreto para a busca de CEP do Correios
# • Validar, de acordo com o resultado observado X o resultado esperado, se o teste foi atendido corretamente ou não
# • Informar a quantidade geral de testes processados
# • Informar a quantidade de testes bem sucedidos
# • Informar a quantidade de testes falhos
# • Informar a taxa de sucesso

# IMPORTS
# https://docs.python.org/3/library/os.html
import os

# https://docs.python.org/3/library/time.html
import time

# https://docs.python.org/3/library/json.html
import json

# https://docs.python.org/3/library/datetime.html
import datetime

# https://pypi.org/project/selenium/
# ATENÇÃO: Configurado para rodar com a versão 86 do Google Chrome (limitações do driver)
# Para erros de execução em ambientes não controlados, verificar a versão do navegador em chrome://version e baixar o driver adequado
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Define uma função que gera um log personalizado em tempo de execução no console
def printlog(log):
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

# Inicia a execução do script de testes
printlog("Iniciando execução")

# Busca por CEP na página dos Correios
def procura_por(cep):
    printlog("Iniciando consulta")
    browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
    assert 'Busca CEP' in browser.title, 'Site do Correios não carregou'
    caixa_de_busca = browser.find_element_by_id('endereco')
    printlog("Buscando por " + cep)
    caixa_de_busca.send_keys(cep)
    assert cep in caixa_de_busca.get_attribute('value'), 'A busca não foi inserida corretamente'
    caixa_de_busca.send_keys(Keys.RETURN)

# Define uma função que localiza (ou não) o endereço na página de resultados
# Tenta localizar por 3 vezes com timeouts, seja por tempo de carregamento da página quanto por confirmação
# Caso exista, retorna o resultado encontrado; caso contrário retorna "Não há dados a serem exibidos"
def localiza_resultado():
    logradouro_nome = "NOT FOUND"
    tentativas = 3
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

# Função responsável pela rotina de pesquisa e análise de resultado
def verifica(test):
    procura_por(test)
    resultado = localiza_resultado()
    return resultado

# Define os testes a serem executados a partir do arquivo testcases.json
# O arquivo consiste em uma estrutura (key, value) de "Teste": "Resultado esperado"
printlog("Gerando dicionário de buscas...")
with open(testcasesPath, encoding='utf-8') as testcasesFile:
    testcases = json.load(testcasesFile)
    printlog("Dicionário de buscas gerado!")
    printlog("[TESTCASES.JSON]: " + str(testcases) + "\n\n")

# Instancia as variáveis estatísticas
quantidade_de_testes = 0
quantidade_de_testes_bem_sucedidos = 0
quantidade_de_testes_falhos = 0

# Rotina de validação dos testes
printlog("INICIANDO BUSCA DE ENDEREÇOS...")
# Para cada caso de teste e seu respectivo resultado esperado a partir do arquivo "testcases.json"
for case, expected_result in testcases.items():
    printlog("[CASO DE TESTE]: " + case)
    # Verifica o teste e atribui o resultado à variável "result"
    result = verifica(case)
    printlog("[RESULTADO]: " + result)
    printlog("[RESULTADO ESPERADO]: " + expected_result)
    # Se o resultado esperado estiver contido - literalmente - no resultado real
    if expected_result in result:
        printlog("[RESULTADO DO TESTE]: SUCESSO")
        # Incrementa a quantidade de testes e adiciona um novo teste à quantidade de bem sucedidos
        quantidade_de_testes += 1
        quantidade_de_testes_bem_sucedidos += 1
    # Se o resultado esperado não estiver contido no resultado real
    else:
        printlog("[RESULTADO DO TESTE: FALHA")
        # Incrementa a quantidade de testes e adiciona um novo teste à quantidade de falhas
        quantidade_de_testes += 1
        quantidade_de_testes_falhos += 1
    print("\n")

# Define a função que calcula a taxa de sucesso da execução baseada nas estatísticas adquiridas durante o processo
def calcula_taxa_de_sucesso():
    # A taxa de sucesso é a razão dos testes bem sucedidos pela quantidade total de testes
    taxa_de_sucesso = quantidade_de_testes_bem_sucedidos/quantidade_de_testes
    return taxa_de_sucesso

# Grava as estatísticas no console
printlog("[QUANTIDADE DE TESTES PROCESSADOS]: " + str(quantidade_de_testes_bem_sucedidos + quantidade_de_testes_falhos))
printlog("[QUANTIDADE DE TESTES BEM SUCEDIDOS]: " + str(quantidade_de_testes_bem_sucedidos))
printlog("[QUANTIDADE DE TESTES FALHOS]: " + str(quantidade_de_testes_falhos))
printlog("[TAXA DE SUCESSO]: " + str(calcula_taxa_de_sucesso()*100) + "%\n\n")

# Finaliza a execução e encerra o driver
printlog("Finalizando execução")
browser.quit()