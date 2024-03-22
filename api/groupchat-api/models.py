from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://denstrygin:4054@mariadb:3306/messenger"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    chats = relationship('GroupChatMember', back_populates='user')

class GroupChat(Base):
    __tablename__ = 'group_chats'

    chat_id = Column(Integer, primary_key=True, autoincrement=True)
    chat_name = Column(String(255), nullable=False)
    creator_user_id = Column(Integer, ForeignKey('users.user_id'))
    members = relationship('GroupChatMember', back_populates='chat')

class GroupChatMember(Base):
    __tablename__ = 'group_chat_members'

    chat_id = Column(Integer, ForeignKey('group_chats.chat_id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    chat = relationship('GroupChat', back_populates='members')
    user = relationship('User', back_populates='chats')

class GroupChatMessage(Base):
    __tablename__ = 'group_chat_messages'

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, ForeignKey('group_chats.chat_id'))
    sender_user_id = Column(Integer, ForeignKey('users.user_id'))
    message_content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)