from py_ds_hw_2.connection.connection import connection
from sqlalchemy.orm.session import Session
from py_ds_hw_2.tables.main import User , Status, Task, TaskStatus
from sqlalchemy import func
from faker import Faker
fake = Faker()
import random

domain = 'example.com'
random_number = random.randint(1, 12)
random_status = random.randint(1, 3)
statuses = TaskStatus.enums

def create_user(session: Session, fullname:str, email:str)-> None:
    new_entry = User(fullname, email)
    session.add(new_entry)

def create_task(session: Session, name:str, description:str,user_id:int )-> None:
    new_entry = Task(name=name, description=description)
    session.add(new_entry)

def create_status(session: Session, name:str)-> None:
    new_entry = Status(name=name)
    session.add(new_entry)

def get_user_without_tasks(session: Session)-> list:
    users = session.query(User).filter(User.tasks == None).all()
    print(len(users))    

def get_all_user_tasks(session: Session)-> list:
    users = session.query(User).all()
    tasks = session.query(Task).filter(Task.user_id == users[0].id).all()
    print(tasks)

def update_user_task(session: Session, task_id:int, status:TaskStatus = "new")-> None:
    task = session.query(Task).filter_by(id=task_id).first()
    task.name =status
    session.commit()    

def add_user_task(session: Session, user_id:int)-> None:
    create_task(session, fake.text(10),statuses[random_status] ,user_id )

def get_tasks_by_status(session: Session, status:TaskStatus)-> list:
    tasks = session.query(Task).filter(Task.status_id == status).all()
    print(tasks)

def delete_task(session: Session, task_id:int)-> None:
    task = session.query(Task).filter_by(id=task_id).first()
    session.delete(task)
    session.commit()    

def get_user_by_email(session: Session, email:str)-> list:
    user = session.query(User).filter(User.email == email).all()
    print(user)

def update_user(session: Session, user_id:int, email:str)-> None:
    user = session.query(User).filter_by(id=user_id).first()
    user.email = email
    session.commit()

def count_tasks(session: Session)-> int:
    tasks = session.query(Task.status, func.count(Task.id)).group_by(Task.status).all()
    print(len(tasks))   

def get_user_by_email_domain(session: Session, domain:str)-> list:
    users = session.query(User).filter(User.email.like(f'%@{domain}')).all()
    print(users)

def get_task_by_description(session: Session)-> list:
    tasks = session.query(Task).filter(Task.description != None).all()
    print(tasks)

def add_all()-> None:
    session = connection.create_session()
    create_user(session, fake.name() , fake.email())
    create_status(session,  statuses[random_status])
    create_task(session, fake.text(10),statuses[random_status] , random_number)
    get_all_user_tasks(session)
    get_user_without_tasks(session)
    session.commit()
    session.close()

def init():
    add_all()