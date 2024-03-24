from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://denstrygin:4054@proxysql:6033/messenger"

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

class PtpMessage(Base):
    __tablename__ = 'ptp_messages'

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    sender_user_id = Column(Integer, ForeignKey('users.user_id'))
    recipient_user_id = Column(Integer, ForeignKey('users.user_id'))
    message_content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    def as_dict(self):
        return {
            "message_id": self.message_id,
            "sender_user_id": self.sender_user_id,
            "recipient_user_id": self.recipient_user_id,
            "message_content": self.message_content,
            "timestamp": self.timestamp if isinstance(self.timestamp, str) else self.timestamp.isoformat()
        }

Base.metadata.create_all(bind=engine)
