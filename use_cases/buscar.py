from repositorio import banco
from adicionar import *
def buscarProduto(codigo: int) -> dict or None:
    for produto in banco:
        if codigo == produto['codigo']:
            return produto
    return None

if __name__ == '__main__':
    adicionarProduto('mouse','perifericos', 199)
    print(buscarProduto(1))
    print(buscarProduto(2))

