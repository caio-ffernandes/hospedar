from peewee import Model, CharField, DateField, TextField, IntegerField
from config.database import database 

class VwResponsaveis(Model):
    id_resposaveis = IntegerField()
    nome = CharField(null=True)
    data_in = DateField(null=True)
    data_out = DateField(null=True)
    biografia = TextField(null=True)
    foto = CharField(null=True)
    Tipo_Responsavel = CharField(null=True)
    nome_post = CharField(null=False)

    class Meta:
        database = database
        table_name = 'vw_responsaveis'
        primary_key = False
