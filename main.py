from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"message": "Hello, Welcome to your post"}


@app.post("/createposts")
async def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
