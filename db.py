from pymongo import MongoClient #instala esse pacote: pip install pymongo
cliente = MongoClient('localhost', 27017)#host e porta de conexão
banco = cliente.test_database #selecionao bd que será utilizado
colecao = banco.test_collection #coleção que será utilizada

def insert(data):
    colecao.insert_one(data)

def find(data):
    return colecao.find_one(data)

def update(id, data):
    return colecao.update_one({ '_id': id }, {'$set': data })

def delete(id):
    return colecao.delete_one({ '_id': id })
