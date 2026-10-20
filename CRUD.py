estoque = []

proximo_id = 1

def criar_produto(nome: str, preço: float,  quantidade: int) -> dict:
    global proximo_id

    produto = {
    "id": proximo_id,
    "nome": nome,
    "preço": preço,
    "quantidade": quantidade 

    }
    estoque.append(produto) 
    proximo_id += 1   

    return produto

def listar_produtos() -> list:
    """Retorna a lista completa de produtos cadastrados."""
    return estoque

def atualizar_produto(id_produto: int, novo_nome: str, novo_preço:float, nova_quantidade: int) -> bool:
    """Busca o produto pelo ID e atualiza seus dados."""
    
    for produto in estoque:
     if produto ["id"] == id_produto: 
         produto ["nome"] = novo_nome
         produto ["preço"] = novo_preço
         produto ["quantidade"] = nova_quantidade
         return True
     return False   
 
def deletar_produto(id_produto: int) -> bool:
    """Busca o produto pelo ID e o remove da lista."""
    for produto in estoque:
        if produto["id"] == id_produto:
            estoque.remove(produto)
            return True
    return False    