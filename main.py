from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Banco de dados SQLite
engine = create_engine('sqlite:///alunos.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Modelo da tabela
class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Aluno(id={self.id}, nome='{self.nome}', email='{self.email}')>"

# Criar tabela se não existir
Base.metadata.create_all(engine)

# Funções CRUD
def adicionar_aluno(nome, email):
    aluno = Aluno(nome=nome, email=email)
    session.add(aluno)
    session.commit()
    print(f"✅ Aluno '{nome}' adicionado com sucesso!")

def listar_alunos():
    alunos = session.query(Aluno).all()
    if alunos:
        print("\n📘 Lista de Alunos:")
        for aluno in alunos:
            print(f"ID: {aluno.id} | Nome: {aluno.nome} | Email: {aluno.email}")
    else:
        print("⚠️ Nenhum aluno cadastrado.")

def atualizar_aluno(id_aluno, novo_nome=None, novo_email=None):
    aluno = session.query(Aluno).get(id_aluno)
    if aluno:
        if novo_nome:
            aluno.nome = novo_nome
        if novo_email:
            aluno.email = novo_email
        session.commit()
        print(f"✏️ Aluno ID {id_aluno} atualizado com sucesso!")
    else:
        print("❌ Aluno não encontrado.")

def deletar_aluno(id_aluno):
    aluno = session.query(Aluno).get(id_aluno)
    if aluno:
        session.delete(aluno)
        session.commit()
        print(f"🗑️ Aluno '{aluno.nome}' deletado com sucesso!")
    else:
        print("❌ Aluno não encontrado.")

# Função RA (Registro do Aluno)
def registro_aluno(nome):
    aluno = session.query(Aluno).filter_by(nome=nome).first()
    if aluno:
        print(f"📧 O e-mail de {nome} é: {aluno.email}")
    else:
        print(f"❌ Nenhum aluno encontrado com o nome '{nome}'.")

# Menu interativo
def menu():
    while True:
        print("\n=== SISTEMA DE ALUNOS ===")
        print("1 - Adicionar aluno")
        print("2 - Listar alunos")
        print("3 - Atualizar aluno")
        print("4 - Deletar aluno")
        print("5 - RA (Registro do Aluno)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            email = input("Email: ")
            adicionar_aluno(nome, email)
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            id_aluno = int(input("ID do aluno: "))
            novo_nome = input("Novo nome (deixe vazio para não alterar): ")
            novo_email = input("Novo email (deixe vazio para não alterar): ")
            atualizar_aluno(id_aluno, novo_nome or None, novo_email or None)
        elif opcao == '4':
            id_aluno = int(input("ID do aluno: "))
            deletar_aluno(id_aluno)
        elif opcao == '5':
            nome = input("Digite o nome do aluno: ")
            registro_aluno(nome)
        elif opcao == '0':
            print("👋 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    menu()
