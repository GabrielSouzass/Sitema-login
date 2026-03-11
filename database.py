import json

ARQUIVO = "usuarios.json"

def carregar_usuarios():
    try:
        with open(ARQUIVO, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
    
def salvar_usuarios(usuarios):
    with open (ARQUIVO, "w") as file:
        json.dump(usuarios, file, indent=4)