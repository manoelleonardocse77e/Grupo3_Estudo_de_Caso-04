import csv

def cadastrar_funcionario():
    nome = input("Nome do Funcionário:\n")
    cpf = input("CPF do Funcionário:\n")
    cargo = input("Cargo do Funcionário:\n")
    historico = input("Histórico do Funcionário:\n")
    turno = input("Turno do Funcionário\n")
    hora = 0
    desempenho = 0

    cadastro = {
        "CPF": cpf,
        "Nome": nome,
        "Cargo": cargo,
        "Historico": historico,
        "Turno": turno,
        "Horas": hora,
        "Desempenho": desempenho
    }

    salva_cadastro(cadastro)

def salva_cadastro(cadastro):
    fieldnames = ["Nome", "CPF", "Cargo", "Historico", "Turno", "Horas", "Desempenho"]

    with open("CadastroFuncionarios.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(cadastro)

def gerenciar_funcionario():
    menu = int(input("1- Gerenciar Escala de Trabalho\n2- Registro de Horas\n3- Avaliação de Desempenho\n"))

    if menu == 1:
        nome = input("Nome do Funcionário:\n")
        alterar_escala(nome)

    elif menu == 2:
        nome = input("Nome do Funcionário:\n")
        registrar_horas(nome)
    
    elif menu == 3:
        nome = input("Nome do Funcionário:\n")
        registrar_desempenho(nome)

def registrar_desempenho(nome_funcionario):
    linhas_atualizadas = []

    with open('CadastroFuncionarios.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        cabecalho = leitor_csv.fieldnames

        for linha in leitor_csv:
            if linha['Nome'] == nome_funcionario:
                novo_desempenho = int(input(f"Nova Nota do Desempenho de{nome_funcionario}:\n"))
                linha["Desempenho"] = novo_desempenho

            linhas_atualizadas.append(linha)

    escrever_csv(linhas_atualizadas, cabecalho)

def registrar_horas(nome_funcionario):
    linhas_atualizadas = []

    with open('CadastroFuncionarios.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        cabecalho = leitor_csv.fieldnames

        for linha in leitor_csv:
            if linha['Nome'] == nome_funcionario:
                try:
                    horas_atuais = int(linha["Horas"])
                except ValueError:
                    horas_atuais = 0

                novo_turno = int(input(f"Quantas horas a mais para {nome_funcionario}?\n"))
                nova_quantidade_horas = horas_atuais + novo_turno
                linha["Horas"] = nova_quantidade_horas

            linhas_atualizadas.append(linha)

    escrever_csv(linhas_atualizadas, cabecalho)

def alterar_escala(nome_funcionario):
    linhas_atualizadas = []

    with open('CadastroFuncionarios.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        cabecalho = leitor_csv.fieldnames

        for linha in leitor_csv:
            if linha['Nome'] == nome_funcionario:
                novo_turno = input(f"Novo Turno para {nome_funcionario}:\n")
                linha["Turno"] = novo_turno

            linhas_atualizadas.append(linha)

    escrever_csv(linhas_atualizadas, cabecalho)

def escrever_csv(linhas, cabecalho):
    with open('CadastroFuncionarios.csv', 'w', newline='') as arquivo_csv:
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
        escritor_csv.writeheader()
        escritor_csv.writerows(linhas)

def acessar_funcionario():
    nome_funcionario = input("Digite o nome do funcionário:\n")
    
    with open('CadastroFuncionarios.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        
        for linha in leitor_csv:
            if linha['Nome'] == nome_funcionario:
                print("\nInformações do Funcionário:")
                print(f"Nome: {linha['Nome']}")
                print(f"CPF: {linha['CPF']}")
                print(f"Cargo: {linha['Cargo']}")
                print(f"Histórico: {linha['Historico']}")
                print(f"Turno: {linha['Turno']}")
                print(f"Horas Trabalhadas: {linha['Horas']}")
                print(f"Desempenho: {linha['Desempenho']}")
                return

        print(f"Funcionário com o nome '{nome_funcionario}' não encontrado.")

menu = int(input("1- Cadastrar Funcionário\n2- Gerenciar Funcionário\n3- Acessar Informações do Funcionário\n"))

if menu == 1:
    cadastrar_funcionario()
elif menu == 2:
    gerenciar_funcionario()
elif menu == 3:
    acessar_funcionario()
