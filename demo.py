from sqlalchemy import create_engine

#in memory only sqlite db
engine = create_engine('sqlite:///demo.db', echo=True)

# Lazy Connecting
# The Engine, when first returned by create_engine(), has not actually tried to connect to the database yet; that happens only the first time it is asked to perform a task against the database.

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Text, Sequence
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    addresses = relationship("Address", order_by="Address.id", backref="user")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)


from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", backref=backref('addresses', order_by=id))

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()