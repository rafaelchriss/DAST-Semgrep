import subprocess
import pickle

password = "Admin123456!"

comando = input("Digite um comando: ")

subprocess.call(comando, shell=True)

dados = input("Digite dados serializados: ")
pickle.loads(dados.encode())
