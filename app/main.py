from fastapi import FastAPI
from .router import posts,fief,votes,topics,email
from .database import engine 
from sqladmin import Admin
from .sqladmin_view import PostsAdmin, UserAdmin,TopicsAdmin
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# models.Base.metadata.create_all(bind=engine)

admin = Admin(app, engine)
admin.add_view(PostsAdmin)
admin.add_view(TopicsAdmin)
admin.add_view(UserAdmin)

app.include_router(posts.router)
app.include_router(fief.router)
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

# @app.get('/', response_class=RedirectResponse)
# def home():
#     return "https://pro-hunt.netlify.app/"

@app.get('/')
def home():
    return {"msg":"Hello world!!!"}