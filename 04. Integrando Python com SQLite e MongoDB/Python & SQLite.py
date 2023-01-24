from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))

    conta = relationship('Conta', back_populates='cliente')

    def __repr__(self):
        return f'Cliente( id = {self.id}, nome = {self.nome}, cpf = {self.cpf}, endereco = "{self.endereco}" )'


class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    saldo = Column(Integer)

    cliente = relationship('Cliente', back_populates='conta')

    def __repr__(self):
        return f'Conta( id = {self.id}, tipo = {self.tipo}, agencia = {self.agencia}, num = {self.num}, id_cliente = {self.id_cliente}, saldo = {self.saldo} )'


# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# investiga o esquema de banco de dados
inspector_engine = inspect(engine)
print()
print(inspector_engine.has_table('cliente'))
print()
print(inspector_engine.has_table('conta'))
print()
print(inspector_engine.get_table_names())
print()
print(inspector_engine.default_schema_name)
print()

with Session(engine) as session:
    joao = Cliente(
        nome = 'Joao',
        cpf = '11111111111',
        endereco = 'Rua 1, nº 11',
        conta = [Conta(
        tipo = 'Poupança',
        agencia = 1,
        num = 1,
        saldo = 1500)])

    maria = Cliente(
        nome = 'Maria',
        cpf = '22222222222',
        endereco = 'Rua 2, nº 22',
        conta = [Conta(
        tipo = 'Poupança',
        agencia = 1,
        num = 2,
        saldo = 525)])

    rita = Cliente(
        nome = 'Rita',
        cpf = '33333333333',
        endereco = 'Rua 3, nº 33',
        conta = [Conta(
        tipo = 'Conta Corrente',
        agencia = 1,
        num = 3,
        saldo = 800)])

    guilherme = Cliente(
        nome = 'Guilherme',
        cpf = '44444444444',
        endereco = 'Rua 4, nº 44',
        conta = [Conta(
        tipo = 'Conta Corrente',
        agencia = 1,
        num = 4,
        saldo = 00)])

    # enviando para o DB
    session.add(joao)
    session.add(maria)
    session.add(rita)
    session.add(guilherme)

    session.commit()

######################## QUERIES ########################

query_cliente = select(Cliente).where(Cliente.nome == 'Joao')
print('\nRecuperando clientes a partir de condição de filtragem')
for cliente in session.scalars(query_cliente):
    print(cliente)


query_conta = select(Conta).where(Conta.id_cliente.in_([3]))
print('\nRecuperando as contas de um cliente com id = 3')
for conta in session.scalars(query_conta):
    print(conta)


query_cliente_ordenado = select(Cliente).order_by(Cliente.nome.asc())
print('\nRecuperando clientes de forma ordenada por nome de forma crescente')
for cliente in session.scalars(query_cliente_ordenado):
    print(cliente)


query_join = select(Cliente.nome, Conta.saldo).join_from(Cliente, Conta)
print('\nRecuperando clientes e os respectivos saldos através de join')
for result in session.scalars(query_join):
    print(result)

######################################################### 

connection = engine.connect()
results = connection.execute(query_join).fetchall()
print('\nRecuperando clientes e os respectivos saldos através de join a partir da connection')
for result in results:
    print(result)

query_count = select(func.count('*')).select_from(Cliente)
print('\nTotal de instâncias em Cliente')
for result in session.scalars(query_count):
    print(result)

# encerrando a session
session.close()
