from repositorio import banco
from use_cases.buscar import buscarProduto
from use_cases.adicionar import adicionarProduto

def editarProduto(codigo, nome, categoria, preco):
    produto = buscarProduto(codigo)
    if produto:
        produto['nome'] = nome
        produto['categoria'] = categoria
        produto['preco'] = preco
        print('Dados alterados com sucesso!')
    else:
        print('Produto não encontrado!')


if __name__ == '__main__':
    adicionarProduto('mouse','perifericos', 199)
    editarProduto(1, 'teclado', 'perifericos', 199)
    print(banco)