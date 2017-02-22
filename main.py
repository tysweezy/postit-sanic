from sanic import Sanic
from sanic.response import json, html
from pymongo import MongoClient
import os

app = Sanic(__name__)
client = MongoClient('localhost', 27017)
db = client.postit

# servin' all the assets!
app.static('/public', './public')

# single page app...FTW
@app.route("/")
async def index(request):
    template = open(os.getcwd() + '/templates/index.html')
    return html(template.read())

@app.route("api/posts", methods=['GET'])
async def posts(resquest):
    posts = db.posts.find()
    p = []
    for post in posts:
        p.append({'title': post['title'], 'body': post['body']})

    return json(p)

# example of a post request
@app.route('api/post/create', methods=['POST'])
async def create_post(request):
    post = request.json
    db.posts.insert({'title': post['title'], 'body': post['body']})

    return json(post)

    

app.run(host="0.0.0.0", port=5000, debug=True)