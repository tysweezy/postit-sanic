from sanic import Sanic
from sanic.response import json, html
from db import *
import os

app = Sanic(__name__)

# servin' all the assets!
app.static('/public', './public')

# single page app...FTW
@app.route("/")
async def index(request):
    template = open(os.getcwd() + '/templates/index.html')
    return html(template.read())

@app.route("api/posts", methods=['GET'])
async def posts(resquest):
    p = []

    for post in Post.select():
        p.append({'title': post.title, 'body': post.body})

    return json(p)

# example of a post request
@app.route('api/post/create', methods=['POST'])
async def create_post(request):
    post = request.json
   
    insert = Post.create(title=post['title'], body=post['body'])
    insert.save()

    return json(post)

app.run(host="0.0.0.0", port=5000, debug=True)