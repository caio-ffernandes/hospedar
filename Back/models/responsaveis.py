from peewee import Model, AutoField, CharField, DateField, DateTimeField, TextField, ForeignKeyField
from config.database import database
from models.tipo_responsavel import Tipo_RespDB
from models.posts import PostsDB

class ResponsaveisDB(Model):
    id_resposaveis = AutoField()
    nome = CharField(null=True)
    data_in = DateField(null=True)
    data_out = DateField(null=True)
    biografia = TextField(null=True)
    foto = CharField(null=True, max_length=255)  # Mantém a URL/caminho da imagem
    tipos_resps_id_tipos_resps = ForeignKeyField(Tipo_RespDB, backref='responsaveis', column_name='tipos_resps_id_tipos_resps')
    posts_id_post = ForeignKeyField(PostsDB, backref='responsaveis', column_name='posts_id_post')

    class Meta:
        database = database
        table_name = 'responsaveis'
