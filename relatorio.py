def gerar_relatorio(arquivo_origem, arquivo_destino):
    try:
        with open(arquivo_origem, 'r') as arquivo_entrada:
            dados = arquivo_entrada.read()

        with open(arquivo_destino, 'w') as arquivo_saida:
            arquivo_saida.write(dados)

        print(f'Dados copiados de {arquivo_origem} para {arquivo_destino} com sucesso.')
    except FileNotFoundError:
        print(f'O arquivo {arquivo_origem} não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

