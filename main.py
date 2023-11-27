import csv

#Modulo 4

estoque_arquivo = 'estoque.csv'

def carregar_estoque():
    try:
        with open(estoque_arquivo, 'r', newline='') as file:
            reader = csv.DictReader(file)
            estoque = {row['Ingrediente']: int(row['Quantidade']) for row in reader}
    except FileNotFoundError:
        estoque = {}
    return estoque

def salvar_estoque(estoque):
    with open(estoque_arquivo, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Ingrediente', 'Quantidade'])
        writer.writeheader()
        for ingrediente, quantidade in estoque.items():
            writer.writerow({'Ingrediente': ingrediente, 'Quantidade': quantidade})

def adicionar_ingredientes():
  estoque = carregar_estoque()

  while True:
      ingrediente = input("Digite o nome do ingrediente ('sair' para encerrar): ")
      if ingrediente.lower() == 'sair':
          break

      quantidade = int(input(f"Digite a quantidade de {ingrediente}: "))

      if ingrediente in estoque:
          estoque[ingrediente] += quantidade
      else:
          estoque[ingrediente] = quantidade

  salvar_estoque(estoque)
  print("Ingredientes adicionados ao estoque com sucesso!")

def monitoramento_producao():
  estoque = carregar_estoque()

  print("Estoque atual:")
  for ingrediente, quantidade in estoque.items():
      print(f"{ingrediente}: {quantidade}")

  estoque_baixo = [ingred for ingred, quantidade in estoque.items() if quantidade < 10]  
  if estoque_baixo:
      print("\nAtenção! Estoque baixo para os seguintes ingredientes:")
      for ingrediente in estoque_baixo:
          print(ingrediente)
  else:
      print("\nEstoque está adequado. Nenhum ingrediente com estoque baixo.")

  salvar_estoque(estoque)

def receita_filial1():
  f = open("Receitas.txt", "a")
  f.write("Maionese de batatas com legumes! \n INGREDIENTES: \n 2 batatas médias (sem casca) picadas \n 3 xícaras de chá de maionese\n 1 colher de chá de mostarda\n 1 lata de seleta de legumes\n ½ xícara de chá de milho\n Sal e pimenta a gosto\n Salsinha a gosto")
  f.close()

  f = open("Receitas.txt", "r")
  print(f.read())
  f.close()

def receita_filial2():
  f = open("Receitas.txt", "a")
  f.write("Maionese de batatas com legumes! \n INGREDIENTES: \n 2 batatas médias (sem casca) picadas \n 3 xícaras de chá de maionese\n 1 colher de chá de mostarda\n 1 lata de seleta de legumes\n ½ xícara de chá de milho\n Sal e pimenta a gosto\n Salsinha a gosto")
  f.close()

  f = open("Receitas.txt", "r")
  print(f.read())
  f.close()

def receita_filial3():
  f = open("Receitas.txt", "a")
  f.write("Maionese de batatas com legumes! \n INGREDIENTES: \n 2 batatas médias (sem casca) picadas \n 3 xícaras de chá de maionese\n 1 colher de chá de mostarda\n 1 lata de seleta de legumes\n ½ xícara de chá de milho\n Sal e pimenta a gosto\n Salsinha a gosto")
  f.close()

  f = open("Receitas.txt", "r")
  print(f.read())
  f.close()

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

def cadastrar_cardapio(cardapio):
  estoque = carregar_estoque()

  nome = input('Digite o nome do prato: ')
  descricao = input('Digite descrição do produto: ')
  ingrediente = input('Digite os ingredientes necessarios: ')
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
      if ingred in estoque:
          quantidade_utilizada = int(input(f"Digite a quantidade de {ingred} utilizada: "))
          estoque[ingred] -= quantidade_utilizada
      else:
          print(f"{ingred} não está no estoque.")

  cardapio.append(cardapio_dic)
  salvar_cardapio('Lista_cardapio.csv', cardapio)
  salvar_estoque(estoque)

cardapio = []

while True:
  print('-=' * 20)
  print('Menu principal: \n')
  print(' 1 - Monitoramento de produção\n 2 - Receitas\n 3 - Cardapio das Filiais\n 4 - Adcionar ingredientes\n 5 - Sair\n')

  escolha = int(input('Escolha uma opção: '))
  print('\n')

  if escolha == 1:
    monitoramento_producao()
  elif escolha == 2:
    menu_receita()
  elif escolha == 3:
    cadastrar_cardapio(cardapio)
  elif escolha == 4:
    adicionar_ingredientes()
  elif escolha == 5:
    print('Saindo...')
    exit()
  else:
    print('Opção inválida')