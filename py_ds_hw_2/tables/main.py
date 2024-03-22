from sqlalchemy import create_engine, Column, Integer, ForeignKey, VARCHAR, Enum 
from sqlalchemy.ext.declarative import declarative_base
from py_ds_hw_2.connection.connection import connection
from sqlalchemy.orm import relationship

Base = declarative_base()

class TaskStatus(Enum):
    NEW = 'new'
    IN_PROGRESS = 'in progress'
    COMPLETED = 'completed'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(VARCHAR(100))
    email = Column(VARCHAR(100), unique=True)
    tasks = relationship("Task", back_populates="user",   cascade="all, delete-orphan", single_parent=True)
    
    def __init__(self, fullname: str ="", email: str = "") -> None:
        super().__init__()
        self.fullname = fullname
        self.email = email

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100))
    description = Column(VARCHAR(100))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='tasks')
    status_id = Column(Integer, ForeignKey('status.id'))
    status = relationship('Status', back_populates='tasks')
    def __init__(self, name: str="", description: str="",user_id:Integer = 1) -> None:
        super().__init__()
        self.name = name
        self.description = description
        self.user_id = user_id

class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(TaskStatus)
    
    tasks = relationship('Task', back_populates='status')
    def __init__(self, name: str="") -> None:
        super().__init__()
        self.name = name




engine = connection.create_engine()
Base.metadata.create_all(engine)