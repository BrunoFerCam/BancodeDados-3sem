import pymongo
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://mane:124578895623@branco.3nl94.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test


global mydb
mydb = client.mercadolivre

def findSort():
    #Sort
    global mydb
    mycol = mydb.usuario
    print("\n####SORT####") 
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)

def findQuery():
    #Query
    global mydb
    mycol = mydb.usuario
    print("\n####QUERY####")
    myquery = { "nome": "Diogo Branquinho" }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def insert(nome, cpf):
    #Insert
    global mydb
    mycol = mydb.usuario
    print("\n####INSERT####")
    mydict = { "nome": nome, "cpf":cpf}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)


############# main

findSort()
findQuery()
insert("Mane eh mane", "123.123.123.11")

