from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from ORM import Pessoas


def RetornaSessionn():
    HOST = "localhost"
    USER = "root"
    PASSWORD = ""
    PORT = "3306"
    DB = "aulapythonfull"
    CONN = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = RetornaSessionn()

x = session.query(Pessoas).filter(Pessoas.id == 2)
x[0].nome = 'Rene'

for i in x:
    print(i.id)