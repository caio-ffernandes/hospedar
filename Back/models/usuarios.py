from peewee import AutoField, CharField, Model
from config.database import database

class UsuariosDB(Model):
    id = AutoField()
    nome = CharField(max_length=100)
    email = CharField(max_length=100)
    senha = CharField(max_length=100)
    telefone = CharField(max_length=15, null=True)
    tipo = CharField(max_length=20, default='comum')

    class Meta:
        database = database
        table_name = 'usuarios'
