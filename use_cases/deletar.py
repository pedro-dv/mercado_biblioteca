from repositorio import banco
from use_cases.adicionar import adicionarProduto
from use_cases.buscar import buscarProduto

def deletarProduto(codigo: int):
    produto = buscarProduto(codigo)
    if produto:
        banco.remove(produto)
        print('produto removido com sucesso!')
    else:
        print('produto nao encontrado!')

if __name__ == '__main__':
    adicionarProduto('mouse','periferico',199)
    print(banco)
    deletarProduto(1)
    print(banco)
    deletarProduto(1)