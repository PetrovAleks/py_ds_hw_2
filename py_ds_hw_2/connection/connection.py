from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session

class Connection:
    def __init__(self)-> None:
        self.engine = self.create_engine()
    

    def create_engine(self)-> Engine:
        connection_string ='postgresql://postgres:mysecretpassword@localhost:5432/postgres'
        return create_engine(connection_string)

    def create_session(self) -> Session:
        Session = sessionmaker(bind=self.engine)
        return Session()


connection = Connection()
