import os
import shutil

def organizar_pastas(diretorio):
    for arquivo in os.listdir(diretorio):
        nome, extensao = os.path.splitext(arquivo)
        if extensao:
            pasta_destino = os.path.join(diretorio, extensao[1:])
            os.makedirs(pasta_destino, exist_ok=True)
            shutil.move(os.path.join(diretorio, arquivo), pasta_destino)

organizar_pastas("C:/caminho/para/sua/pasta")
