# LANCHONETE
# --------------------------------------------------------------------------------------- #

# MENU LISTA
menu_produtos = [
    {"id": 1, "nome": "Hambúrguer", "preco": 18.00},
    {"id": 2, "nome": "Batata Frita", "preco": 12.00},
    {"id": 3, "nome": "Refrigerante", "preco": 5.00},
    {"id": 4, "nome": "Milkshake", "preco": 16.00}
]

# --------------------------------------------------------------------------------------- #

# VALORES DENCONTO E TAXA DE ENTREGA
desconto = 0.20
taxa_de_entrega = 15.00

# --------------------------------------------------------------------------------------- #

# FUNÇÕES
def menu():
    print("\n------ MENU ------")
    for i in menu_produtos:
        print(f"{i['id']} - {i['nome']} | R$ {i['preco']:.2f}")
    print("0 - Finalizar")
    print("------------------")


def escolher_produto():
    return int(input("Selecione um produto: "))


def escolher_quantidade(nome):
    return int(input(f"Informe a quantidade de {nome}s: "))


def buscar_produto(id):
    # Percorre todos os produtos da lista menu_produtos
    for i in menu_produtos:
        
        # Verifica se o id do produto atual é igual ao id informado
        if i["id"] == id:
            
            # Se encontrar, retorna o produto
            return i
    
    # Se não encontrar nenhum produto com esse id, retorna None
    return None


def mostrar_resumo(pedido, total):
    print("\n----- RESUMO -----")
    for i in pedido:
        print(f"{i[0]} x{i[1]} = R$ {i[2]:.2f}")
    print(f"Total: R$ {total:.2f}")


def finalizar(total):
    while True:
        print("\nEntrega?\n1-Sim\n2-Não")
        opcao = input("Escolha: ")

        if opcao == "1":
            total += taxa_de_entrega # Caso selecione 1 soma-se o valor da taxa de entrega ao total da compra
            break
        elif opcao == "2":
            total -= total * desconto # Caso selecione 2 aplica-se um desconto de 20% na compra
            break
        else:
            print("Opção inválida")

    return total

# --------------------------------------------------------------------------------------- #

# LOOP DE REPETIÇÃO DO PROGRAMA
def programa():
    total = 0
    pedido = []

    while True:
        menu()
        opcao = escolher_produto()

        if opcao == 0:
            if len(pedido) == 0: # len() conta a quantidade de elementos dentro de pedido
                print("\nNenhum produto foi selecionado.")
                print("Programa encerrado.")
                return  # encerra a função em que está
            break # interrompe o loop
        
        # Busca o produto escolhido pelo usuário com base na opção digitada
        produto = buscar_produto(opcao)

        # Verifica se o produto existe 
        if produto:
            # Pede ao usuário a quantidade desejada daquele produto
            qtd = escolher_quantidade(produto["nome"])

             # Verifica se a quantidade é válida
            if qtd > 0:
                # Calcula o subtotal (preço * quantidade)
                subtotal = produto["preco"] * qtd
                # Soma o subtotal ao total geral do pedido
                total += subtotal
                # Adiciona o item ao pedido (nome, quantidade e subtotal)
                pedido.append((produto["nome"], qtd, subtotal))
                # Confirma que o produto foi adicionado
                print("Produto adicionado com sucesso!")
            else:
                print("Quantidade inválida")
        else:
            print("Produto inválido")

    # Após sair do loop de pedidos:
    # Mostra um resumo com todos os itens pedidos e o total
    mostrar_resumo(pedido, total)

    # Finaliza o pedido (aplica desconto ou taxa de entrega, por exemplo)
    total = finalizar(total)

    print(f"\nTOTAL DA COMPRA: R$ {total:.2f}")
    print("Compra finalizada com sucesso!")

# --------------------------------------------------------------------------------------- #

# EXECUTA O PROGRAMA
programa()