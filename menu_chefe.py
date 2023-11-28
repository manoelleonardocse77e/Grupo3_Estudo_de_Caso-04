import csv

estoque_arquivo = 'estoque.csv'

class md1:

    def __init__(self):
        self.estoque = self.carregar_estoque()

    def carregar_estoque(self):
        try:
            with open(estoque_arquivo, 'r', newline='') as file:
                reader = csv.DictReader(file)
                estoque = {row['Ingrediente']: int(row['Quantidade']) for row in reader}
        except FileNotFoundError:
            estoque = {}
        return estoque

    def salvar_estoque(self):
        with open(estoque_arquivo, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Ingrediente', 'Quantidade'])
            writer.writeheader()
            for ingrediente, quantidade in self.estoque.items():
                writer.writerow({'Ingrediente': ingrediente, 'Quantidade': quantidade})

    def adicionar_ingredientes(self):
        while True:
            ingrediente = input("Digite o nome do ingrediente ('sair' para encerrar): ")
            if ingrediente.lower() == 'sair':
                break

            quantidade = int(input(f"Digite a quantidade de {ingrediente}: "))

            if ingrediente in self.estoque:
                self.estoque[ingrediente] += quantidade
            else:
                self.estoque[ingrediente] = quantidade

        self.salvar_estoque()
        print("Ingredientes adicionados ao estoque com sucesso!")

    def monitoramento_producao(self):
        print("Estoque atual:")
        for ingrediente, quantidade in self.estoque.items():
            print(f"{ingrediente}: {quantidade}")

        estoque_baixo = [ingred for ingred, quantidade in self.estoque.items() if quantidade < 10]  
        if estoque_baixo:
            print("\nAtenção! Estoque baixo para os seguintes ingredientes:")
            for ingrediente in estoque_baixo:
                print(ingrediente)
        else:
            print("\nEstoque está adequado. Nenhum ingrediente com estoque baixo.")

        self.salvar_estoque()

    def cadastrar_cardapio(self, cardapio):
        nome = input('Digite o nome do prato: ')
        descricao = input('Digite descrição do produto: ')
        ingrediente = input('Digite os ingredientes necessários: ')
        preco = float(input('Digite o preço unitário do produto: '))

        cardapio_dic = {
            'Nome': nome,
            'Descrição': descricao,
            'Preço': preco,
            'Ingredientes': ingrediente
        }

        ingredientes_utilizados = ingrediente.split(',')
        for ingred in ingredientes_utilizados:
            ingred = ingred.strip()
            if ingred in self.estoque:
                quantidade_utilizada = int(input(f"Digite a quantidade de {ingred} utilizada: "))
                self.estoque[ingred] -= quantidade_utilizada
            else:
                print(f"{ingred} não está no estoque.")

        cardapio.append(cardapio_dic)
        self.salvar_cardapio('Lista_cardapio.csv', cardapio)
        self.salvar_estoque()

def menu_receita():
    print('Qual filial deseja ver as receitas:\n 1 - filial 1\n 2 - filial 2\n 3 - filial 3\n')

    escolha = input('Digite a opção desejada: ')
    print('\n')

    if escolha == '1':
        receita_filial1()
    elif escolha == '2':
        receita_filial2()
    elif escolha == '3':
        receita_filial3()
    else:
        print('Filial não cadastrada')
        menu_receita()

def salvar_cardapio(filename, cardapio):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(cardapio[0].keys())
        for item in cardapio:
            writer.writerow(item.values())

cardapio = []

controle_estoque = md1()


senha_correta = "senha123"

tentativas = 3

while True:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta! Tentativas restantes: {tentativas}")
        
        if tentativas == 0:
            print("Número de tentativas excedido. Saindo do programa.")
            exit()

while True:
    print('-=' * 20)
    print('Menu principal: \n')
    print(' 1 - Monitoramento de produção\n 2 - Receitas\n 3 - Cardápio das Filiais\n 4 - Adicionar ingredientes\n 5 - Sair\n')

    escolha = int(input('Escolha uma opção: '))
    print('\n')

    if escolha == 1:
        controle_estoque.monitoramento_producao()
    elif escolha == 2:
        menu_receita()
    elif escolha == 3:
        controle_estoque.cadastrar_cardapio(cardapio)
    elif escolha == 4:
        controle_estoque.adicionar_ingredientes()
    elif escolha == 5:
        print('Saindo...')
        exit()
    else:
        print('Opção inválida')
