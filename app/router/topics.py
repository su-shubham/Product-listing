from typing import List
from fastapi import Depends,APIRouter, HTTPException, Response,status
from sqlalchemy.orm import Session
from app import schemas
from app.database import get_db
from .. import models
from .fief import auth
from fief_client import FiefAccessTokenInfo

router=APIRouter(
    prefix='/topics',
    tags=['Topics']
)

@router.get('/')
async def topics(db:get_db=Depends()):
    topics = db.query(models.Topic).all()
    return topics
# @router.get('/',response_model=List[schemas.TopicsOut])
# async def topics(db:get_db=Depends()):
#     topics = db.query(models.Topic).all()
#     return topics

@router.get('/{name}',status_code=status.HTTP_200_OK)
async def get_one_topic(name:str,db:Session=Depends(get_db)):
        print(name)
        get_one_topic = db.query(models.Topic).filter(models.Topic.name==name).first()
        if get_one_topic:
            specific_posts = db.query(models.Post).filter(models.Post.topic_id==name).all() 
            print(specific_posts)
            return specific_posts
