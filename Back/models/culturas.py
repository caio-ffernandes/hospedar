from peewee import AutoField, CharField, Model
from config.database import database

class CulturaDB(Model):
    id_cultura = AutoField()
    nome_cultura = CharField()

    class Meta:
        database = database
        table_name = 'culturas'
