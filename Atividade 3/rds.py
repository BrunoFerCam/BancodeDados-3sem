import json
import redis
import pymongo
import secrets
from datetime import datetime
from bson import ObjectId 

conR = redis.Redis(host="redis-12390.c11.us-east-1-2.ec2.cloud.redislabs.com",
                   port=12390,
                   password="FkhYVcHDAmhY417QVYC0qORwjNCS3zD2")
conR.set("user_MiguelC","MiguelC")

client = pymongo.MongoClient("mongodb+srv://root:fatec@teste.kfaa4qw.mongodb.net/?retryWrites=true&w=majority")
global mydb
mydb = client.Mercado_Livre

######################FORNECEDOR#######################
def insertFornecedor():
    mycol = mydb.fornecedor
    print("Iniciando a inserção do fornecedor\n")
    print("\n#### Insert Fornecedor ####")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")

    endereco = {
        "logradouro": input("Logradouro: "),
        "numero": input("Numero: "),
        "complemento": input("Complemento: "),
        "bairro": input("Bairro: "),
        "cidade": input("Cidade: "),
        "estado": input("Estado: "),
        "cep": input("CEP: ")
    }
    
    tipos_telefone = ["CELULAR", "RESIDENCIAL"]
    tipo = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
    while tipo not in tipos_telefone:
        print("Tipo de telefone inválido, escolha entre Celular ou Residencial")
        tipo = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
    numero = input("Número de telefone: ")
    
    telefone = {"tipo": tipo, "numero": numero}
    
    data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    mydict = {"nome": nome, "email": email, "senha": senha, "endereco": [endereco], "telefone": [telefone], "data_criacao": data_criacao}
    inserir = mycol.insert_one(mydict)
    fornecedor_id = inserir.inserted_id

    endereco["_id_fornecedor"] = fornecedor_id
    telefone["_id_fornecedor"] = fornecedor_id
    mycol.update_one({"_id": fornecedor_id}, {"$set": {"endereco": [endereco], "telefone": [telefone]}})


def findFornecedor():
    mycol = mydb.fornecedor
    print("Iniciando a busca de fornecedores\n")
    print("#### Listagem de Fornecedores ####")
    fornecedores = mycol.find()
    for fornecedor in fornecedores:
        print(f"ID: {fornecedor['_id']}")
        print(f"Nome: {fornecedor['nome']}")
        print(f"Email: {fornecedor['email']}")
        print("Endereço:")
        for endereco in fornecedor['endereco']:
            print(f"  Logradouro: {endereco['logradouro']}")
            print(f"  Número: {endereco['numero']}")
            print(f"  Complemento: {endereco['complemento']}")
            print(f"  Bairro: {endereco['bairro']}")
            print(f"  Cidade: {endereco['cidade']}")
            print(f"  Estado: {endereco['estado']}")
            print(f"  CEP: {endereco['cep']}")

        print("Telefone:")
        for telefone in fornecedor['telefone']:
            print(f"  Tipo: {telefone.get('tipo', 'N/A')}")
            print(f"  Número: {telefone.get('numero', 'N/A')}")
        print()


def updateFornecedor(): 
    mycol = mydb.fornecedor

    id_fornecedor = input("Digite o ID do fornecedor que deseja atualizar: ")

    try:
        id_fornecedor = ObjectId(id_fornecedor)
    except Exception as e:
        print("Erro ao converter ID:", e)
        return

    fornecedor_existente = mycol.find_one({"_id": id_fornecedor})
    if fornecedor_existente:
        print("Fornecedor encontrado. Por favor, insira as novas informações.")
    else:
        print("Fornecedor não encontrado.")
        return
    
    nome = fornecedor_existente.get('nome')
    email = fornecedor_existente.get('email')
    senha = fornecedor_existente.get('senha')

    print("\nAtualizando informações do fornecedor\n")
    while True:
        pergunta = input("Deseja atulizar seus dados? (S/N) ").upper()
        while pergunta not in ["S", "N", "SIM", "NAO", "NÃO"]:
            print("Resposta inválida. Tente novamente.")
            pergunta = input("Deseja atulizar seus dados? (S/N) ").upper()
        if pergunta in ["S", "SIM"]:
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            break
        elif pergunta in ["N", "NAO", "NÃO"]:
            break

    endereco_atualizado = fornecedor_existente.get('endereco', {} )
    telefone_atualizado = fornecedor_existente.get('telefone', {})

    while True:
        resposta = input("Deseja Atualizar Endereço? (S/N) ").upper()
        while resposta not in ["S", "N", "SIM", "NAO", "NÃO"]:
            print("Resposta inválida. Tente novamente.")
            resposta = input("Deseja Atualizar Endereço? (S/N) ").upper()
        if resposta in ["S", "SIM"]:
            endereco_atualizado = {
                "logradouro": input("Logradouro: "),
                "numero": input("Numero: "),
                "complemento": input("Complemento: "),
                "bairro": input("Bairro: "),
                "cidade": input("Cidade: "),
                "estado": input("Estado: "),
                "cep": input("CEP: ")
            }
            break
        elif resposta in ["N", "NAO", "NÃO"]:
            break

    while True:
        resposta = input("Deseja Atualizar Telefone? (S/N) ").upper()
        while resposta not in ["S", "N", "SIM", "NAO", "NÃO"]:
            print("Resposta inválida. Tente novamente.")
            resposta = input("Deseja Atualizar Telefone? (S/N) ").upper()
        if resposta in ["S", "SIM"]:
            tipo = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
            while tipo not in ["CELULAR", "RESIDENCIAL"]:
                print("Tipo de telefone inválido. Tente novamente.")
                tipo = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
            numero = input("Número de telefone: ")
            telefone_atualizado = {"tipo": tipo, "numero": numero}
            break
        elif resposta in ["N", "NAO", "NÃO"]:
            break
    
    while True:
        resposta_endereco = input("Deseja adicionar mais um endereço? (S/N) ").upper()
        while resposta_endereco not in ["S", "N", "SIM", "NAO", "NÃO"]:
            print("Resposta inválida. Tente novamente.")
            resposta_endereco = input("Deseja adicionar mais um endereço? (S/N) ").upper()
        if resposta_endereco in ["S", "SIM"]:
            endereco = {
                "logradouro": input("Logradouro: "),
                "numero": input("Numero: "),
                "complemento": input("Complemento: "),
                "bairro": input("Bairro: "),
                "cidade": input("Cidade: "),
                "estado": input("Estado: "),
                "cep": input("CEP: ")
            }
            endereco_atualizado.append(endereco)
        elif resposta_endereco in ["N", "NAO", "NÃO"]:
            break

    while True:
        resposta_telefone = input("Deseja adicionar mais um telefone? (S/N) ").upper()
        while resposta_telefone not in ["S", "N", "SIM", "NAO", "NÃO"]:
            print("Resposta inválida. Tente novamente.")
            resposta_telefone = input("Deseja Atualizar Telefone? (S/N) ").upper()
        if resposta_telefone in ["S", "SIM"]:
            tipo = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
            while tipo not in ["CELULAR", "RESIDENCIAL"]:
                print("Tipo de telefone inválido. Tente novamente.")
                tipo = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
            numero = input("Número de telefone: ")
            telefone_atualizado.append({"tipo": tipo, "numero": numero})
            break
        elif resposta in ["N", "NAO", "NÃO"]:
            break

    atualizacao = {
        "$set": {
            "nome": nome,
            "email": email,
            "senha": senha,
            "endereco": endereco_atualizado,
            "telefone": telefone_atualizado
        }
    }
    mycol.update_one({"_id": id_fornecedor}, atualizacao)
    print("Fornecedor atualizado com sucesso")


def deleteFornecedor():
    mycol = mydb.fornecedor
    id_fornecedor = input("Qual o id do fornecedor que deseja excluir?: ")
    fornecedor_existente = mycol.delete_one({"_id": ObjectId(id_fornecedor)})
    if fornecedor_existente:
        print("Fornecedor excluído com sucesso")
    else:
        print("Fornecedor não encontrado")


######################USUARIO#######################
def insertUsuario():
    mycol = mydb.usuario
    print("Iniciando a inserção do usuário\n")
    print("\n#### Insert Usuário ####")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")

    endereco = {
        "logradouro": input("Logradouro: "),
        "numero": input("Numero: "),
        "complemento": input("Complemento: "),
        "bairro": input("Bairro: "),
        "cidade": input("Cidade: "),
        "estado": input("Estado: "),
        "cep": input("CEP: ")
    }
    
    tipos_telefone = ["CELULAR", "RESIDENCIAL"]
    tipo = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
    while tipo not in tipos_telefone:
        print("Tipo de telefone inválido, escolha entre Celular ou Residencial")
        tipo = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
    numero = input("Número de telefone: ")
    
    telefone = {"tipo": tipo, "numero": numero}
    
    data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    mydict = {"nome": nome, "email": email, "senha": senha, "endereco": [endereco], "telefone": [telefone], "data_criacao": data_criacao}
    inserir = mycol.insert_one(mydict)
    usuario_id = inserir.inserted_id

    endereco["_id_usuario"] = usuario_id
    telefone["_id_usuario"] = usuario_id
    mycol.update_one({"_id": usuario_id}, {"$set": {"endereco": [endereco], "telefone": [telefone]}})


def findUsuario():
    mycol = mydb.usuario
    print("Iniciando a busca de usuários\n")
    print("#### Listagem de Usuários ####")
    usuarios = mycol.find()
    for usuario in usuarios:
        print(f"ID: {usuario['_id']}")
        print(f"Nome: {usuario['nome']}")
        print(f"Email: {usuario['email']}")
        print(f"Senha: {usuario['senha']}")
        print("Endereço:")
        for endereco in usuario['endereco']:
            print(f"  Logradouro: {endereco['logradouro']}")
            print(f"  Número: {endereco['numero']}")
            print(f"  Complemento: {endereco['complemento']}")
            print(f"  Bairro: {endereco['bairro']}")
            print(f"  Cidade: {endereco['cidade']}")
            print(f"  Estado: {endereco['estado']}")
            print(f"  CEP: {endereco['cep']}")

        print("Telefone:")
        for telefone in usuario['telefone']:
            print(f"  Tipo: {telefone.get('tipo', 'N/A')}")
            print(f"  Número: {telefone.get('numero', 'N/A')}")
        print()


def updateUsuario(): 
    mycol = mydb.usuario

    id_usuario = input("Digite o ID do usuário que deseja atualizar: ")

    try:
        id_usuario = ObjectId(id_usuario)
    except Exception as e:
        print("Erro ao converter ID:", e)
        return

    usuario_existente = mycol.find_one({"_id": id_usuario})
    if usuario_existente:
        print("Usuário encontrado. Por favor, insira as novas informações.")
    else:
        print("Usuário não encontrado.")
        return
    
    nome = usuario_existente.get('nome')
    email = usuario_existente.get('email')
    senha = usuario_existente.get('senha')

    print("\nAtualizando informações do usuário\n")
    while True:
        pergunta = input("Deseja atualizar seus dados? (S/N) ").upper()
        while pergunta not in ["S", "N", "SIM", "NAO", "NÃO"]:
            print("Resposta inválida. Tente novamente.")
            pergunta = input("Deseja atualizar seus dados? (S/N) ").upper()
        if pergunta in ["S", "SIM"]:
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            break
        elif pergunta in ["N", "NAO", "NÃO"]:
            break

    endereco_atualizado = usuario_existente.get('endereco', [] )
    telefone_atualizado = usuario_existente.get('telefone', [])

    while True:
        resposta = input("Deseja Atualizar Endereço? (S/N) ").upper()
        while resposta not in ["S", "N", "SIM", "NAO", "NÃO"]:
            print("Resposta inválida. Tente novamente.")
            resposta = input("Deseja Atualizar Endereço? (S/N) ").upper()
        if resposta in ["S", "SIM"]:
            endereco_atualizado = {
                "logradouro": input("Logradouro: "),
                "numero": input("Numero: "),
                "complemento": input("Complemento: "),
                "bairro": input("Bairro: "),
                "cidade": input("Cidade: "),
                "estado": input("Estado: "),
                "cep": input("CEP: ")
            }
            break
        elif resposta in ["N", "NAO", "NÃO"]:
            break

    while True:
        resposta = input("Deseja Atualizar Telefone? (S/N) ").upper()
        while resposta not in ["S", "N", "SIM", "NAO", "NÃO"]:
            print("Resposta inválida. Tente novamente.")
            resposta = input("Deseja Atualizar Telefone? (S/N) ").upper()
        if resposta in ["S", "SIM"]:
            tipo = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
            while tipo not in ["CELULAR", "RESIDENCIAL"]:
                print("Tipo de telefone inválido. Tente novamente.")
                tipo = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
            numero = input("Número de telefone: ")
            telefone_atualizado.append({"tipo": tipo, "numero": numero})
            break
        elif resposta in ["N", "NAO", "NÃO"]:
            break

    while True:
        resposta_endereco = input("Deseja adicionar mais um endereço? (S/N) ").upper()
        while resposta_endereco not in ["S", "N", "SIM", "NAO", "NÃO"]:
            print("Resposta inválida. Tente novamente.")
            resposta_endereco = input("Deseja adicionar mais um endereço? (S/N) ").upper()
        if resposta_endereco in ["S", "SIM"]:
            novo_endereco = {
                "logradouro": input("Logradouro: "),
                "numero": input("Numero: "),
                "complemento": input("Complemento: "),
                "bairro": input("Bairro: "),
                "cidade": input("Cidade: "),
                "estado": input("Estado: "),
                "cep": input("CEP: ")
            }
            endereco_atualizado.append(novo_endereco)
        elif resposta_endereco in ["N", "NAO", "NÃO"]:
            break

    while True:
        resposta_telefone = input("Deseja adicionar mais um telefone? (S/N) ").upper()
        while resposta_telefone not in ["S", "N", "SIM", "NAO", "NÃO"]:
            print("Resposta inválida. Tente novamente.")
            resposta_telefone = input("Deseja adicionar mais um telefone? (S/N) ").upper()
        if resposta_telefone in ["S", "SIM"]:
            tipo = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
            while tipo not in ["CELULAR", "RESIDENCIAL"]:
                print("Tipo de telefone inválido. Tente novamente.")
                tipo = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
            numero = input("Número de telefone: ")
            telefone_atualizado.append({"tipo": tipo, "numero": numero})
            break
        elif resposta_telefone in ["N", "NAO", "NÃO"]:
            break

    atualizacao = {
        "$set": {
            "nome": nome,
            "email": email,
            "senha": senha,
            "endereco": endereco_atualizado,
            "telefone": telefone_atualizado
        }
    }
    mycol.update_one({"_id": id_usuario}, atualizacao)
    print("Usuário atualizado com sucesso")


def deleteUsuario():
    mycol = mydb.usuario
    id_usuario = input("Qual o id do usuário que deseja excluir?: ")
    usuario_existente = mycol.delete_one({"_id": ObjectId(id_usuario)})
    if usuario_existente:
        print("Usuário excluído com sucesso")
    else:
        print("Usuário não encontrado")


######################PRODUTO#######################
def insertProduto():
    mycol_produto = mydb.produto
    mycol_fornecedor = mydb.fornecedor
    
    print("Iniciando a inserção do produto\n")
    print("\n#### Inserir Produto ####")
    nome = input("Nome do Produto: ")
    quantidade = input("Quantidade do Produto: ")
    descricao = input("Descrição do Produto: ")
    preco = input("Preço do Produto: ")
    marca = input("Marca do Produto: ")
    categoria = input("Categoria do Produto: ")
    imagem = input("URL da Imagem do Produto: ")
    data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    fornecedor_id = input("ID do Fornecedor Associado: ")
    
    fornecedor_existente = mycol_fornecedor.find_one({"_id": ObjectId(fornecedor_id)})
    if not ObjectId.is_valid(fornecedor_id):
        print("ID inválido. verifique o ID do fornecedor e tente novamente.")
        return

    if not fornecedor_existente:
        print(f"Fornecedor com ID {fornecedor_id} não encontrado.")
        print("Por favor, verifique o ID do fornecedor e tente novamente.")
        return
    
    produto_dict = {
        "nome": nome,
        "quantidade": quantidade,
        "descricao": descricao,
        "preco": preco,
        "marca": marca,
        "categoria": categoria,
        "imagem": imagem,
        "data_criacao": data_criacao,
        "fornecedor_id": ObjectId(fornecedor_id)
    }
    
    inserir = mycol_produto.insert_one(produto_dict)
    
    mycol_fornecedor.update_one(
        {"_id": ObjectId(fornecedor_id)},
        {"$addToSet": {"produtos": str(inserir.inserted_id)}}
    )
    
    print("Produto inserido com sucesso.")



def findProduto():
    mycol = mydb.produto
    print("#### Listagem de Todos os Produtos ####")
    produtos = mycol.find()
    for produtos in produtos:
        print(f"ID: {produtos['_id']}")
        print(f"Nome: {produtos['nome']}")
        print(f"Quantidade: {produtos['quantidade']}")
        print(f"Descrição: {produtos['descricao']}")
        print(f"Preço: {produtos['preco']}")
        print(f"Categoria: {produtos['categoria']}")
        print(f"Marca: {produtos['marca']}")
        print(f"Imagem: {produtos['imagem']}")
        print(f"Data de Criação: {produtos['data_criacao']}")
        print(f"ID do fornecedor: {produtos['fornecedor_id']}")
        print()



def updateProduto():
    mycol = mydb.produto

    id_produto = input("Digite o ID do produto que deseja atualizar: ")
    id_produto = ObjectId(id_produto)

    if not ObjectId.is_valid(id_produto):
        print("ID inválido. Verifique o ID e tente novamente.")
        return

    produto_existente = mycol.find_one({"_id": id_produto})
    if produto_existente:
        print("Produto encontrado. Por favor, insira as novas informações.")
    else:
        print("Produto não encontrado.")
        return

    nome = produto_existente.get('nome')
    quantidade = produto_existente.get('quantidade')
    descricao = produto_existente.get('descricao')
    preco = produto_existente.get('preco')
    marca = produto_existente.get('marca')
    categoria = produto_existente.get('categoria')
    imagem = produto_existente.get('imagem')

    print("\nAtualizando informações do produto\n")
    nome = input("Novo nome: ")
    quantidade = input("Nova quantidade: ")
    descricao = input("Nova descrição: ")
    preco = float(input("Novo preço: "))
    marca = input("Nova marca: ")
    categoria = input("Nova categoria: ")
    imagem = input("Nova URL da imagem: ")

    atualizacao = {
        "$set": {
            "nome": nome,
            "quantidade": quantidade,
            "descricao": descricao,
            "preco": preco,
            "marca": marca,
            "categoria": categoria,
            "imagem": imagem
        }
    }
    mycol.update_one({"_id": id_produto}, atualizacao)
    print("Produto atualizado com sucesso.")


def deleteProduto():
    mycol = mydb.produto

    id_produto = input("Digite o ID do produto que deseja excluir: ")
    id_produto = ObjectId(id_produto)

    if not ObjectId.is_valid(id_produto):
        print("ID inválido. Verifique o ID e tente novamente.")
        return

    produto_existente = mycol.delete_one({"_id": id_produto})
    if produto_existente:
        print("Produto excluído com sucesso.")
    else:
        print("Produto não encontrado.")


######################FAVORITOS#######################
def insertFavorito():
    mycol_favoritos = mydb.favoritos
    mycol_usuario = mydb.usuario
    mycol_produto = mydb.produto
    
    print("Adicionando produto aos favoritos de um usuário\n")
    
    usuario_id = input("ID do Usuário: ")
    
    if not ObjectId.is_valid(usuario_id):
        print("ID de usuário inválido. Verifique o ID e tente novamente.")
        return

    usuario_existente = mycol_usuario.find_one({"_id": ObjectId(usuario_id)})
    if not usuario_existente:
        print(f"Usuário com ID {usuario_id} não encontrado.")
        print("Por favor, verifique o ID do usuário e tente novamente.")
        return
    
    produto_id = input("ID do Produto: ")
    
    if not ObjectId.is_valid(produto_id):
        print("ID de produto inválido. Verifique o ID e tente novamente.")
        return

    produto_existente = mycol_produto.find_one({"_id": ObjectId(produto_id)})
    if not produto_existente:
        print(f"Produto com ID {produto_id} não encontrado.")
        print("Por favor, verifique o ID do produto e tente novamente.")
        return
    
    favoritos_dict = {
        "usuario_id": ObjectId(usuario_id),
        "produto_id": ObjectId(produto_id),
        "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    
    mycol_favoritos.insert_one(favoritos_dict)
    print("Produto adicionado aos favoritos com sucesso.")



def findFavorito():
    mycol_favoritos = mydb.favoritos
    mycol_usuario = mydb.usuario
    mycol_produto = mydb.produto

    id_usuario = input("Digite o ID do usuário para listar os favoritos: ")

    try:
        id_usuario = ObjectId(id_usuario)
    except Exception as e:
        print("Erro ao converter ID do usuário:", e)
        return

    usuario = mycol_usuario.find_one({"_id": id_usuario})
    if not usuario:
        print(f"Usuário com ID {id_usuario} não encontrado.")
        return

    nome_usuario = usuario['nome']
    print(f"Listando favoritos do usuário {nome_usuario} (ID: {id_usuario})\n")

    favoritos = mycol_favoritos.find({"usuario_id": id_usuario})

    for favorito in favoritos:
        try:
            id_produto = ObjectId(favorito['produto_id'])
        except Exception as e:
            print(f"Erro ao converter ID do produto: {e}")
            continue
        
        data_criacao = favorito['data_criacao']

        produto = mycol_produto.find_one({"_id": id_produto})
        if not produto:
            print(f"Produto com ID {id_produto} não encontrado.")
            continue
        nome_produto = produto['nome']
        preco_produto = produto['preco']
        imagem_produto = produto['imagem']

        print(f"ID do Favorito: {favorito['_id']}")
        print(f"ID do Usuário: {id_usuario}")
        print(f"Nome do Usuário: {nome_usuario}")
        print(f"ID do Produto: {id_produto}")
        print(f"Nome do Produto: {nome_produto}")
        print(f"Preço do Produto: {preco_produto}")
        print(f"Imagem do Produto: {imagem_produto}")
        print(f"Data de Criação: {data_criacao}")
        print()



def updateFavorito():
    mycol_favoritos = mydb.favoritos
    mycol_usuario = mydb.usuario
    mycol_produto = mydb.produto
    
    print("Adicionando novo favorito ao usuário\n")
    
    usuario_id = input("ID do Usuário: ")
    if not ObjectId.is_valid(usuario_id):
        print("ID de usuário inválido. Verifique o ID e tente novamente.")
        return
    
    usuario_existente = mycol_usuario.find_one({"_id": ObjectId(usuario_id)})
    if not usuario_existente:
        print(f"Usuário com ID {usuario_id} não encontrado.")
        print("Por favor, verifique o ID do usuário e tente novamente.")
        return
    
    produto_id = input("ID do Produto: ")
    if not ObjectId.is_valid(produto_id):
        print("ID de produto inválido. Verifique o ID e tente novamente.")
        return
    
    produto_existente = mycol_produto.find_one({"_id": ObjectId(produto_id)})
    if not produto_existente:
        print(f"Produto com ID {produto_id} não encontrado.")
        print("Por favor, verifique o ID do produto e tente novamente.")
        return
    
    favorito_dict = {
        "usuario_id": ObjectId(usuario_id),
        "produto_id": ObjectId(produto_id),
        "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    
    mycol_favoritos.insert_one(favorito_dict)
    print("Novo favorito adicionado ao usuário com sucesso.")


def deleteFavorito():
    mycol_favoritos = mydb.favoritos
    
    favorito_id = input("Digite o ID do favorito que deseja excluir: ")
    
    if not ObjectId.is_valid(favorito_id):
        print("ID de favorito inválido. Verifique o ID e tente novamente.")
        return
    
    favorito_existente = mycol_favoritos.find_one({"_id": ObjectId(favorito_id)})
    if not favorito_existente:
        print("Favorito não encontrado.")
        return
    
    mycol_favoritos.delete_one({"_id": ObjectId(favorito_id)})
    print("Favorito excluído com sucesso.")


######################FAVORITOS#######################
def realizarCompra():
    mycol_usuario = mydb.usuario
    mycol_produto = mydb.produto
    mycol_compras = mydb.compras
    
    print("Realizando Compra\n")
    
    id_usuario = input("ID do Usuário: ")
    if not ObjectId.is_valid(id_usuario):
        print("ID de usuário inválido. Verifique o ID e tente novamente.")
        return
    
    usuario_existente = mycol_usuario.find_one({"_id": ObjectId(id_usuario)})
    if not usuario_existente:
        print(f"Usuário com ID {id_usuario} não encontrado.")
        print("Por favor, verifique o ID do usuário e tente novamente.")
        return
    
    produtos_compra = []
    valor_total = 0
    
    while True:
        id_produto = input("ID do produto que deseja comprar: ")
        if not ObjectId.is_valid(id_produto):
            print("ID de produto inválido. Verifique o ID e tente novamente")
            continue
        
        produto_existente = mycol_produto.find_one({"_id": ObjectId(id_produto)})
        if not produto_existente:
            print(f"Produto com ID {id_produto} não encontrado")
            print("Por favor, verifique o ID do produto e tente novamente")
            continue
        
        try:
            quantidade = int(input("Quantidade do Produto: "))
            if quantidade <= 0:
                print("Quantidade inválida. A quantidade deve ser maior que zero.")
                continue
        except ValueError:
            print("Quantidade inválida. Insira um valor numérico.")
            continue
        
        valor_produto = produto_existente['preco'] * quantidade
        valor_total += valor_produto
        
        produtos_compra.append({
            "produto_id": ObjectId(id_produto),
            "fornecedor_id": produto_existente['fornecedor_id'],
            "quantidade": quantidade,
            "valor_produto": valor_produto
        })
        
        continuar = input("Deseja adicionar mais produtos? (S/N): ").strip().lower()
        if continuar != 's':
            break
    
    if not produtos_compra:
        print("Nenhum produto selecionado. A compra não pode ser realizada.")
        return
    
    forma_pagamento = input("Forma de pagamento (PIX ou Cartão de Crédito): ").lower()
    while forma_pagamento not in ["pix", "cartão de crédito"]:
        print("Forma de pagamento inválida. Escolha entre PIX ou Cartão de Crédito.")
        forma_pagamento = input("Forma de pagamento (PIX ou Cartão de Crédito): ").lower()
    
    data_pagamento = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    pagamento_dict = {
        "usuario_id": ObjectId(id_usuario),
        "produtos": produtos_compra,
        "valor_total": valor_total,
        "forma_pagamento": forma_pagamento,
        "data_pagamento": data_pagamento
    }
    mycol_compras.insert_one(pagamento_dict)
    
    print("Compra realizada com sucesso.")


def listarComprasUsuario():
    mycol_compras = mydb.compras
    mycol_usuario = mydb.usuario
    mycol_produto = mydb.produto
    
    print("Listando Compras por Usuário\n")
    
    id_usuario = input("ID do Usuário: ")
    if not ObjectId.is_valid(id_usuario):
        print("ID de usuário inválido. Verifique o ID e tente novamente.")
        return
    
    usuario_existente = mycol_usuario.find_one({"_id": ObjectId(id_usuario)})
    if not usuario_existente:
        print(f"Usuário com ID {id_usuario} não encontrado.")
        print("Por favor, verifique o ID do usuário e tente novamente.")
        return
    
    compras_usuario = mycol_compras.find({"usuario_id": ObjectId(id_usuario)})
    
    for compra in compras_usuario:
        print(f"ID da Compra: {compra['_id']}")
        print(f"Data da Compra: {compra['data_pagamento']}")
        print(f"Forma de Pagamento: {compra['forma_pagamento']}")
        print("Produtos:")
        for produto in compra['produtos']:
            produto_info = mycol_produto.find_one({"_id": produto['produto_id']})
            print(f"  - Nome: {produto_info['nome']}")
            print(f"    Quantidade: {produto['quantidade']}")
            print(f"    Valor: R${produto['valor_produto']:.2f}")
        print()


######################REDIS######################
def moverProdutoRedis():
    print("Movendo produto do MongoDB para o Redis\n")
    mycol = mydb.produto
    produto_id = input("Digite o ID do produto que deseja mover para o Redis: ")
    
    try:
        produto_id = ObjectId(produto_id)
    except Exception:
        print("ID do produto inválido")
        return

    produto = mycol.find_one({"_id": produto_id})

    if produto:
        chave = str(produto_id)
        conR.delete(chave)
        conR.set(chave, json.dumps(produto, default=str))
        print(f"Produto ID: {produto_id} movido para o Redis")
    else:
        print("Produto não encontrado no MongoDB")

def manipularProdutoRedis():
    print("Manipulando produto no Redis\n")
    produto_id = input("Digite o ID do produto que deseja manipular: ")
    
    try:
        produto_id = ObjectId(produto_id)
    except Exception:
        print("ID do produto inválido")
        return
    
    chave = str(produto_id)
    produto_json = conR.get(chave)
    if not produto_json:
        print("Produto não encontrado no Redis")
        return

    produto = json.loads(produto_json)

    novo_preco = input("Digite o novo preço do produto: ")
    produto['preco'] = novo_preco

    conR.set(chave, json.dumps(produto))

    print(f"Produto ID: {produto_id}")
    print("Manipulação concluída")

def moverProdutoMongoDB():
    print("Movendo produtos do Redis de volta para o MongoDB\n")
    produto_id = input("Digite o ID do produto que deseja mover de volta para o MongoDB: ")
    
    try:
        produto_id = ObjectId(produto_id)
    except Exception:
        print("ID do produto inválido.")
        return
    
    chave = str(produto_id)
    produto_json = conR.get(chave)
    if not produto_json:
        print("Produto não encontrado no Redis.")
        return

    produto = json.loads(produto_json)

    mycol = mydb.produto
    produto['_id'] = produto_id
    mycol.update_one({"_id": produto_id}, {"$set": produto}, upsert=True)
    conR.delete(chave)

    print(f"Produto ID: {produto_id} movido de volta para o MongoDB e removido do Redis.")


def moverUsuarioRedis():
    print("Movendo Usuário para o Redis\n")
    mycol = mydb.usuario
    usuario_id = input("Digite o ID do Usuário que deseja mover para o Redis: ")

    try:
        usuario_id = ObjectId(usuario_id)
    except Exception:
        print("ID do Usuário inválido")

    usuario = mycol.find_one({"_id": usuario_id})

    if usuario:
        chave = str(usuario_id)
        conR.delete(chave)
        conR.set(chave, json.dumps(usuario, default=str))
        print(f"Usuário ID: {usuario_id} movido para o Redis")
    else:
        print("Usuário não encontrado no MongoDB")

def manipularUsuarioRedis():
    print("Manipulando usuario no Redis\n")
    usuario_id = input("Digite o ID do Usuário que deseja manipular: ")

    try:
        usuario_id = ObjectId(usuario_id)
    except Exception:
        print("ID do Usuário inválido")

    chave = str(usuario_id)
    usuario_json = conR.get(chave)
    if not usuario_json:
        print("Usuário não encontrado no Redis")
        return
    
    usuario = json.loads(usuario_json)

    novo_nome = input("Digite o novo nome do usuário: ")
    usuario["nome"] = novo_nome

    conR.set(chave, json.dumps(usuario))

    print(f"Usuário ID: {usuario_id}")
    print("Manipulação concluída")

def moverUsuarioMongoDB():
    print("Movendo produtos do Redis de volta para o MongoDB\n")
    usuario_id = input("Digite o ID do usuário que deseja mover de volta para o MongoDB: ")
    
    try:
        usuario_id = ObjectId(usuario_id)
    except Exception:
        print("ID do usuário inválido")
        return
    
    chave = str(usuario_id)
    usuario_json = conR.get(chave)
    if not usuario_json:
        print("Usuário não encontrado no Redis")
        return

    usuario = json.loads(usuario_json)

    mycol = mydb.usuario
    usuario['_id'] = usuario_id
    mycol.update_one({"_id": usuario_id}, {"$set": usuario}, upsert=True)
    conR.delete(chave)

    print(f"Usuario ID: {usuario_id} movido de volta para o MongoDB e removido do Redis.")


def loginUsuario():
    print("Iniciando login do usuário\n")
    mycol = mydb.usuario

    usuario_email = input("Digite o email do usuário: ")
    usuario_senha = input("Digite a senha do usuário: ")

    usuario = mycol.find_one({"email": usuario_email, "senha": usuario_senha})

    if usuario:
        if usuario_senha == usuario['senha'] and usuario_email == usuario['email']:
            usuario_id = str(usuario['_id'])

            if conR.exists(usuario_id):
                print("Usuário já está logado")
                return None
            
            token = secrets.token_hex(16)
            conR.set(usuario_id, token)
            conR.expire(token, 10)

            print(f"Login concluído. Token: {token}")
            return token
        else:
            print("Senha incorreta")
    else:
        print("Usuário não encontrado")


######################MENU#######################
def menu():
    loop = True
    while loop:
        print("""
            1 - Novo Usuario \n
            2 - Novo Fornecedor \n 
            3 - Novo Produto \n
            4 - Novo Favorito \n
            5 - Encontrar Usuario \n
            6 - Encontrar Fornecedor \n
            7 - Encontrar Produto \n
            8- Encontrar Favorito \n
            9 - Atualizar Usuario \n
            10 - Atualizar Fornecedor \n
            11 - Atualizar Produto \n
            12 - Atualizar Favorito \n
            13 - Deletar Usuario \n
            14 - Deletar Fornecedor \n
            15 - Deletar Produto \n
            16 - Deletar Favorito \n
            17 - Realizar Compra \n
            18 - Listar Compras por Usuário \n
            --------------Redis--------------\n
              -----------Produto-----------\n
            19 - Mover Produto Para o Redis \n
            20 - Manipular Produto no Redis \n
            21 - Mover Produto do Redis para o MongoDB \n
              -----------Usuario-----------\n
            22 - Mover Usuario Para o Redis \n
            23 - Manipular Usuario no Redis \n
            24 - Mover Usuario do Redis para o MongoDB \n
              -----------Login-----------\n
            25 - Logar Usuário \n
            0 - Sair \n
        """)
        escolha = input("Digite a Operação desejada: ")
        match escolha:
            case "1":
                insertUsuario()
            case "2":
               insertFornecedor()
            case "3":
                insertProduto()
            case "4":
                insertFavorito()
            case "5":
                findUsuario()
            case "6":
                findFornecedor()
            case "7":
                findProduto()
            case "8":
                findFavorito()
            case "9":
                updateUsuario()
            case "10":
                updateFornecedor()
            case "11":
                updateProduto()
            case "12":
                updateFavorito()
            case "13":
                deleteUsuario()
            case "14":
                deleteFornecedor()
            case "15":
                deleteProduto()
            case "16":
                deleteFavorito()
            case "17":
                realizarCompra()
            case "18":
                listarComprasUsuario()
            case "19":
                moverProdutoRedis()
            case "20":
                manipularProdutoRedis()
            case "21":
                moverProdutoMongoDB()
            case "22":
                moverUsuarioRedis()
            case "23":
                manipularUsuarioRedis()
            case "24":
                moverUsuarioMongoDB()
            case "25":
                loginUsuario()
            case "0":
                print("Saindo...")
                loop = False
menu()