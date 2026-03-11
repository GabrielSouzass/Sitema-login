from database import carregar_usuarios, salvar_usuarios

def cadastrar_usuario(nome, senha):
    usuarios = carregar_usuarios()
    
    for usuario in usuarios:
        if usuario ["nome"] == nome:
            return False
        
    usuarios.append({
        "nome": nome,
        "senha": senha
    })
    
    salvar_usuarios(usuarios)
    return True

def login(nome, senha):
    usuarios = carregar_usuarios()
    
    for usuario in usuarios:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            return True
        
    return False
        