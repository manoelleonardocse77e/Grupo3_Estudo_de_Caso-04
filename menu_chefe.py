import getpass

def carregar_senhas(nome_arquivo):
    senhas = {}
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            modulo, senha = linha.strip().split(':')
            senhas[modulo] = senha
    return senhas

def verificar_senha(usuario, senha, senhas_armazenadas):
    if usuario in senhas_armazenadas and senha == senhas_armazenadas[usuario]:
        return True
    else:
        return False

def modulo1():
    print("Bem-vindo ao Módulo 1!")
    # Lógica do Módulo 1

def modulo2():
    print("Bem-vindo ao Módulo 2!")
    # Lógica do Módulo 2

def modulo3():
    print("Bem-vindo ao Módulo 3!")
    # Lógica do Módulo 3

def main():
    nome_arquivo_senhas = 'senhas.txt'
    senhas_armazenadas = carregar_senhas(nome_arquivo_senhas)

    while True:
        print("\n=== Menu ===")
        print("1. Controle de Estoque")
        print("2. Monitoramento de Producao")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '0':
            print("Saindo do programa.")
            break
        elif escolha in ['1', '2', '3']:
            usuario = input("Digite seu nome de usuário: ")
            senha = getpass.getpass("Digite sua senha: ")

            if verificar_senha(usuario, senha, senhas_armazenadas):
                if escolha == '1':
                    modulo1()
                elif escolha == '2':
                    modulo2()
            else:
                print("Usuário ou senha incorretos. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
