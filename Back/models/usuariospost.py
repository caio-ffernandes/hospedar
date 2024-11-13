from peewee import Model, IntegerField, ForeignKeyField
from playhouse.shortcuts import model_to_dict
from config.database import database
from models.usuarios import UsuariosDB
from models.posts import PostsDB

class UsuariosHasPostsDB(Model):
    usuarios_id = ForeignKeyField(UsuariosDB, backref='usuarios_posts', column_name='usuarios_id')
    posts_id_post = ForeignKeyField(PostsDB, backref='posts_usuarios', column_name='posts_id_post')
    id_usuarios_has_postscol = IntegerField(primary_key=True)

    class Meta:
        database = database
        table_name = 'usuarios_has_posts'

    def to_dict(self):
        return model_to_dict(self)
