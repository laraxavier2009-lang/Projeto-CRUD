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