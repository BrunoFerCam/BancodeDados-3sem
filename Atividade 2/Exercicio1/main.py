from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://aluno:F4t3c2023@branco.3nl94.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
global db
db = client.mercadolivre

# CRUD para Usuários
def create_usuario():
    global db
    mycol = db.usuario
    print("\nInserindo um novo usuário")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    key = 'S'
    end = []
    while key == 'S':
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {
            "rua": rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco)
        key = input("Deseja cadastrar um novo endereço (S/N)? ").upper()
    mydoc = {"nome": nome, "sobrenome": sobrenome, "cpf": cpf, "end": end}
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)

def read_usuario(nome):
    global db
    mycol = db.usuario
    print("Usuários existentes: ")
    if not nome:
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"], x["cpf"])
    else:
        myquery = {"nome": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_usuario(nome):
    global db
    mycol = db.usuario
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    print("Dados do usuário: ", mydoc)
    nome = input("Mudar Nome: ")
    if nome:
        mydoc["nome"] = nome

    sobrenome = input("Mudar Sobrenome: ")
    if sobrenome:
        mydoc["sobrenome"] = sobrenome

    cpf = input("Mudar CPF: ")
    if cpf:
        mydoc["cpf"] = cpf

    newvalues = {"$set": mydoc}
    mycol.update_one(myquery, newvalues)

def delete_usuario(nome, sobrenome):
    global db
    mycol = db.usuario
    myquery = {"nome": nome, "sobrenome": sobrenome}
    mydoc = mycol.delete_one(myquery)
    print("Deletado o usuário ", mydoc)

# CRUD para Vendedores
def create_vendedor():
    global db
    mycol = db.vendedor
    print("\nInserindo um novo vendedor")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    key = 'S'
    end = []
    while key == 'S':
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {
            "rua": rua,
            "num": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco)
        key = input("Deseja cadastrar um novo endereço (S/N)? ").upper()
    mydoc = {"nome": nome, "sobrenome": sobrenome, "cpf": cpf, "end": end}
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)

def read_vendedor(nome):
    global db
    mycol = db.vendedor
    print("Vendedores existentes: ")
    if not nome:
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"], x["cpf"])
    else:
        myquery = {"nome": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_vendedor(nome):
    global db
    mycol = db.vendedor
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    print("Dados do vendedor: ", mydoc)
    nome = input("Mudar Nome: ")
    if nome:
        mydoc["nome"] = nome

    sobrenome = input("Mudar Sobrenome: ")
    if sobrenome:
        mydoc["sobrenome"] = sobrenome

    cpf = input("Mudar CPF: ")
    if cpf:
        mydoc["cpf"] = cpf

    newvalues = {"$set": mydoc}
    mycol.update_one(myquery, newvalues)

def delete_vendedor(nome, sobrenome):
    global db
    mycol = db.vendedor
    myquery = {"nome": nome, "sobrenome": sobrenome}
    mydoc = mycol.delete_one(myquery)
    print("Deletado o vendedor ", mydoc)

# CRUD para Produtos
def create_produto():
    global db
    mycol = db.produto
    print("\nInserindo um novo produto")
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    preco = input("Preço: ")
    quantidade = input("Quantidade: ")
    mydoc = {"nome": nome, "descricao": descricao, "preco": preco, "quantidade": quantidade}
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)

def read_produto(nome):
    global db
    mycol = db.produto
    print("Produtos existentes: ")
    if not nome:
        mydoc = mycol.find().sort("nome")
        for x in mydoc:
            print(x["nome"], x["preco"])
    else:
        myquery = {"nome": nome}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_produto(nome):
    global db
    mycol = db.produto
    myquery = {"nome": nome}
    mydoc = mycol.find_one(myquery)
    print("Dados do produto: ", mydoc)
    nome = input("Mudar Nome: ")
    if nome:
        mydoc["nome"] = nome

    descricao = input("Mudar Descrição: ")
    if descricao:
        mydoc["descricao"] = descricao

    preco = input("Mudar Preço: ")
    if preco:
        mydoc["preco"] = preco

    quantidade = input("Mudar Quantidade: ")
    if quantidade:
        mydoc["quantidade"] = quantidade

    newvalues = {"$set": mydoc}
    mycol.update_one(myquery, newvalues)

def delete_produto(nome):
    global db
    mycol = db.produto
    myquery = {"nome": nome}
    mydoc = mycol.delete_one(myquery)
    print("Deletado o produto ", mydoc)

# CRUD para Favoritos
def create_favorito():
    global db
    mycol = db.favorito
    print("\nInserindo um novo favorito")
    nome_usuario = input("Nome do Usuário: ")
    nome_produto = input("Nome do Produto: ")
    favorito = {"usuario": nome_usuario, "produto": nome_produto}
    x = mycol.insert_one(favorito)
    print("Favorito inserido com ID ", x.inserted_id)

def read_favorito(nome_usuario):
    global db
    mycol = db.favorito
    print("Favoritos existentes: ")
    if not nome_usuario:
        mydoc = mycol.find().sort("usuario")
        for x in mydoc:
            print(x["usuario"], x["produto"])
    else:
        myquery = {"usuario": nome_usuario}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)

def update_favorito(nome_usuario, nome_produto):
    global db
    mycol = db.favorito
    myquery = {"usuario": nome_usuario, "produto": nome_produto}
    mydoc = mycol.find_one(myquery)
    print("Dados do favorito: ", mydoc)
    novo_produto = input("Mudar Produto: ")
    if novo_produto:
        mydoc["produto"] = novo_produto

    newvalues = {"$set": mydoc}
    mycol.update_one(myquery, newvalues)

def delete_favorito(nome_usuario, nome_produto):
    global db
    mycol = db.favorito
    myquery = {"usuario": nome_usuario, "produto": nome_produto}
    mydoc = mycol.delete_one(myquery)
    print("Deletado o favorito ", mydoc)

# Funcionalidades de Compra
def create_compra():
    global db
    mycol = db.compra
    print("\nInserindo uma nova compra")
    nome_usuario = input("Nome do Usuário: ")
    nome_produto = input("Nome do Produto: ")
    quantidade = int(input("Quantidade: "))
    compra = {"usuario": nome_usuario, "produto": nome_produto, "quantidade": quantidade}
    x = mycol.insert_one(compra)
    print("Compra inserida com ID ", x.inserted_id)

def read_compras_por_usuario(nome_usuario):
    global db
    mycol = db.compra
    print("Compras realizadas pelo usuário: ")
    myquery = {"usuario": nome_usuario}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

# Menu Principal
def main():
    key = ''
    while key != 'S':
        print("1-CRUD Usuário")
        print("2-CRUD Vendedor")
        print("3-CRUD Produto")
        print("4-CRUD Favorito")
        print("5-Compra")
        key = input("Digite a opção desejada? (S para sair) ").upper()

        if key == '1':
            print("Menu do Usuário")
            print("1-Create Usuário")
            print("2-Read Usuário")
            print("3-Update Usuário")
            print("4-Delete Usuário")
            sub = input("Digite a opção desejada? (V para voltar) ").upper()
            if sub == '1':
                create_usuario()
            elif sub == '2':
                nome = input("Read usuário, deseja algum nome específico? ")
                read_usuario(nome)
            elif sub == '3':
                nome = input("Update usuário, deseja algum nome específico? ")
                update_usuario(nome)
            elif sub == '4':
                nome = input("Nome a ser deletado: ")
                sobrenome = input("Sobrenome a ser deletado: ")
                delete_usuario(nome, sobrenome)

        elif key == '2':
            print("Menu do Vendedor")
            print("1-Create Vendedor")
            print("2-Read Vendedor")
            print("3-Update Vendedor")
            print("4-Delete Vendedor")
            sub = input("Digite a opção desejada? (V para voltar) ").upper()
            if sub == '1':
                create_vendedor()
            elif sub == '2':
                nome = input("Read vendedor, deseja algum nome específico? ")
                read_vendedor(nome)
            elif sub == '3':
                nome = input("Update vendedor, deseja algum nome específico? ")
                update_vendedor(nome)
            elif sub == '4':
                nome = input("Nome a ser deletado: ")
                sobrenome = input("Sobrenome a ser deletado: ")
                delete_vendedor(nome, sobrenome)

        elif key == '3':
            print("Menu do Produto")
            print("1-Create Produto")
            print("2-Read Produto")
            print("3-Update Produto")
            print("4-Delete Produto")
            sub = input("Digite a opção desejada? (V para voltar) ").upper()
            if sub == '1':
                create_produto()
            elif sub == '2':
                nome = input("Read produto, deseja algum nome específico? ")
                read_produto(nome)
            elif sub == '3':
                nome = input("Update produto, deseja algum nome específico? ")
                update_produto(nome)
            elif sub == '4':
                nome = input("Nome a ser deletado: ")
                delete_produto(nome)

        elif key == '4':
            print("Menu do Favorito")
            print("1-Favoritar Produto por Usuário")
            print("2-Read Favorito")
            print("3-Update Favorito")
            print("4-Delete Favorito")
            sub = input("Digite a opção desejada? (V para voltar) ").upper()
            if sub == '1':
                create_favorito()
            elif sub == '2':
                nome_usuario = input("Read favorito, deseja algum usuário específico? ")
                read_favorito(nome_usuario)
            elif sub == '3':
                nome_usuario = input("Nome do Usuário: ")
                nome_produto = input("Produto atual: ")
                update_favorito(nome_usuario, nome_produto)
            elif sub == '4':
                nome_usuario = input("Nome do Usuário: ")
                nome_produto = input("Nome do Produto a ser deletado: ")
                delete_favorito(nome_usuario, nome_produto)

        elif key == '5':
            print("Menu de Compra")
            print("1-Create Compra")
            print("2-Read Compras por Usuário")
            sub = input("Digite a opção desejada? (V para voltar) ").upper()
            if sub == '1':
                create_compra()
            elif sub == '2':
                nome_usuario = input("Nome do Usuário: ")
                read_compras_por_usuario(nome_usuario)

    print("Tchau Prof...")

if __name__ == "__main__":
    main()
