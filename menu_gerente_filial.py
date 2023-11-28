import csv
import pandas as pd
import matplotlib.pyplot as plt
import smtplib
from email.mime.text import MIMEText

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

class PedidoFornecedor:
    def __init__(self):
        self.fornecedores = []
        self.ponto_reposicao = {}
        self.email_gerente = "gerente@empresa.com"
        self.smtp_server = "smtp.empresa.com"
        self.smtp_port = 587
        self.smtp_username = "seu_usuario"
        self.smtp_password = "sua_senha"

    def cadastrar_fornecedor(self, nome, email):
        self.fornecedores.append({"nome": nome, "email": email})

    def definir_ponto_reposicao(self, produto, ponto):
        self.ponto_reposicao[produto] = ponto

    def verificar_necessidade_reabastecimento(self, estoque):
        pedidos = []
        for produto, nivel_atual in estoque.items():
            ponto_rep = self.ponto_reposicao.get(produto, 0)
            if nivel_atual <= ponto_rep:
                pedido = {"produto": produto, "quantidade": ponto_rep - nivel_atual}
                pedidos.append(pedido)
        return pedidos

    def gerar_pedido(self, pedidos):
        if not pedidos:
            return

        with open("pedidos.txt", "a") as file_txt:
            for pedido in pedidos:
                file_txt.write(f"Produto: {pedido['produto']}, Quantidade: {pedido['quantidade']}\n")

        with open("pedidos.csv", "a", newline="") as file_csv:
            csv_writer = csv.writer(file_csv)
            for pedido in pedidos:
                csv_writer.writerow([pedido['produto'], pedido['quantidade']])

        self.enviar_email_alerta()

    def enviar_email_alerta(self):
        subject = "Alerta de Reabastecimento"
        body = "Há produtos que atingiram o ponto de reposição. Verifique os pedidos em anexo."
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = "sistema@empresa.com"
        msg["To"] = self.email_gerente

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail("sistema@empresa.com", [self.email_gerente], msg.as_string())

def exibir_menu():
    print("\nMenu:")
    print("1. Cadastrar Funcionário")
    print("2. Gerenciar Funcionário")
    print("3. Acessar Informações do Funcionário")
    print("4. Gerar Gráfico de Vendas")
    print("5. Relatório de Movimentação de Estoque")
    print("6. Relatório de Eficiência Operacional")
    print("7. Sair")

def verificar_senha():
    senha_correta = "senha123"  # Substitua pela sua senha real
    tentativas = 3

    while tentativas > 0:
        senha_inserida = input("Digite a senha para acessar o sistema: ")
        if senha_inserida == senha_correta:
            return True
        else:
            tentativas -= 1
            print(f"Senha incorreta. Tentativas restantes: {tentativas}")

    print("Número máximo de tentativas atingido. Encerrando o programa.")
    return False

if __name__ == "__main__":
    if verificar_senha():
        controle_estoque = ControleEstoque()
        pedido_fornecedor = PedidoFornecedor()

        while True:
            exibir_menu()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                controle_estoque.cadastrar_funcionario()
            elif escolha == "2":
                controle_estoque.gerenciar_funcionario()
            elif escolha == "3":
                controle_estoque.acessar_funcionario()
            elif escolha == "4":
                arquivo_grafico = input("Insira o arquivo para gerar o gráfico: ")
                gerar_grafico(arquivo_grafico)
                print("Gráfico gerado")
            elif escolha == "5":
                arquivos_relatorios = ['arquivo1.csv', 'arquivo2.csv', 'arquivo3.csv']
                relatorio_movimentacao_estoque(arquivos_relatorios)
            elif escolha == "6":
                arquivos_relatorios = ['arquivo1.csv', 'arquivo2.csv', 'arquivo3.csv']
                relatorio_eficiencia_operacional(arquivos_relatorios)
            elif escolha == "7":
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Senha incorreta. Encerrando o programa.")
