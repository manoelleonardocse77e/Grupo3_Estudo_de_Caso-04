import csv
import smtplib
from email.mime.text import MIMEText

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
    print("1. Cadastrar Fornecedor")
    print("2. Definir Ponto de Reposição")
    print("3. Simular Estoque")
    print("4. Verificar Necessidade de Reabastecimento")
    print("5. Gerar Pedidos e Arquivos")
    print("6. Sair")

if __name__ == "__main__":
    pedido_fornecedor = PedidoFornecedor()
    estoque_atual = {}  # Mova a declaração do estoque para fora do loop

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_fornecedor = input("Nome do fornecedor: ")
            email_fornecedor = input("Email do fornecedor: ")
            pedido_fornecedor.cadastrar_fornecedor(nome_fornecedor, email_fornecedor)

        elif escolha == "2":
            produto = input("Nome do produto: ")
            while True:
                try:
                    ponto_rep = int(input("Ponto de Reposição: "))
                    break  # Se a conversão para int for bem-sucedida, sai do loop
                except ValueError:
                    print("Por favor, insira um valor inteiro válido para o ponto de reposição.")

            pedido_fornecedor.definir_ponto_reposicao(produto, ponto_rep)

        elif escolha == "3":
            estoque_atual = {}
            while True:
                produto = input("Nome do produto (ou 'fim' para encerrar): ")
                if produto.lower() == 'fim':
                    break
                quantidade = int(input("Quantidade em estoque: "))
                estoque_atual[produto] = quantidade

        elif escolha == "4":
            pedidos_a_realizar = pedido_fornecedor.verificar_necessidade_reabastecimento(estoque_atual)
            print("Necessidade de reabastecimento verificada.")

        elif escolha == "5":
            pedido_fornecedor.gerar_pedido(pedidos_a_realizar)
            print("Pedidos e arquivos gerados com sucesso!")

        elif escolha == "6":
            break

        else:
            print("Opção inválida. Tente novamente.")
