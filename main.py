import CRUD

def exibir_menu():
    print("\n" + "="*30)
    print("  GESTÃO DE ESTOQUE TECH")
    print("\n"*30)
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

      elif opçao == 5:
       print("\n Saindo do sistema...Até logo!")  
       break

if __name__ == "__main__":
    main()   


   