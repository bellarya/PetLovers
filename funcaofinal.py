pets = []

def cadastrar_pet():
    nomepet = input("Digite o nome do pet: ")
    donocpf = input("Digite o CPF do dono: ")
    especiepet = input("Digite a espécie do pet: ")
    racapet = input("Digite a raça do pet: ")
    
    pets.append([nomepet, donocpf, especiepet, racapet])
    print("Pet cadastrado com sucesso!")

def atualizar_pet():
    if not pets:
        print("Não há pets cadastrados.")
        return
    nomepet = input("Digite o nome do pet para atualizar: ")
    for i in range(len(pets)):
        if pets[i][0] == nomepet:
            novonome = input("Digite o novo nome do pet: ")
            donocpf = input("Digite o novo CPF do dono: ")  
            pets[i] = [novonome, donocpf, pets[i][3], pets[i][4]]
            print("Pet atualizado com sucesso!")
            return
    print("Pet não encontrado.")

def apagar_pet():
    if not pets:
        print("Não há pets cadastrados.")
        return
    nomepet = input("Digite o nome do pet para remover: ")
    for i in range(len(pets)):
        if pets[i][0] == nomepet:
            del pets[i]
            print("Pet removido com sucesso!")
            return
    print("Pet não encontrado.")

def consultar_pet():
    if not pets:
        print("Não há pets cadastrados.")
        return
    else:
        pet = input("Digite o nome do pet para consultar: ")
    
        pet_encontrado = False  
        for pet in pets:  
            if pet == pets[0]:  
                print(f"Nome: {pet[0]}, Dono: {pet[1]}, Espécie: {pet[2]}, Raça: {pet[3]}")
                pet_encontrado = True
                break
        if not pet_encontrado:
            print("Pet não encontrado.")

atendimentos = []

def iniciar_atendimento():
    if not pets:
        print("Não há pets cadastrados para atendimento.")
        return
    nomepet = input("Digite o nome do pet para iniciar o atendimento: ")
    for pet in pets:
        if pet[0] == nomepet:
            dono = pet[1]
            servico = input("Digite o serviço prestado: ")
            datatendimento = input("Digite a data do atendimento (DD/MM/AAAA): ")
            atendimentos.append([nomepet, dono, servico, datatendimento])
            print("Atendimento iniciado com sucesso!")
            return
    print("Pet não encontrado.")

def agendar_atendimento():
    if not pets:
        print("Não há pets cadastrados para agendamento.")
        return
    nomepet = input("Digite o nome do pet para agendar o atendimento: ")
    for pet in pets:
        if pet[0] == nomepet:
            dono = pet[1]
            datagendada = input("Digite a data para agendar o atendimento (DD/MM/AAAA): ")
            atendimentos.append([nomepet, dono, "Agendado", datagendada])
            print("Atendimento agendado com sucesso!")
            return
    print("Pet não encontrado.")

def remarcar_atendimento():
    if not atendimentos:
        print("Não há atendimentos agendados.")
        return
    nomepet = input("Digite o nome do pet para remarcar o atendimento: ")
    for atendimento in atendimentos:
        if atendimento[0] == nomepet:
            novadata = input("Digite a nova data para o atendimento (DD/MM/AAAA): ")
            atendimento[3] = novadata
            print("Atendimento remarcar com sucesso!")
            return
    print("Pet não encontrado ou sem atendimentos agendados.")


def consulta_relatorio_1():
    if not atendimentos:
        print("Não há atendimentos registrados.")
        return
    print("Relatório de Todos os Atendimentos:")
    for atendimento in atendimentos:
        print(f"Pet: {atendimento[0]}, Dono: {atendimento[1]}, Serviço: {atendimento[2]}, Data: {atendimento[3]}")
