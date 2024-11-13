from peewee import AutoField, CharField, Model
from config.database import database

class Tipo_RespDB(Model):
    id_tipos_resps = AutoField()
    nome= CharField()

    class Meta:
        database = database
        table_name = 'tipos_resps'
