from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "Harry Potter", "content": "Harry Potter and the Prisoner of Azkaban", "id": 1},
            {"title": "Guardians Of the Galaxy", "content": "Volume I-III", "id": 2}]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"MOVIE DATA": my_posts}


@app.post("/createposts")
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000)
    my_posts.append(post_dict)
    return {"data": post_dict}
