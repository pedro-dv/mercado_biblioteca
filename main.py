from use_cases.adicionar import adicionarProduto
from use_cases.buscar import buscarProduto
from use_cases.editar import editarProduto
from use_cases.listar import listarProduto
from use_cases.deletar import deletarProduto

def menu():
    while True:
        print('--- Bem-vindo ao menu ---')
        print('''1- Adicionar produto
        2- Editar produto
        3- Buscar produto
        4- Deletar produto
        5- Listar todos os produtos
        outro - sair''')
        op = int(input('Digite a opção:'))


        if op == 1:
            nome = input('Digite o nome do produto:')
            categoria = input('digite a categoria do produto:')
            preco = float(input('Digite o preço do produto:'))
            adicionarProduto(nome, categoria, preco)

        elif op == 2:
            nome = input('Digite o nome do produto:')
            categoria = input('Digite a categoria do produto:')
            preco = float(input('Digite o preço do produto:'))
            editarProduto(nome, categoria, preco)

        elif op == 3:
            codigo = int(input('Digite o codigo do produto:'))
            buscarProduto(codigo)

        elif op == 4:
            codigo = int(input('Digite o codigo do produto:'))
            deletarProduto(codigo)

        elif op == 5:
            listarProduto()

        else:
            break


