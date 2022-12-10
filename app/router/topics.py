from typing import List
from fastapi import Depends,APIRouter, HTTPException, Response,status
from sqlalchemy.orm import Session
from app import schemas
from app.database import get_db
from .. import models

router=APIRouter(
    prefix='/topics',
    tags=['Topics']
)

@router.get('/',response_model=List[schemas.TopicsOut])
def topics(db:get_db=Depends()):
    topics = db.query(models.Topic).all()
    return topics

@router.get('/{name}',status_code=status.HTTP_200_OK)
async def get_specific_topic(name:str,db:Session=Depends(get_db)):
        get_one_topic = db.query(models.Topic).filter(models.Topic.name==name).first()
        if get_one_topic:
            specific_posts = db.query(models.Post).filter(models.Post.topic_id==name).all() 
            return specific_posts
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Topic with {name} is not found")

@router.post('/',status_code=status.HTTP_201_CREATED)
async def create_topic(topics:schemas.TopicsCreate,db:Session=Depends(get_db)):
    new_topics=models.Topic(**topics.dict())
    db.add(new_topics)
    db.commit()
    db.refresh(new_topics)
    return new_topics
