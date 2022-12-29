from fastapi import FastAPI,Request
from .router import posts,fief,votes,topics,email
from .database import engine 
from sqladmin import Admin
from .sqladmin_view import PostsAdmin, UserAdmin,TopicsAdmin
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi


app = FastAPI()

# models.Base.metadata.create_all(bind=engine)

admin = Admin(app, engine)
admin.add_view(PostsAdmin)
admin.add_view(TopicsAdmin)
admin.add_view(UserAdmin)

app.include_router(posts.router)
app.include_router(votes.router)
app.include_router(topics.router)
app.include_router(email.router)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/')
async def home(request:Request):
    data = await request.body()
    print(data)
    return {"message":"Success"}

def my_schema():
   openapi_schema = get_openapi(
       title="Prohunt",
       version="0.1.0",
       routes=app.routes,
   )
   openapi_schema["info"] = {
       "title" : "Prohunt",
       "version" : "0.1.0",
       "description" : "Product Listing & Voting API",
   }
   app.openapi_schema = openapi_schema
   return app.openapi_schema

app.openapi = my_schema