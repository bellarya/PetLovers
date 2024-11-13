clientes = []

def cadastro_clientes():
            
        if len(clientes) == 0:
            print("Não há clientes cadastrados. Cadastre um cliente.")
            
            nomecliente = input("Digite o nome do novo cliente: ")
            senha = input("Digite a senha: ")
            cpf = int(input("Digite o CPF: "))

            clientes.append([nomecliente, senha, 'C', cpf])
            print("Cliente cadastrado com sucesso!")
    
        else:
            nomecliente = input("Digite o nome do novo cliente: ")
            senha = input("Digite a senha: ")
            cpf = int(input("Digite o CPF: "))
            for i in range (len(clientes)):
                if cpf == clientes[i][3]:
                    print("Clinte já registrado! Cadastre um novo!")
                    return False
            clientes.append([nomecliente, senha, 'C', cpf])
            print("Cliente cadastrado com sucesso!")

def login_clientes():
    global usuario_logado, tipo
    while True:
        nomecliente = input("Digite o cliente para login: ")
        senha = input("Digite a senha: ")
        for i in range(len(clientes)):
            if nomecliente == clientes[i][0] and senha == clientes[i][1]:
                usuario_logado = clientes
                tipo = 'C'
                print("Cliente autenticado.")
                return tipo
        else:
            print("Cliente ou senha inválido!")
            return None

def clientes_atualizar():
    if len(clientes) == 0:
        print("Não há clientes cadastrados.")
        return
    while True:
        nomecliente = input("Digite o nome do cliente para atualizar: ")
        for i in range(len(clientes)):
            if nomecliente == clientes[i][0]:
                novasenha = input("Digite a nova senha: ")
                clientes[i][1] = novasenha

                print("Atualização realizada com sucesso!")
                return True

            else:
                print("Cliente não encontrado.")

def apagar_cliente():
    if len(clientes) == 0:
        print("Não há clientes cadastrados.")
        return 
    while True:
        nomecliente = input("Digite o nome do cliente para remove-lo: ")
        for i in range(len(clientes)):
            if nomecliente == clientes[i][0]:
                del clientes[i]
                print("Cliente removido com sucesso!")
                return True

def consultar_cliente():
    if len(clientes) == 0:
        print("Não há clientes cadastrados.")
        return
    else:
        senhacliente = input("Digite a senha do cliente para consultar: ")
    
        cliente_encontrado = False
        for cliente in clientes:  
            if senhacliente == cliente[1]:  
                print(f"Nome: {cliente[0]}, Senha: {cliente[1]}, Tipo: {cliente[2]}, CPF: {cliente[3]}")
                cliente_encontrado = True
                break
        if not cliente_encontrado:
            print("Cliente não encontrado.")