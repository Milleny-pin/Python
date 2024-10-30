# Inicializa o dicionário de estoque
estoque = {}

def exibir_menu():
    print('\n|^^^^^\nExibir Menu^^^^^|')
    print('|1   Adicionar produto  |')
    print('|2   Atualizar produto  |')
    print('|3   Visualizar estoque |')
    print('|4      Fazer sacola    |')
    print('|5         Sair         |')

def adicionar_produto():
    while True:
        produto = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))
        quantidade = int(input(f'Digite a quantidade de {produto} que deseja adicionar: '))
        if produto in estoque:
            estoque[produto]['quantidade'] += quantidade
        else:
            estoque[produto] = {'preco': preco, 'quantidade': quantidade}
        print(f'{quantidade} {produto}(s) adicionadas com sucesso!')
        adicionar = input('Deseja adicionar mais algum produto? [s/n]: ')
        if adicionar.lower() != 's':
            break

def atualizar_produto():
    produto = input('Digite o nome do produto que deseja atualizar: ')
    if produto in estoque:
        preco = float(input('Digite o novo preço do produto: '))
        quantidade = int(input(f'Digite a nova quantidade de {produto}: '))
        estoque[produto] = {'preco': preco, 'quantidade': quantidade}
        print(f'Produto {produto} atualizado com sucesso!')
    else:
        print(f'Produto {produto} não encontrado no estoque.')

def visualizar_estoque():
    print('\nEstoque atual:')
    for produto, detalhes in estoque.items():
        print(f"Produto: {produto}, Preço: {detalhes['preco']}, Quantidade: {detalhes['quantidade']}")
    if not estoque:
        print('O estoque está vazio.')

def fazer_sacola():
    sacola = {}
    while True:
        produto = input('Digite o nome do produto que deseja adicionar à sacola: ')
        if produto in estoque:
            quantidade_disponivel = estoque[produto]['quantidade']
            quantidade = int(input(f'Digite a quantidade de {produto} que deseja adicionar (Disponível: {quantidade_disponivel}): '))
            if quantidade <= quantidade_disponivel:
                if produto in sacola:
                    sacola[produto]['quantidade'] += quantidade
                else:
                    sacola[produto] = {'preco': estoque[produto]['preco'], 'quantidade': quantidade}
                print(f'{quantidade} {produto}(s) adicionadas à sacola.')
            else:
                print(f'Quantidade solicitada não disponível. Disponível: {quantidade_disponivel}')
        else:
            print(f'Produto {produto} não encontrado no estoque.')
        
        adicionar_mais = input('Deseja adicionar mais algum produto à sacola? [s/n]: ')
        if adicionar_mais.lower() != 's':
            break
    
    # Calcula o custo total
    custo_total = sum(detalhes['preco'] * detalhes['quantidade'] for detalhes in sacola.values())
    print('\nSacola:')
    for produto, detalhes in sacola.items():
        print(f"Produto: {produto}, Preço: {detalhes['preco']}, Quantidade: {detalhes['quantidade']}")
    print(f'Custo total da sacola: R$ {custo_total:.2f}')

while True:
    exibir_menu()
    opcao = input('Selecione uma opção: ')

    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        atualizar_produto()
    elif opcao == '3':
        visualizar_estoque()
    elif opcao == '4':
        fazer_sacola()
    elif opcao == '5':
        print('Saindo...')
        break
    else:
        print('Opção inválida!')
    
    voltar_menu = input('Deseja voltar ao menu principal? [s/n]: ')
    if voltar_menu.lower() != 's':
        print('Saindo...')
        break

