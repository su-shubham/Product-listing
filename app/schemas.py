from typing import List,Dict,Any
from pydantic import BaseModel, conint,EmailStr


class EmailSchema(BaseModel):
    email: List[EmailStr]|None=None

class Topics(BaseModel):
    image_url:str
    topic_url:str
    name:str
    content:str

class TopicsCreate(Topics):
    pass

class TopicsOut(Topics):
    class Config:
        orm_mode=True

class Post(BaseModel):
    url:str
    title:str
    description:str
    topic_id:str
    

class PostOut(Post):
    topic:TopicsOut
    class Config:
            orm_mode=True

class PostsCreate(Post):
    pass
    
class User(BaseModel):
    id:str

class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)



