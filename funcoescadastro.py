usuarios = [['Adm', '4321', 'A']] # adm base para iniciar com o login 

def cadastro_usuarios():
        
        if len(usuarios) == 0:
            print("Não há usuários funcionários. Cadastre um funcionário.")
        
            nomeusuario = input("Digite o nome do novo funcionário: ")
            senha = input("Digite a senha: ")

            usuarios.append([nomeusuario, senha, 'A'])
            print("funcionários cadastrado com sucesso!")

        else:
            nomeusuario = input("Digite o nome do novo funcionário: ")
            senha = input("Digite a senha: ")

            usuarios.append([nomeusuario, senha, 'A'])
            print("Funcionário cadastrado com sucesso!")

def login_usuario():
    global usuario_logado, tipo
    while True:
        nomeusuario = input("Digite o funcionário para login: ")
        senha = input("Digite a senha: ")
        for i in range(len(usuarios)):
            if nomeusuario == usuarios[i][0] and senha == usuarios[i][1]:
                usuario_logado = usuarios
                tipo = 'A'
                print("Funcionário autenticado.")
                return tipo
        else:
            print("Funcionário ou senha inválido!")
            return None

def usuario_atualizar():
    if len(usuarios) == 0:
        print("Não há funcionários cadastrados.")
        return
    while True:
        nomeusuario = input("Digite o nome do funcionário para atualizar: ")
        for i in range(len(usuarios)):
            if nomeusuario == usuarios[i][0]:
                novasenha = input("Digite a nova senha: ")
                usuarios[i][1] = novasenha 

                print("Atualização realizada com sucesso!")
                return True

            else:
                print("Funcionário não encontrado.")
                return False

def apagar_usuario():
    if len(usuarios) == 0:
        print("Não há funcionários cadastrados.")
        return 
    while True:
        nomeusuario = input("Digite o nome do funcionário para remove-lo: ")
        for i in range(len(usuarios)):
            if nomeusuario == usuarios[i][0]:
                del usuarios[i]
                print("Funcionário removido com sucesso!")
                return True

def consultar_usuarios():
    if len(usuarios) == 0:
        print("Não há funcionários cadastrados.")
        return

    print("Funcionários cadastrados: ")
    for i in usuarios:
        print(f"Nome: {i[0]}, Senha: {i[1]}, Tipo: {i[2]}")