import pprint
import pymongo

client = pymongo.MongoClient("mongodb+srv://pymongo:<password>@cluster0.5wo31ce.mongodb.net/?retryWrites=true&w=majority")
db = client.test

collection = db.bank_collection
print(collection)

new_posts = [{
    'nome': 'Joao',
    'cpf': '11111111111',
    'endereco': 'Rua 1, nº 11',
    'tipo': 'Poupança',
    'agencia': 1,
    'number': 1,
    'saldo': 1500.00
},

{
    'nome': 'Maria',
    'cpf': '22222222222',
    'endereco': 'Rua 2, nº 22',
    'tipo': 'Poupança',
    'agencia': 1,
    'number': 2,
    'saldo': 1575.85
},

{
    'nome': 'Rita',
    'cpf': '33333333333',
    'endereco': 'Rua 3, nº 33',
    'tipo': 'Conta Corrente',
    'agencia': 1,
    'number': 3,
    'saldo': 357.50
},

{
    'nome': 'Guilherme',
    'cpf': '44444444444',
    'endereco': 'Rua 4, nº 44',
    'tipo': 'Conta Corrente',
    'agencia': 1,
    'number': 4,
    'saldo': 4250.60
},

{
    'nome': 'Miguel',
    'cpf': '55555555555',
    'endereco': 'Rua 5, nº 55',
    'tipo': 'Poupança',
    'agencia': 1,
    'number': 5,
    'saldo': 1500.00
}]

posts = db.posts
post_id = posts.insert_many(new_posts).inserted_id
