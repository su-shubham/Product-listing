from typing import Optional
from pydantic import BaseModel, conint

class Topics(BaseModel):
    image_url:str
    topic_url:str
    name:str
    content:str

class TopicsOut(Topics):
    class Config:
        orm_mode=True

class Post(BaseModel):
    url:str
    title:str
    description:str
    topic_id:str
    topic:TopicsOut

class PostOut(Post):
        class Config:
            orm_mode=True

class PostsCreate(Post):
    id:int
    
class User(BaseModel):
    id:str

class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)



