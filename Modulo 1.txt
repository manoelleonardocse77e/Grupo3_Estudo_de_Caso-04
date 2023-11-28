import csv

class ControleEstoque:
    def __init__(self):
        self.estoque = self.carregar_estoque()

    def carregar_estoque(self):
        try:
            with open('estoque.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                estoque = {row['produto']: {'quantidade': int(row['quantidade']), 'limite': int(row['limite'])} for
                           row in reader}
                return estoque
        except FileNotFoundError:
            print("Arquivo 'estoque.csv' não encontrado. Criando um novo estoque vazio.")
            return {}

    def salvar_estoque(self):
        with open('estoque.csv', 'w', newline='') as csvfile:
            fieldnames = ['produto', 'quantidade', 'limite']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for produto, info in self.estoque.items():
                writer.writerow({'produto': produto, 'quantidade': info['quantidade'], 'limite': info['limite']})

    def monitorar_estoque(self):
        for produto, info in self.estoque.items():
            print(f"{produto}: Quantidade disponível - {info['quantidade']}, Limite - {info['limite']}")

    def alerta_estoque(self):
        for produto, info in self.estoque.items():
            if info['quantidade'] < info['limite']:
                print(f"ALERTA: {produto} está abaixo do limite. Quantidade disponível: {info['quantidade']}")

    def integrar_entregas(self, entregas):
        for entrega in entregas:
            produto, quantidade_entregue, limite = entrega
            if produto in self.estoque:
                self.estoque[produto]['quantidade'] += quantidade_entregue
                self.estoque[produto]['limite'] = limite
            else:
                self.estoque[produto] = {'quantidade': quantidade_entregue, 'limite': limite}

        self.salvar_estoque()

def modulo1():
    controle_estoque = ControleEstoque()
    print("=-=" * 24)
    print("                      Monitoramento de Estoque")
    print("=-=" * 24)

    # exemplo de recebimento
    #entregas_programadas = [('Farinha', 100, 100),
                            #('Açúcar', 50, 100),
                            #('Sal', 30, 100)]

    # Atualização estoque com os recebimentos
    #controle_estoque.integrar_entregas(entregas_programadas)

    # Exemplo para retirar determinada quantidade do produto
    #entregas_programadas = [('Farinha', -50, 1000)]

    #controle_estoque.integrar_entregas(entregas_programadas)


    controle_estoque.monitorar_estoque()

    print("=-=" * 24)

    controle_estoque.alerta_estoque()
