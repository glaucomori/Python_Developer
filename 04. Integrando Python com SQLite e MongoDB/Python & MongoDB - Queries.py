import pprint
import pymongo

client = pymongo.MongoClient("mongodb+srv://pymongo:<password>@cluster0.5wo31ce.mongodb.net/?retryWrites=true&w=majority")
db = client.test
collection = db.bank_collection
posts = db.posts

print('\nRecuperação de um documento aplicando filtro')
pprint.pprint(db.posts.find_one({'nome': 'Rita'}))

print('\nDocumentos no banco de dados')
for post in posts.find():
    pprint.pprint(post)

print('\nQuantidade de documentos existentes no banco de dados')
print(posts.count_documents({}))

print('\nRecuperar a quantidade de dados aplicando filtro')
print(posts.count_documents({'tipo': 'Poupança'}))

print('\nRetornar as contas na agência 1')
for post in posts.find({'agencia': 1}):
    pprint.pprint(post)

print('\nOrganizar as contas alfabeticamente pelo nome do cliente')
for post in posts.find().sort('nome'):
    pprint.pprint(post)
