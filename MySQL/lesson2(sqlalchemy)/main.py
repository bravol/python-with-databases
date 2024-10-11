
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship,sessionmaker


engine = create_engine("mysql+mysqlconnector://root:CISSYbravol%4075@localhost:3306/hr")

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'hr'}
    emp_id = Column(Integer, primary_key=True)
    name = Column(String(length=20))
    position = Column(String(length=25))
    dep_id = Column(Integer, ForeignKey('hr.departments.dep_id'))

    def __repr__(self):
        return f"<name:{self.name}, position:{self.position}>"


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'schema': 'hr'}
    task_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('hr.employees.emp_id'))
    description = Column(String(length=50))
    emp = relationship('Employee')

    def __repr__(self):
        return f"<emp_id:{self.emp_id}, description:{self.description}>"




class Department(Base):
    __tablename__ = 'departments'
    __table_args__ = {'schema': 'hr'}
    dep_id = Column(Integer, primary_key=True)
    name = Column(String(length=20))


sessionmaker = sessionmaker()
sessionmaker.configure(bind=engine)
session = sessionmaker()

emp1 = session.query(Employee).filter_by(name='Brian').all()
print(emp1)
tasks1 = session.query(Task).filter_by(emp_id=1).all()
print(tasks1)
