from typing import List
from fastapi import Depends,APIRouter, HTTPException, Response,status
from sqlalchemy.orm import Session
from app import schemas
from app.database import get_db
from .. import models
from .fief import auth
from fief_client import FiefAccessTokenInfo

router=APIRouter(
    prefix="/posts",
    tags=['Products']
)

@router.get('/',response_model=List[schemas.PostOut])
async def get_posts(db:Session=Depends(get_db)):
    posts=  db.query(models.Post).all()
    return posts

@router.get('/{id}',response_model=schemas.PostOut)
async def get_one_post(id:int,db:Session=Depends(get_db),access_token_info: FiefAccessTokenInfo = Depends(auth.authenticated())):
    get_one_posts = db.query(models.Post).filter(models.Post.id==id).first()
    

    if access_token_info:
        return get_one_posts
    if not get_one_posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with {id} is not found.")
    


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.PostOut)
async def create_posts(posts:schemas.Post,db:Session=Depends(get_db)):
    new_posts=models.Post(**posts.dict())
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    return new_posts

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_posts(id:int,db:Session=Depends(get_db),access_token_info: FiefAccessTokenInfo = Depends(auth.authenticated())):
    delete_query = db.query(models.Post).filter(models.Post.id==id)
    delete_post = delete_query.first()
    if not delete_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with {id} is Not found")
    db.delete(delete_post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}')
async def update_posts(id:int,updates_post:schemas.PostsCreate,db:Session=Depends(get_db),access_token_info: FiefAccessTokenInfo = Depends(auth.authenticated())):
    update_query = db.query(models.Post).filter(models.Post.id==id)
    if not update_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with {id} is Not found")
    update_query.update(updates_post.dict(),synchronize_session=False)
    db.commit()
    return update_query.first()

