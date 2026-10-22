import CRUD

def exibir_menu():
    print("\n" + "="*30)
    print("  GESTÃO DE ESTOQUE TECH")
    print("="*30)
    print("1. Cadastrar produto")
    print("2. Listar produto")
    print("3. Deletar produto")
    print("4. Atualizar produto")
    print("5. Sair")
    print("="*30)

def main():
    while True:
      exibir_menu()
      opçao = input(" Ecolha uma opção (1-5):")

      if opçao == "1":
         print("\n---Novo produto---")
         nome = input("Nome do produto: ")
         preço = float(input("Preço (ex: 89.90): "))
         quantidade = int(input("Quantidade em estoque: "))

         produto_criado = CRUD.criar_produto(nome,preço,quantidade)
         print(f"\n*Produto {produto_criado['nome']} cadastrado com secesso!")

      
      elif opçao == "2":
         produtos = CRUD.listar_produtos()
         if produtos:
            print("\n---Lista de produtos---")
            for produto in produtos:
                print(f"ID: {produto['id']}")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: R$ {produto['preço']:.2f}")
                print(f"Quantidade: {produto['quantidade']}")
                print("-" * 30)
            
         else:
             print("\nNenhum produto encontardo no estoque.")


      elif opçao == "3":
         id_produto = int(input("\nDigite o ID do produto que deseja deletar:"))
         sucesso = CRUD.deletar_produto(id_produto)
           
         if sucesso:
            print(f"Produto com ID {id_produto} deletado com secesso!")
         else:
            print(f"Produto com ID {id_produto} não encontrado!")


      elif opçao == "4":
         id_produto = int(input("\nDigite o ID do produto que deseja atualizar:"))
         print("\n---Atualizar produto---")
         nome = input("Novo nome do produto: ")
         preço = float(input("Novo preço (ex: 89.90): "))
         quantidade = int(input("Nova quantidade em estoque: "))

         sucesso = CRUD.atualizar_produto(id_produto, nome, preço, quantidade)
         if sucesso:
            print(f"Produto com ID {id_produto} atualizado com secesso!")
         else:
            print(f"Produto com ID {id_produto} não encontrado!")


      elif opçao == "5":
       print("\n Saindo do sistema...Até logo!")  
       break

if __name__ == "__main__":
    main()   


   