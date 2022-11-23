from fastapi import Depends,APIRouter
from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAccessTokenInfo, FiefAsync
from fief_client.integrations.fastapi import FiefAuth

router=APIRouter(
    tags=['Users']
)
fief = FiefAsync(  
    "https://hellofief.fief.dev/",
    "ZtMb_HVlWr4IhmUXbBFNyK39s6ZBGEjRz4S8IQ3GOhI",
    "qBV6yxZeV5rAXLxnT7BBORT0WpP9CYs16cXppwJwj7Q",
)

scheme = OAuth2AuthorizationCodeBearer(  
    "https://hellofief.fief.dev/authorize",  
    "https://hellofief.fief.dev/api/token",  
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
