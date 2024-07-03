import json

x = '{"nome": "Diogo", "sobrenome": "Branquinho", "enderecos": [{"rua": "Av Guadalupe", "num": "300", "bairro": "Jd Am\u00e9rica", "cidade": "S\u00e3o Jos\u00e9 dos Campos", "estado": "S\u00e3o Paulo", "cep": "12.235-000"}, {"rua": "Est Dr Altino Bondesan", "num": "500", "bairro": "Eug\u00eanio de Melo", "cidade": "S\u00e3o Jos\u00e9 dos Campos", "estado": "S\u00e3o Paulo", "cep": "12.247-016"}]}'
y = json.loads(x) # transforma um json em obj

print(y)
print("")

for i in y["enderecos"]:
    print("----> ",i)

y["enderecos"][0]["num"] = "300 Ap 62"

for i in y["enderecos"]:
    print("----> ",i)





nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
end = [] #isso é uma lista

key = 1

while (key != 'N'):
    rua = input("Rua: ")
    num = input("Num: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")
    endereco = {        #isso nao eh json, isso é chave-valor, eh um obj
        "rua":rua,
        "num": num,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "cep": cep
    }
    end.append(endereco) #estou inserindo na lista
    key = input("Deseja cadastrar um novo endereço (S/N)? ")

usuario = {  #estou montando o obj final
    "nome" : nome,
    "sobrenome" : sobrenome,
    "enderecos" : end
}
print(json.dumps(usuario)) #estou transformando um obj em json (texto)

