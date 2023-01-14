from fastapi import Depends,APIRouter
from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAccessTokenInfo, FiefAsync
from fief_client.integrations.fastapi import FiefAuth

router=APIRouter(
    tags=['Users']
)
fief = FiefAsync(  
    "{}",
    "{}",
    "{}",
)

scheme = OAuth2AuthorizationCodeBearer(  
    "{}",  
    "{}",  
    scopes={"openid": "openid", "offline_access": "offline_access"},
)

auth = FiefAuth(fief, scheme)  

@router.get("/user")
async def protected(
    access_token_info: FiefAccessTokenInfo = Depends(auth.authenticated()),  
):
        # try:
        #     user_db_query = db.query(models.User).filter(models.User.id==id)
        #     user_db= user_db_query.first()
        #     if not user_db: 
        #             user_id=models.User(id=self['sub'])
        #             print(user_id.id)
        #             db.add(user_id)
        #             db.commit()


        # except UnmappedInstanceError as e:
        #     print(e)
    return access_token_info
