from model import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib

def retorna_session():
    HOST = "localhost"
    USER = "root"
    PASSWORD = ""
    PORT = "3306"
    DB = "sistemalogin"
    CON = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    engine = create_engine(CON, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

class ControllerCadastro():
    @classmethod
    def verifica_dados(cls, nome, email, senha):
            if len(nome) > 50 or len (nome) < 3:
                return 2
            elif len(email) > 100:
                return 3
            elif len(senha) > 100 or len(senha) < 6:
                return 4
            
            return 1  
    @classmethod

    def cadastrar(cls, nome, email, senha):
        session = retorna_session()
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all()

        if len(usuario) > 0:
            return 5
        
        dados_verificados = cls.verifica_dados(nome, email, senha)

        if dados_verificados != 1:
            return dados_verificados
        
        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            p1 = Pessoa(nome=nome, email=email ,senha=senha)
            session.add(p1)
            session.commit()
            return 1
        
        except Exception as e:
            print(f"Ocorreu um erro {e}")
            return 3

class ControllerLogin():
    @classmethod
    def login(cls, email, senha):
        session = retorna_session()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        logado = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha).all()

        if len(logado) == 1:
            return {'logado': True, 'id': logado[0].id}
        else:
            return False