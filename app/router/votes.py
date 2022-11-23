from fastapi import Depends,APIRouter, HTTPException, Response,status
from sqlalchemy.orm import Session
from app import models
from app.database import get_db
from ..schemas import Vote
from .fief import auth
from fief_client import FiefAccessTokenInfo

router=APIRouter(
    prefix="/vote",
    tags=['Votes']
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def vote(vote:Vote,access_token_info: FiefAccessTokenInfo = Depends(auth.authenticated()),db:Session=Depends(get_db)):

    post = db.query(models.Post).filter(models.Post.id==vote.post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post with {vote.post_id} doesn't exists.")
    
    votes_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,models.User.id == access_token_info['id'])
    found_vote = votes_query.first() 
    if (vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail=f"User with {access_token_info['id']} has already voted on {vote.post_id}"
            )
        new_vote = models.Vote(post_id=vote.post_id,user_id=access_token_info['id'])
        db.add(new_vote)
        db.commit()
        return {"message":"Vote added successfully"}
    else:
        if not found_vote:
            raise HTTPException(status_code = 404,detail=f"Vote doesn't exists")
        votes_query.delete(synchronize_session=False)
        db.commit()
        return {"message":"Vote deleted Successfully"}



