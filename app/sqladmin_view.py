from sqladmin import ModelView
from .models import Post,User,Topic

class PostsAdmin(ModelView, model=Post):
    column_list = [Post.id, Post.title,Post.description,Post.url,Post.created_at,Post.topic_id]
    column_searchable_list =[Post.title]

class UserAdmin(ModelView,model=User):
    column_list = [User.id]
    column_searchable_list =[User.id]

class TopicsAdmin(ModelView,model=Topic):
    column_list= [Topic.id,Topic.name,Topic.content,Topic.created_at,Topic.image_url,Topic.topic_url,Topic.own_topic]
    column_searchable_list = {Topic.id}

