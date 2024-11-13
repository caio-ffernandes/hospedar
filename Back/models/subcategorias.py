from peewee import AutoField, CharField, ForeignKeyField, Model
from config.database import database
from models.culturas import CulturaDB

class SubcategoriasDB(Model):
    id_subcategoria = AutoField()
    nome_subcategoria = CharField()
    culturas = ForeignKeyField(
        model=CulturaDB, backref='subcategorias', column_name='culturas_id_cultura'
    )

    class Meta:
        database = database
        table_name = 'subcategorias'

