# Definindo a função principal do aplicativo
def main():
    # Inicializando a lista de compras
    lista_de_compras = []

    # Loop principal do aplicativo
    while True:
        # Exibindo as opções do menu
        print("\n=== Lista de Compras ===")
        print("1. Adicionar item")
        print("2. Ver lista de compras")
        print("3. Remover item")
        print("4. Limpar lista de compras")
        print("5. Sair")

        # Solicitando ao usuário que escolha uma opção
        escolha = input("Escolha uma opção: ")

        # Verificando a escolha do usuário
        if escolha == "1":
            item = input("Digite o item a ser adicionado: ")
            lista_de_compras.append(item)
            print(f"'{item}' foi adicionado à lista de compras.")
        elif escolha == "2":
            if lista_de_compras:
                print("\nLista de Compras:")
                for i, item in enumerate(lista_de_compras, 1):
                    print(f"{i}. {item}")
            else:
                print("A lista de compras está vazia.")
        elif escolha == "3":
            if lista_de_compras:
                print("Lista de Compras:")
                for i, item in enumerate(lista_de_compras, 1):
                    print(f"{i}. {item}")
                indice = int(input("Digite o número do item a ser removido: ")) - 1
                if 0 <= indice < len(lista_de_compras):
                    item_removido = lista_de_compras.pop(indice)
                    print(f"'{item_removido}' foi removido da lista de compras.")
                else:
                    print("Índice inválido.")
            else:
                print("A lista de compras está vazia.")
        elif escolha == "4":
            lista_de_compras.clear()
            print("A lista de compras foi limpa.")
        elif escolha == "5":
            print("Obrigado por usar a Lista de Compras. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Chamando a função principal para executar o aplicativo
if __name__ == "__main__":
    main()
