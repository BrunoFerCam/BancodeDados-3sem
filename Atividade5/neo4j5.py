from neo4j import GraphDatabase
from datetime import datetime
import uuid

uri = "bolt://localhost:7687"
username = "brunoFC"
password = "1ik0yvDXRtS-DWuUD6hgXtt_nzDv5BLha-vQPKEgJN0"

driver = GraphDatabase.driver(uri, auth=(username, password))

def insertFornecedor():
    fornecedor_id = str(uuid.uuid4())
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    logradouro = input("Logradouro: ")
    numero = input("Numero: ")
    complemento = input("Complemento: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")
    tipo_telefone = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
    numero_telefone = input("Número de telefone: ")
    data_criacao = datetime.now().isoformat()

    query = """
    CREATE (f:Fornecedor {
        id: $fornecedor_id, 
        nome: $nome, 
        email: $email, 
        senha: $senha, 
        logradouro: $logradouro, 
        numero: $numero, 
        complemento: $complemento, 
        bairro: $bairro, 
        cidade: $cidade, 
        estado: $estado, 
        cep: $cep, 
        tipo_telefone: $tipo_telefone, 
        numero_telefone: $numero_telefone, 
        data_criacao: $data_criacao
    })
    """
    with driver.session() as session:
        session.run(query, fornecedor_id=fornecedor_id, nome=nome, email=email, senha=senha, 
                    logradouro=logradouro, numero=numero, complemento=complemento, bairro=bairro, 
                    cidade=cidade, estado=estado, cep=cep, tipo_telefone=tipo_telefone, 
                    numero_telefone=numero_telefone, data_criacao=data_criacao)
    print("Fornecedor inserido com sucesso.")

def insertUsuario():
    usuario_id = str(uuid.uuid4())
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    logradouro = input("Logradouro: ")
    numero = input("Numero: ")
    complemento = input("Complemento: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")
    tipo_telefone = input("Escolha o tipo de telefone entre Celular ou Residencial: ").upper()
    numero_telefone = input("Número de telefone: ")
    data_criacao = datetime.now().isoformat()

    query = """
    CREATE (u:Usuario {
        id: $usuario_id, 
        nome: $nome, 
        email: $email, 
        senha: $senha, 
        logradouro: $logradouro, 
        numero: $numero, 
        complemento: $complemento, 
        bairro: $bairro, 
        cidade: $cidade, 
        estado: $estado, 
        cep: $cep, 
        tipo_telefone: $tipo_telefone, 
        numero_telefone: $numero_telefone, 
        data_criacao: $data_criacao
    })
    """
    with driver.session() as session:
        session.run(query, usuario_id=usuario_id, nome=nome, email=email, senha=senha, 
                    logradouro=logradouro, numero=numero, complemento=complemento, bairro=bairro, 
                    cidade=cidade, estado=estado, cep=cep, tipo_telefone=tipo_telefone, 
                    numero_telefone=numero_telefone, data_criacao=data_criacao)
    print("Usuário inserido com sucesso.")

def insertProduto():
    produto_id = str(uuid.uuid4())
    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))
    marca = input("Marca: ")
    categoria = input("Categoria: ")
    imagem = input("Imagem: ")
    fornecedor_id = input("ID do Fornecedor: ")
    data_criacao = datetime.now().isoformat()

    query = """
    MATCH (f:Fornecedor {id: $fornecedor_id})
    CREATE (p:Produto {
        id: $produto_id, 
        nome: $nome, 
        quantidade: $quantidade, 
        descricao: $descricao, 
        preco: $preco, 
        marca: $marca, 
        categoria: $categoria, 
        imagem: $imagem, 
        data_criacao: $data_criacao
    })-[:FORNECIDO_POR]->(f)
    """
    with driver.session() as session:
        session.run(query, produto_id=produto_id, nome=nome, quantidade=quantidade, descricao=descricao, 
                    preco=preco, marca=marca, categoria=categoria, imagem=imagem, data_criacao=data_criacao, 
                    fornecedor_id=fornecedor_id)
    print("Produto inserido com sucesso")

def realizarCompra():
    print("Realizando Compra\n")
    
    id_usuario = input("ID do Usuário: ")
    with driver.session() as session:
        usuario_existente = session.run("MATCH (u:Usuario {id: $id_usuario}) RETURN u", id_usuario=id_usuario).single()
    if not usuario_existente:
        print(f"Usuário com ID {id_usuario} não encontrado.")
        print("Por favor, verifique o ID do usuário e tente novamente.")
        return
    
    produtos_compra = []
    valor_total = 0
    
    while True:
        id_produto = input("ID do Produto: ")
        with driver.session() as session:
            produto_existente = session.run("MATCH (p:Produto {id: $id_produto}) RETURN p", id_produto=id_produto).single()
        if not produto_existente:
            print(f"Produto com ID {id_produto} não encontrado.")
            print("Por favor, verifique o ID do produto e tente novamente.")
            continue
        
        try:
            quantidade = int(input("Quantidade do Produto: "))
            if quantidade <= 0:
                print("Quantidade inválida. A quantidade deve ser maior que zero.")
                continue
        except ValueError:
            print("Quantidade inválida. Insira um valor numérico.")
            continue
        
        valor_produto = produto_existente['p']['preco'] * quantidade
        valor_total += valor_produto
        
        produtos_compra.append({
            "produto_id": id_produto,
            "fornecedor_id": produto_existente['p']['fornecedor_id'],
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
    
    data_pagamento = datetime.now().isoformat()
    
    compra_id = str(uuid.uuid4())
    
    with driver.session() as session:
        session.run(
            """
            MATCH (u:Usuario {id: $id_usuario})
            CREATE (c:Compra {
                id: $compra_id, 
                valor_total: $valor_total, 
                forma_pagamento: $forma_pagamento, 
                data_pagamento: $data_pagamento
            })-[:REALIZADA_POR]->(u)
            """, id_usuario=id_usuario, compra_id=compra_id, valor_total=valor_total, 
            forma_pagamento=forma_pagamento, data_pagamento=data_pagamento)
        for produto in produtos_compra:
            session.run(
                """
                MATCH (p:Produto {id: $produto_id}), (c:Compra {id: $compra_id})
                CREATE (c)-[:INCLUI]->(p)
                """, produto_id=produto["produto_id"], compra_id=compra_id)
    print("Compra realizada com sucesso.")

def listarFornecedores():
    query = "MATCH (f:Fornecedor) RETURN f"
    with driver.session() as session:
        result = session.run(query)
        fornecedores = list(result)
    print("Lista de Fornecedores:")
    for record in fornecedores:
        fornecedor = record["f"]
        print(f"ID: {fornecedor['id']}")
        print(f"Nome: {fornecedor['nome']}")
        print(f"Email: {fornecedor['email']}")
        print("Endereço:")
        print(f"  Logradouro: {fornecedor['logradouro']}")
        print(f"  Número: {fornecedor['numero']}")
        print(f"  Complemento: {fornecedor['complemento']}")
        print(f"  Bairro: {fornecedor['bairro']}")
        print(f"  Cidade: {fornecedor['cidade']}")
        print(f"  Estado: {fornecedor['estado']}")
        print(f"  CEP: {fornecedor['cep']}")
        print("Telefone:")
        print(f"  Tipo: {fornecedor['tipo_telefone']}")
        print(f"  Número: {fornecedor['numero_telefone']}")
        print(f"Data de Criação: {fornecedor['data_criacao']}")
        print()


def listarUsuarios():
    query = "MATCH (u:Usuario) RETURN u"
    with driver.session() as session:
        result = session.run(query)
        usuarios = list(result)
    print("Lista de Usuários:")
    for record in usuarios:
        usuario = record["u"]
        print(f"ID: {usuario['id']}")
        print(f"Nome: {usuario['nome']}")
        print(f"Email: {usuario['email']}")
        print("Endereço:")
        print(f"  Logradouro: {usuario['logradouro']}")
        print(f"  Número: {usuario['numero']}")
        print(f"  Complemento: {usuario['complemento']}")
        print(f"  Bairro: {usuario['bairro']}")
        print(f"  Cidade: {usuario['cidade']}")
        print(f"  Estado: {usuario['estado']}")
        print(f"  CEP: {usuario['cep']}")
        print("Telefone:")
        print(f"  Tipo: {usuario['tipo_telefone']}")
        print(f"  Número: {usuario['numero_telefone']}")
        print(f"Data de Criação: {usuario['data_criacao']}")
        print()

def listarProdutos():
    query = "MATCH (p:Produto)-[:FORNECIDO_POR]->(f:Fornecedor) RETURN p, f"
    with driver.session() as session:
        result = session.run(query)
        produtos = list(result)
    print("Lista de Produtos:")
    for record in produtos:
        produto = record["p"]
        fornecedor = record["f"]
        print(f"ID: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Descrição: {produto['descricao']}")
        print(f"Preço: {produto['preco']}")
        print(f"Marca: {produto['marca']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Imagem: {produto['imagem']}")
        print(f"Data de Criação: {produto['data_criacao']}")
        print("Fornecedor:")
        print(f"  Nome: {fornecedor['nome']}")
        print(f"  Email: {fornecedor['email']}")
        print("  Endereço:")
        print(f"    Logradouro: {fornecedor['logradouro']}")
        print(f"    Número: {fornecedor['numero']}")
        print(f"    Complemento: {fornecedor['complemento']}")
        print(f"    Bairro: {fornecedor['bairro']}")
        print(f"    Cidade: {fornecedor['cidade']}")
        print(f"    Estado: {fornecedor['estado']}")
        print(f"    CEP: {fornecedor['cep']}")
        print("  Telefone:")
        print(f"    Tipo: {fornecedor['tipo_telefone']}")
        print(f"    Número: {fornecedor['numero_telefone']}")
        print()

def listarCompras():
    query = "MATCH (c:Compra)-[:REALIZADA_POR]->(u:Usuario) RETURN c, u"
    with driver.session() as session:
        result = session.run(query)
        compras = list(result)
    print("Lista de Compras:")
    for record in compras:
        compra = record["c"]
        usuario = record["u"]
        print(f"ID da Compra: {compra['id']}")
        print(f"Usuário: {usuario['nome']}")
        print(f"Valor Total: {compra['valor_total']}")
        print(f"Forma de Pagamento: {compra['forma_pagamento']}")
        print(f"Data do Pagamento: {compra['data_pagamento']}")
        produtos_query = "MATCH (c:Compra {id: $compra_id})-[:INCLUI]->(p:Produto) RETURN p"
        with driver.session() as session:
            produtos_result = session.run(produtos_query, compra_id=compra["id"])
            produtos = list(produtos_result)
        for produto_record in produtos:
            produto = produto_record["p"]
            print(f"  Nome: {produto['nome']}")
            print(f"  Quantidade: {produto['quantidade']}")
            print(f"  Preço: {produto['preco']}")
        print()


def menu():
    while True:
        print("=== MENU ===")
        print("1. Inserir Fornecedor")
        print("2. Inserir Usuário")
        print("3. Inserir Produto")
        print("4. Realizar Compra")
        print("5. Listar Fornecedores")
        print("6. Listar Usuários")
        print("7. Listar Produtos")
        print("8. Listar Compras")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            insertFornecedor()
        elif opcao == '2':
            insertUsuario()
        elif opcao == '3':
            insertProduto()
        elif opcao == '4':
            realizarCompra()
        elif opcao == '5':
            listarFornecedores()
        elif opcao == '6':
            listarUsuarios()
        elif opcao == '7':
            listarProdutos()
        elif opcao == '8':
            listarCompras()
        elif opcao == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()