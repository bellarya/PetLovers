servicos = []

def cadastrar_servico():
    nomeservico = input("Digite o tipo do serviço: ")
    precoservico = float(input("Digite o preço do serviço: "))
    
    servicos.append([nomeservico, precoservico])
    print("Serviço cadastrado com sucesso!")

def atualizar_servico():
    if not servicos:
        print("Não há serviços cadastrados.")
        return
    nomeservico = input("Digite o tipo do serviço para atualizar: ")
    for i in range(len(servicos)):
        if servicos[i][0] == nomeservico:
            novonome = input("Digite o novo tipo do serviço: ")
            novopreco = float(input("Digite o novo preço do serviço: "))
            servicos[i] = [novonome, novopreco]
            print("Serviço atualizado com sucesso!")
            return
    print("Serviço não encontrado.")

def apagar_servico():
    if not servicos:
        print("Não há serviços cadastrados.")
        return
    nomeservico = input("Digite o tipo do serviço para remover: ")
    for i in range(len(servicos)):
        if servicos[i][0] == nomeservico:
            del servicos[i]
            print("Serviço removido com sucesso!")
            return
    print("Serviço não encontrado.")

def consultar_servico():
    if not servicos:
        print("Não há serviços cadastrados.")
        return
    for servico in servicos:
        print(f"Tipo do serviço: {servico[0]}, Preço: R$ {servico[1]:.2f}")