from pymongo import MongoClient
from pymongo.server_api import ServerApi

def get_db():
    uri = "mongodb+srv://brunofernandescampos:FJwbzZ2dq5I22HIH@cluster0.09dtabz.mongodb.net/"
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client.mercadolivre

db = get_db()

def create_usuario():
    mycol = db.usuario
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    end = []

    while True:
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {"rua": rua, "num": num, "bairro": bairro, "cidade": cidade, "estado": estado, "cep": cep}
        end.append(endereco)
        
        continuar = input("Deseja cadastrar um novo endereço (S/N)? ").upper()
        if continuar != 'S':
            break

    usuario = {"nome": nome, "sobrenome": sobrenome, "cpf": cpf, "end": end}
    resultado = mycol.insert_one(usuario)
    print(f"Usuário inserido com ID {resultado.inserted_id}")

def read_usuario(nome=None):
    mycol = db.usuario
    if nome:
        query = {"nome": nome}
        usuarios = mycol.find(query)
    else:
        usuarios = mycol.find().sort("nome")

    for usuario in usuarios:
        print(usuario)

def update_usuario(nome):
    mycol = db.usuario
    query = {"nome": nome}
    usuario = mycol.find_one(query)

    if usuario:
        novo_nome = input("Novo Nome (deixe vazio para manter): ") or usuario['nome']
        novo_sobrenome = input("Novo Sobrenome (deixe vazio para manter): ") or usuario['sobrenome']
        novo_cpf = input("Novo CPF (deixe vazio para manter): ") or usuario['cpf']

        novos_valores = {"$set": {"nome": novo_nome, "sobrenome": novo_sobrenome, "cpf": novo_cpf}}
        mycol.update_one(query, novos_valores)
        print("Usuário atualizado com sucesso.")
    else:
        print("Usuário não encontrado.")

def delete_usuario(nome, sobrenome):
    mycol = db.usuario
    query = {"nome": nome, "sobrenome": sobrenome}
    resultado = mycol.delete_one(query)
    print(f"{resultado.deleted_count} usuário(s) deletado(s).")

def create_vendedor():
    mycol = db.vendedor
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    end = []

    while True:
        rua = input("Rua: ")
        num = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {"rua": rua, "num": num, "bairro": bairro, "cidade": cidade, "estado": estado, "cep": cep}
        end.append(endereco)
        
        continuar = input("Deseja cadastrar um novo endereço (S/N)? ").upper()
        if continuar != 'S':
            break

    vendedor = {"nome": nome, "sobrenome": sobrenome, "cpf": cpf, "end": end}
    resultado = mycol.insert_one(vendedor)
    print(f"Vendedor inserido com ID {resultado.inserted_id}")

def read_vendedor(nome=None):
    mycol = db.vendedor
    if nome:
        query = {"nome": nome}
        vendedores = mycol.find(query)
    else:
        vendedores = mycol.find().sort("nome")

    for vendedor in vendedores:
        print(vendedor)

def update_vendedor(nome):
    mycol = db.vendedor
    query = {"nome": nome}
    vendedor = mycol.find_one(query)

    if vendedor:
        novo_nome = input("Novo Nome (deixe vazio para manter): ") or vendedor['nome']
        novo_sobrenome = input("Novo Sobrenome (deixe vazio para manter): ") or vendedor['sobrenome']
        novo_cpf = input("Novo CPF (deixe vazio para manter): ") or vendedor['cpf']

        novos_valores = {"$set": {"nome": novo_nome, "sobrenome": novo_sobrenome, "cpf": novo_cpf}}
        mycol.update_one(query, novos_valores)
        print("Vendedor atualizado com sucesso.")
    else:
        print("Vendedor não encontrado.")

def delete_vendedor(nome, sobrenome):
    mycol = db.vendedor
    query = {"nome": nome, "sobrenome": sobrenome}
    resultado = mycol.delete_one(query)
    print(f"{resultado.deleted_count} vendedor(es) deletado(s).")

def create_produto():
    mycol = db.produto
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    produto = {"nome": nome, "descricao": descricao, "preco": preco, "quantidade": quantidade}
    resultado = mycol.insert_one(produto)
    print(f"Produto inserido com ID {resultado.inserted_id}")

def read_produto(nome=None):
    mycol = db.produto
    if nome:
        query = {"nome": nome}
        produtos = mycol.find(query)
    else:
        produtos = mycol.find().sort("nome")

    for produto in produtos:
        print(produto)

def update_produto(nome):
    mycol = db.produto
    query = {"nome": nome}
    produto = mycol.find_one(query)

    if produto:
        novo_nome = input("Novo Nome (deixe vazio para manter): ") or produto['nome']
        nova_descricao = input("Nova Descrição (deixe vazio para manter): ") or produto['descricao']
        novo_preco = float(input("Novo Preço (deixe vazio para manter): ") or produto['preco'])
        nova_quantidade = int(input("Nova Quantidade (deixe vazio para manter): ") or produto['quantidade'])

        novos_valores = {"$set": {"nome": novo_nome, "descricao": nova_descricao, "preco": novo_preco, "quantidade": nova_quantidade}}
        mycol.update_one(query, novos_valores)
        print("Produto atualizado com sucesso.")
    else:
        print("Produto não encontrado.")

def delete_produto(nome):
    mycol = db.produto
    query = {"nome": nome}
    resultado = mycol.delete_one(query)
    print(f"{resultado.deleted_count} produto(s) deletado(s).")

def create_favorito():
    mycol = db.favorito
    nome_usuario = input("Nome do Usuário: ")
    nome_produto = input("Nome do Produto: ")

    favorito = {"usuario": nome_usuario, "produto": nome_produto}
    resultado = mycol.insert_one(favorito)
    print(f"Favorito inserido com ID {resultado.inserted_id}")

def read_favorito(nome_usuario=None):
    mycol = db.favorito
    if nome_usuario:
        query = {"usuario": nome_usuario}
        favoritos = mycol.find(query)
    else:
        favoritos = mycol.find().sort("usuario")

    for favorito in favoritos:
        print(favorito)

def update_favorito(nome_usuario, nome_produto):
    mycol = db.favorito
    query = {"usuario": nome_usuario, "produto": nome_produto}
    favorito = mycol.find_one(query)

    if favorito:
        novo_produto = input("Novo Produto (deixe vazio para manter): ") or favorito['produto']

        novos_valores = {"$set": {"produto": novo_produto}}
        mycol.update_one(query, novos_valores)
        print("Favorito atualizado com sucesso.")
    else:
        print("Favorito não encontrado.")

def delete_favorito(nome_usuario, nome_produto):
    mycol = db.favorito
    query = {"usuario": nome_usuario, "produto": nome_produto}
    resultado = mycol.delete_one(query)
    print(f"{resultado.deleted_count} favorito(s) deletado(s).")

def create_compra():
    mycol = db.compra
    nome_usuario = input("Nome do Usuário: ")
    nome_produto = input("Nome do Produto: ")
    quantidade = int(input("Quantidade: "))

    compra = {"usuario": nome_usuario, "produto": nome_produto, "quantidade": quantidade}
    resultado = mycol.insert_one(compra)
    print(f"Compra inserida com ID {resultado.inserted_id}")

def read_compra(nome_usuario=None):
    mycol = db.compra
    if nome_usuario:
        query = {"usuario": nome_usuario}
        compras = mycol.find(query)
    else:
        compras = mycol.find().sort("usuario")

    for compra in compras:
        print(compra)

def update_compra(nome_usuario, nome_produto):
    mycol = db.compra
    query = {"usuario": nome_usuario, "produto": nome_produto}
    compra = mycol.find_one(query)

    if compra:
        nova_quantidade = int(input("Nova Quantidade (deixe vazio para manter): ") or compra['quantidade'])

        novos_valores = {"$set": {"quantidade": nova_quantidade}}
        mycol.update_one(query, novos_valores)
        print("Compra atualizada com sucesso.")
    else:
        print("Compra não encontrada.")

def delete_compra(nome_usuario, nome_produto):
    mycol = db.compra
    query = {"usuario": nome_usuario, "produto": nome_produto}
    resultado = mycol.delete_one(query)
    print(f"{resultado.deleted_count} compra(s) deletada(s).")

def main():
    while True:
        print("\nMenu Principal")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Vendedores")
        print("3. Gerenciar Produtos")
        print("4. Gerenciar Favoritos")
        print("5. Gerenciar Compras")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\nGerenciar Usuários")
            print("1. Criar Usuário")
            print("2. Ler Usuário")
            print("3. Atualizar Usuário")
            print("4. Deletar Usuário")
            print("5. Voltar")

            opcao_usuario = input("Escolha uma opção: ")

            if opcao_usuario == '1':
                create_usuario()
            elif opcao_usuario == '2':
                nome = input("Nome do Usuário (deixe vazio para listar todos): ")
                read_usuario(nome)
            elif opcao_usuario == '3':
                nome = input("Nome do Usuário a atualizar: ")
                update_usuario(nome)
            elif opcao_usuario == '4':
                nome = input("Nome do Usuário a deletar: ")
                sobrenome = input("Sobrenome do Usuário a deletar: ")
                delete_usuario(nome, sobrenome)
            elif opcao_usuario == '5':
                continue
            else:
                print("Opção inválida.")

        elif opcao == '2':
            print("\nGerenciar Vendedores")
            print("1. Criar Vendedor")
            print("2. Ler Vendedor")
            print("3. Atualizar Vendedor")
            print("4. Deletar Vendedor")
            print("5. Voltar")

            opcao_vendedor = input("Escolha uma opção: ")

            if opcao_vendedor == '1':
                create_vendedor()
            elif opcao_vendedor == '2':
                nome = input("Nome do Vendedor (deixe vazio para listar todos): ")
                read_vendedor(nome)
            elif opcao_vendedor == '3':
                nome = input("Nome do Vendedor a atualizar: ")
                update_vendedor(nome)
            elif opcao_vendedor == '4':
                nome = input("Nome do Vendedor a deletar: ")
                sobrenome = input("Sobrenome do Vendedor a deletar: ")
                delete_vendedor(nome, sobrenome)
            elif opcao_vendedor == '5':
                continue
            else:
                print("Opção inválida.")

        elif opcao == '3':
            print("\nGerenciar Produtos")
            print("1. Criar Produto")
            print("2. Ler Produto")
            print("3. Atualizar Produto")
            print("4. Deletar Produto")
            print("5. Voltar")

            opcao_produto = input("Escolha uma opção: ")

            if opcao_produto == '1':
                create_produto()
            elif opcao_produto == '2':
                nome = input("Nome do Produto (deixe vazio para listar todos): ")
                read_produto(nome)
            elif opcao_produto == '3':
                nome = input("Nome do Produto a atualizar: ")
                update_produto(nome)
            elif opcao_produto == '4':
                nome = input("Nome do Produto a deletar: ")
                delete_produto(nome)
            elif opcao_produto == '5':
                continue
            else:
                print("Opção inválida.")

        elif opcao == '4':
            print("\nGerenciar Favoritos")
            print("1. Criar Favorito")
            print("2. Ler Favorito")
            print("3. Atualizar Favorito")
            print("4. Deletar Favorito")
            print("5. Voltar")

            opcao_favorito = input("Escolha uma opção: ")

            if opcao_favorito == '1':
                create_favorito()
            elif opcao_favorito == '2':
                nome_usuario = input("Nome do Usuário (deixe vazio para listar todos): ")
                read_favorito(nome_usuario)
            elif opcao_favorito == '3':
                nome_usuario = input("Nome do Usuário: ")
                nome_produto = input("Nome do Produto: ")
                update_favorito(nome_usuario, nome_produto)
            elif opcao_favorito == '4':
                nome_usuario = input("Nome do Usuário: ")
                nome_produto = input("Nome do Produto: ")
                delete_favorito(nome_usuario, nome_produto)
            elif opcao_favorito == '5':
                continue
            else:
                print("Opção inválida.")

        elif opcao == '5':
            print("\nGerenciar Compras")
            print("1. Criar Compra")
            print("2. Ler Compra")
            print("3. Atualizar Compra")
            print("4. Deletar Compra")
            print("5. Voltar")

            opcao_compra = input("Escolha uma opção: ")

            if opcao_compra == '1':
                create_compra()
            elif opcao_compra == '2':
                nome_usuario = input("Nome do Usuário (deixe vazio para listar todos): ")
                read_compra(nome_usuario)
            elif opcao_compra == '3':
                nome_usuario = input("Nome do Usuário: ")
                nome_produto = input("Nome do Produto: ")
                update_compra(nome_usuario, nome_produto)
            elif opcao_compra == '4':
                nome_usuario = input("Nome do Usuário: ")
                nome_produto = input("Nome do Produto: ")
                delete_compra(nome_usuario, nome_produto)
            elif opcao_compra == '5':
                continue
            else:
                print("Opção inválida.")

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
