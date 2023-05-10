from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"message": "Hello, Welcome to your post"}


@app.post("/createposts")
async def create_posts():
    return {"message": "Data posted successfully"}
