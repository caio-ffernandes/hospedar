from models.usuariospost import UsuariosHasPostsDB

def create_usuarios_has_posts(data):
    new_record = UsuariosHasPostsDB.create(**data.dict())
    return new_record

def get_all_usuarios_has_posts():
    return [record.to_dict() for record in UsuariosHasPostsDB.select()]

def get_usuarios_has_posts_by_id(record_id):
    try:
        return UsuariosHasPostsDB.get(UsuariosHasPostsDB.id_usuarios_has_postscol == record_id).to_dict()
    except UsuariosHasPostsDB.DoesNotExist:
        return None

def update_usuarios_has_posts(record_id, update_data):
    query = UsuariosHasPostsDB.update(**update_data.dict(exclude_unset=True)).where(UsuariosHasPostsDB.id_usuarios_has_postscol == record_id)
    query.execute()
    return get_usuarios_has_posts_by_id(record_id)

def delete_usuarios_has_posts(record_id):
    query = UsuariosHasPostsDB.delete().where(UsuariosHasPostsDB.id_usuarios_has_postscol == record_id)
    query.execute()
