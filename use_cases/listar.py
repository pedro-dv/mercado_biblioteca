from repositorio import banco
from use_cases.adicionar import adicionarProduto


def listarProduto():
    print('-- LISTA DE PRODUTOS --')
    for produto in banco:
        print(f"codigo: {produto['codigo']}")
        print(f"nome: {produto['nome']}")
        print(f"categoria: {produto['categoria']}")
        print(f"preço: {produto['preco']}")

if __name__ == '__main__':

    adicionarProduto('mouse', 'perifericos', 199)
    adicionarProduto('mousepad', 'acessorios', 100)

    listarProduto()