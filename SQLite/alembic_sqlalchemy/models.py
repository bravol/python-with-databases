from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String,DateTime ,create_engine
from datetime import datetime

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default = datetime.now)
    
    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'  # returns first name and last name concatenated  # example: 'Lumala Brian'
    
    # geting the data
    def __repr__(self):
        return f'UserModel(first_name={self.first_name}, last_name={self.last_name}, birth={self.birth}, created={self.created})'
    
users = [
    UserModel(first_name= 'Lumala', last_name= 'Brian', birth= datetime(1998,5,2)),
    UserModel(first_name= 'Lumala', last_name= 'Bravol', birth= datetime(1998,10,2)),
    UserModel(first_name= 'Brian', last_name= 'Bravol', birth= datetime(1998,6,4)),
]

# interact with database
session_maker = sessionmaker(bind=create_engine('sqlite:///models.db'))

def create_users():
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()

# create_users()
with session_maker() as session:
    user_records = session.query(UserModel).all()
    for user in user_records:
        print(user.full_name)