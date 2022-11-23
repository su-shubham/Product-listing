from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, PrimaryKeyConstraint, String, text
from sqlalchemy.orm import relationship
from .database import Base


class Topic(Base):
    __tablename__="topics"
    id = Column(Integer,autoincrement='ignore_fk')
    name = Column(String,nullable=False,primary_key=True)
    topic_url=Column(String,nullable=False)
    image_url=Column(String,nullable=False)
    content = Column(String,nullable=False)
    created_at=Column(TIMESTAMP,server_default=text('now()'))
    own_topic=relationship('Post',back_populates="topic")
    

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    url=Column(String,nullable=False)
    title = Column(String,nullable=False)
    description = Column(String,nullable=False)
    published=Column(Boolean,nullable=False,server_default='TRUE')
    created_at=Column(TIMESTAMP,server_default=text('now()'))
    topic_id=Column(String,ForeignKey('topics.name'),nullable=False)
    topic = relationship('Topic',back_populates="own_topic")

class User(Base):
    __tablename__="users"
    id=Column(String,nullable=False,primary_key=True)

class Vote(Base):
    __tablename__="votes"
    user_id=Column(String,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
