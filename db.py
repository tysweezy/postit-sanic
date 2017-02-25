from peewee import *
from playhouse.db_url import connect

DATABASE = 'mysql://root:root@127.0.0.1:3306/postit_sanic'

database = connect(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database

class Post(BaseModel):
    title = CharField()
    body = TextField()


def create_tables():
    database.connect()
    database.create_tables([Post])
