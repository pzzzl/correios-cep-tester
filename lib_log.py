# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# https://docs.python.org/3/library/sys.html
import sys

# https://docs.python.org/3/library/os.html
import os

# https://docs.python.org/3/library/codecs.html
import codecs

path = os.getcwd()
logs_path = path + "/logs"
log_filename = datetime.now().strftime("%H-%M-%S %d-%m-%Y") + ".log"
log_filepath = logs_path + "/" + log_filename

print("Definindo local do script")
scriptpath = path + "/main.py"
print("Caminho: \"" + scriptpath + "\"\n")

# Define a pasta de log
print("Definindo caminho da pasta de logs")
print("Caminho: \"" + logs_path + "\"\n")

# Verifica se a pasta de log existe
print("Verificando se a pasta de logs existe")
existe_pasta_de_logs = os.path.isdir(logs_path)
print("Resultado: " + str(existe_pasta_de_logs) + "\n")

# Cria a pasta de log caso não existir
if(not existe_pasta_de_logs):
    print("Criando pasta de logs")
    try:
        os.mkdir(logs_path)
        print("Pasta de logs criada com sucesso\n")
    except:
        print("Erro ao criar pasta de logs")
        sys.exit()

def escreve_arquivo_de_log(log):
    open(log_filepath, "a", encoding="utf-8").write(log + "\n")

# Define uma função que gera um log personalizado em tempo de execução no console
def printlog(log):
    # Se o log informado for uma linha em branco, adiciona a linha ao conjunto de logs e imprime na tela uma linha em branco
    if log == "\n":
        escreve_arquivo_de_log(log)
        print(log)
    else:
        # Imprime um log temporizado caso exista de fato uma mensagem a ser exibida
        agora = datetime.now()
        format_agora = agora.strftime("%H:%M:%S %d/%m/%Y")
        log_temporizado = format_agora + " | " + log
        escreve_arquivo_de_log(log_temporizado)
        print(log_temporizado)