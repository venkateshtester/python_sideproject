from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app= FastAPI()


post: list[dict]=[
    {
        "id": 1,
        "title": "FastAPI is good",
        "content": "content of post 1",
        "author": "user_one",
        "name": "John Doe",
        "message": "Hello everyone!"
    },
    {
        "id": 2,
        "title": "favorite foods",
        "content": "I like pizza",
        "author": "user_two",
        "name": "Jane Smith",
        "message": "Here is my favorite food."
    }
]

@app.get("/", response_class=HTMLResponse)
@app.get("/posts", response_class=HTMLResponse)
def home():
    #return {"message": "Hello world !"}
    return f"<h1>{post[0]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return post