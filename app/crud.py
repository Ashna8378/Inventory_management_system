# from sqlalchemy.orm import Session
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy import exists
# from app import models, schemas
# from fastapi import HTTPException

# # ===================== SERVER =====================
# def get_servers(db: Session):
#     return db.query(models.Server).all()

# def get_server_by_id(db: Session, server_id: int):
#     return db.query(models.Server).filter(models.Server.id == server_id).first()

# def create_server(db: Session, server: schemas.ServerCreate):
#     db_server = models.Server(**server.dict())
#     db.add(db_server)
#     db.commit()
#     db.refresh(db_server)
#     return db_server

# def update_server(db: Session, server_id: int, server: schemas.ServerCreate):
#     db_server = get_server_by_id(db, server_id)
#     if db_server:
#         for key, value in server.dict().items():
#             setattr(db_server, key, value)
#         db.commit()
#         db.refresh(db_server)
#     return db_server

# def delete_server(db: Session, server_id: int):
#     db_server = get_server_by_id(db, server_id)
#     if db_server:
#         try:
#             db.delete(db_server)
#             db.commit()
#             return db_server
#         except IntegrityError:
#             db.rollback()
#             raise HTTPException(status_code=400, detail="Cannot delete server: It is referenced by another table.")
#     return None


# # ===================== LOCATION =====================
# def get_locations(db: Session):
#     return db.query(models.Location).all()

# def get_location(db: Session, location_id: int):
#     return db.query(models.Location).filter(models.Location.location_id == location_id).first()

# def create_location(db: Session, location: schemas.LocationCreate):
#     db_location = models.Location(**location.dict())
#     db.add(db_location)
#     db.commit()
#     db.refresh(db_location)
#     return db_location

# def update_location(db: Session, location_id: int, updated_location: schemas.LocationCreate):
#     db_location = db.query(models.Location).filter(models.Location.location_id == location_id).first()
#     if db_location:
#         for key, value in updated_location.dict().items():
#             setattr(db_location, key, value)
#         db.commit()
#         db.refresh(db_location)
#     return db_location

# def delete_location(db: Session, location_id: int):
#     if db.query(exists().where(models.Server.location_id == location_id)).scalar():
#         raise HTTPException(status_code=400, detail="Location is associated with existing servers. Cannot delete.")
#     db_location = db.query(models.Location).filter(models.Location.location_id == location_id).first()
#     if db_location:
#         db.delete(db_location)
#         db.commit()
#     return db_location


# # ===================== OS =====================
# def get_oses(db: Session):
#     return db.query(models.OS).all()

# def get_os(db: Session, os_id: int):
#     return db.query(models.OS).filter(models.OS.os_id == os_id).first()

# def create_os(db: Session, os: schemas.OSCreate):
#     db_os = models.OS(**os.dict())
#     db.add(db_os)
#     db.commit()
#     db.refresh(db_os)
#     return db_os

# def update_os(db: Session, os_id: int, updated_os: schemas.OSCreate):
#     db_os = db.query(models.OS).filter(models.OS.os_id == os_id).first()
#     if db_os:
#         for key, value in updated_os.dict().items():
#             setattr(db_os, key, value)
#         db.commit()
#         db.refresh(db_os)
#     return db_os

# def delete_os(db: Session, os_id: int):
#     if db.query(exists().where(models.Server.os_id == os_id)).scalar():
#         raise HTTPException(status_code=400, detail="OS is associated with existing servers. Cannot delete.")
#     db_os = db.query(models.OS).filter(models.OS.os_id == os_id).first()
#     if db_os:
#         db.delete(db_os)
#         db.commit()
#     return db_os


# # ===================== TYPE =====================
# def get_types(db: Session):
#     return db.query(models.Type).all()

# def get_type(db: Session, type_id: int):
#     return db.query(models.Type).filter(models.Type.type_id == type_id).first()

# def create_type(db: Session, type_obj: schemas.TypeCreate):
#     db_type = models.Type(**type_obj.dict())
#     db.add(db_type)
#     db.commit()
#     db.refresh(db_type)
#     return db_type

# def update_type(db: Session, type_id: int, updated_type: schemas.TypeCreate):
#     db_type = db.query(models.Type).filter(models.Type.type_id == type_id).first()
#     if db_type:
#         for key, value in updated_type.dict().items():
#             setattr(db_type, key, value)
#         db.commit()
#         db.refresh(db_type)
#     return db_type

# def delete_type(db: Session, type_id: int):
#     if db.query(exists().where(models.Server.type_id == type_id)).scalar():
#         raise HTTPException(status_code=400, detail="Type is associated with existing servers. Cannot delete.")
#     db_type = db.query(models.Type).filter(models.Type.type_id == type_id).first()
#     if db_type:
#         db.delete(db_type)
#         db.commit()
#     return db_type


# # ===================== CATEGORY =====================
# def get_categories(db: Session):
#     return db.query(models.Category).all()

# def get_category(db: Session, category_id: int):
#     return db.query(models.Category).filter(models.Category.category_id == category_id).first()

# def create_category(db: Session, category: schemas.CategoryCreate):
#     db_category = models.Category(**category.dict())
#     db.add(db_category)
#     db.commit()
#     db.refresh(db_category)
#     return db_category

# def update_category(db: Session, category_id: int, updated_category: schemas.CategoryCreate):
#     db_category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
#     if db_category:
#         for key, value in updated_category.dict().items():
#             setattr(db_category, key, value)
#         db.commit()
#         db.refresh(db_category)
#     return db_category

# def delete_category(db: Session, category_id: int):
#     if db.query(exists().where(models.Server.category_id == category_id)).scalar():
#         raise HTTPException(status_code=400, detail="Category is associated with existing servers. Cannot delete.")
#     db_category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
#     if db_category:
#         db.delete(db_category)
#         db.commit()
#     return db_category


# # ===================== ENVIRONMENT =====================

# def get_environments(db: Session):
#     return db.query(models.Environment).all()

# def get_environment(db: Session, environment_id: int):
#     return db.query(models.Environment).filter(models.Environment.environment_id == environment_id).first()

# def create_environment(db: Session, environment: schemas.EnvironmentCreate):
#     db_env = models.Environment(**environment.dict())
#     db.add(db_env)
#     db.commit()
#     db.refresh(db_env)
#     return db_env

# def update_environment(db: Session, environment_id: int, updated_environment: schemas.EnvironmentCreate):
#     db_env = db.query(models.Environment).filter(models.Environment.environment_id == environment_id).first()
#     if db_env:
#         for key, value in updated_environment.dict().items():
#             setattr(db_env, key, value)
#         db.commit()
#         db.refresh(db_env)
#     return db_env

# def delete_environment(db: Session, environment_id: int):
#     if db.query(exists().where(models.Server.environment_id == environment_id)).scalar():
#         raise HTTPException(status_code=400, detail="Environment is associated with existing servers. Cannot delete.")
#     db_env = db.query(models.Environment).filter(models.Environment.environment_id == environment_id).first()
#     if db_env:
#         db.delete(db_env)
#         db.commit()
#     return db_env






from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import exists
from app import models, schemas
from fastapi import HTTPException

# ===================== SERVER =====================

def get_servers(db: Session):
    return db.query(models.Server).all()

def get_server_by_id(db: Session, server_id: int):
    return db.query(models.Server).filter(models.Server.id == server_id).first()

def create_server(db: Session, server: schemas.ServerCreate):
    db_server = models.Server(**server.dict())
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server

def update_server(db: Session, server_id: int, server: schemas.ServerCreate):
    db_server = get_server_by_id(db, server_id)
    if db_server:
        for key, value in server.dict().items():
            setattr(db_server, key, value)
        db.commit()
        db.refresh(db_server)
    return db_server

def delete_server(db: Session, server_id: int):
    db_server = get_server_by_id(db, server_id)
    if db_server:
        try:
            db.delete(db_server)
            db.commit()
            return db_server
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Cannot delete server: It is referenced by another table.")
    return None

def bulk_create_servers(db: Session, servers: list[schemas.ServerCreate]):
    db_servers = [models.Server(**server.dict()) for server in servers]
    db.add_all(db_servers)
    db.commit()
    return db_servers

def bulk_delete_servers(db: Session, server_ids: list[int]):
    servers_to_delete = db.query(models.Server).filter(models.Server.id.in_(server_ids)).all()
    if len(servers_to_delete) != len(server_ids):
        raise HTTPException(status_code=404, detail="Some server IDs not found")
    try:
        for server in servers_to_delete:
            db.delete(server)
        db.commit()
        return {"deleted_count": len(servers_to_delete)}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Cannot delete some servers due to reference constraints.")


# ===================== LOCATION =====================

def get_locations(db: Session):
    return db.query(models.Location).all()

def get_location(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.location_id == location_id).first()

def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

def update_location(db: Session, location_id: int, updated_location: schemas.LocationCreate):
    db_location = db.query(models.Location).filter(models.Location.location_id == location_id).first()
    if db_location:
        for key, value in updated_location.dict().items():
            setattr(db_location, key, value)
        db.commit()
        db.refresh(db_location)
    return db_location

def delete_location(db: Session, location_id: int):
    if db.query(exists().where(models.Server.location_id == location_id)).scalar():
        raise HTTPException(status_code=400, detail="Location is associated with existing servers. Cannot delete.")
    db_location = db.query(models.Location).filter(models.Location.location_id == location_id).first()
    if db_location:
        db.delete(db_location)
        db.commit()
    return db_location

def bulk_create_locations(db: Session, locations: list[schemas.LocationCreate]):
    db_locations = [models.Location(**loc.dict()) for loc in locations]
    db.add_all(db_locations)
    db.commit()
    return db_locations

def bulk_delete_locations(db: Session, location_ids: list[int]):
    for loc_id in location_ids:
        if db.query(exists().where(models.Server.location_id == loc_id)).scalar():
            raise HTTPException(status_code=400, detail=f"Location ID {loc_id} is associated with servers.")
    locations_to_delete = db.query(models.Location).filter(models.Location.location_id.in_(location_ids)).all()
    for location in locations_to_delete:
        db.delete(location)
    db.commit()
    return {"deleted_count": len(locations_to_delete)}


# ===================== OS =====================

def get_oses(db: Session):
    return db.query(models.OS).all()

def get_os(db: Session, os_id: int):
    return db.query(models.OS).filter(models.OS.os_id == os_id).first()

def create_os(db: Session, os: schemas.OSCreate):
    db_os = models.OS(**os.dict())
    db.add(db_os)
    db.commit()
    db.refresh(db_os)
    return db_os

def update_os(db: Session, os_id: int, updated_os: schemas.OSCreate):
    db_os = db.query(models.OS).filter(models.OS.os_id == os_id).first()
    if db_os:
        for key, value in updated_os.dict().items():
            setattr(db_os, key, value)
        db.commit()
        db.refresh(db_os)
    return db_os

def delete_os(db: Session, os_id: int):
    if db.query(exists().where(models.Server.os_id == os_id)).scalar():
        raise HTTPException(status_code=400, detail="OS is associated with existing servers. Cannot delete.")
    db_os = db.query(models.OS).filter(models.OS.os_id == os_id).first()
    if db_os:
        db.delete(db_os)
        db.commit()
    return db_os

def bulk_create_oses(db: Session, os_list: list[schemas.OSCreate]):
    db_oses = [models.OS(**os.dict()) for os in os_list]
    db.add_all(db_oses)
    db.commit()
    return db_oses

def bulk_delete_oses(db: Session, os_ids: list[int]):
    for os_id in os_ids:
        if db.query(exists().where(models.Server.os_id == os_id)).scalar():
            raise HTTPException(status_code=400, detail=f"OS ID {os_id} is associated with servers.")
    os_to_delete = db.query(models.OS).filter(models.OS.os_id.in_(os_ids)).all()
    for os in os_to_delete:
        db.delete(os)
    db.commit()
    return {"deleted_count": len(os_to_delete)}


# ===================== TYPE =====================

def get_types(db: Session):
    return db.query(models.Type).all()

def get_type(db: Session, type_id: int):
    return db.query(models.Type).filter(models.Type.type_id == type_id).first()

def create_type(db: Session, type_obj: schemas.TypeCreate):
    db_type = models.Type(**type_obj.dict())
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type

def update_type(db: Session, type_id: int, updated_type: schemas.TypeCreate):
    db_type = db.query(models.Type).filter(models.Type.type_id == type_id).first()
    if db_type:
        for key, value in updated_type.dict().items():
            setattr(db_type, key, value)
        db.commit()
        db.refresh(db_type)
    return db_type

def delete_type(db: Session, type_id: int):
    if db.query(exists().where(models.Server.type_id == type_id)).scalar():
        raise HTTPException(status_code=400, detail="Type is associated with existing servers. Cannot delete.")
    db_type = db.query(models.Type).filter(models.Type.type_id == type_id).first()
    if db_type:
        db.delete(db_type)
        db.commit()
    return db_type

def bulk_create_types(db: Session, types: list[schemas.TypeCreate]):
    db_types = [models.Type(**type_obj.dict()) for type_obj in types]
    db.add_all(db_types)
    db.commit()
    return db_types

def bulk_delete_types(db: Session, type_ids: list[int]):
    for type_id in type_ids:
        if db.query(exists().where(models.Server.type_id == type_id)).scalar():
            raise HTTPException(status_code=400, detail=f"Type ID {type_id} is associated with servers.")
    types_to_delete = db.query(models.Type).filter(models.Type.type_id.in_(type_ids)).all()
    for type_obj in types_to_delete:
        db.delete(type_obj)
    db.commit()
    return {"deleted_count": len(types_to_delete)}

# ===================== CATEGORY =====================

def get_categories(db: Session):
    return db.query(models.Category).all()

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.category_id == category_id).first()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, updated_category: schemas.CategoryCreate):
    db_category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
    if db_category:
        for key, value in updated_category.dict().items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    if db.query(exists().where(models.Server.category_id == category_id)).scalar():
        raise HTTPException(status_code=400, detail="Category is associated with existing servers. Cannot delete.")
    db_category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category



def bulk_create_categories(db: Session, categories: list[schemas.CategoryCreate]):
    db_categories = [models.Category(**cat.dict()) for cat in categories]
    db.add_all(db_categories)
    db.commit()
    return db_categories

def bulk_delete_categories(db: Session, category_ids: list[int]):
    for cat_id in category_ids:
        if db.query(exists().where(models.Server.category_id == cat_id)).scalar():
            raise HTTPException(status_code=400, detail=f"Category ID {cat_id} is associated with servers.")
    categories_to_delete = db.query(models.Category).filter(models.Category.category_id.in_(category_ids)).all()
    for cat in categories_to_delete:
        db.delete(cat)
    db.commit()
    return {"deleted_count": len(categories_to_delete)}

# ===================== ENVIRONMENT =====================


def get_environments(db: Session):
    return db.query(models.Environment).all()

def get_environment(db: Session, environment_id: int):
    return db.query(models.Environment).filter(models.Environment.environment_id == environment_id).first()

def create_environment(db: Session, environment: schemas.EnvironmentCreate):
    db_env = models.Environment(**environment.dict())
    db.add(db_env)
    db.commit()
    db.refresh(db_env)
    return db_env

def update_environment(db: Session, environment_id: int, updated_environment: schemas.EnvironmentCreate):
    db_env = db.query(models.Environment).filter(models.Environment.environment_id == environment_id).first()
    if db_env:
        for key, value in updated_environment.dict().items():
            setattr(db_env, key, value)
        db.commit()
        db.refresh(db_env)
    return db_env

def delete_environment(db: Session, environment_id: int):
    if db.query(exists().where(models.Server.environment_id == environment_id)).scalar():
        raise HTTPException(status_code=400, detail="Environment is associated with existing servers. Cannot delete.")
    db_env = db.query(models.Environment).filter(models.Environment.environment_id == environment_id).first()
    if db_env:
        db.delete(db_env)
        db.commit()
    return db_env



def bulk_create_environments(db: Session, environments: list[schemas.EnvironmentCreate]):
    db_envs = [models.Environment(**env.dict()) for env in environments]
    db.add_all(db_envs)
    db.commit()
    return db_envs

def bulk_delete_environments(db: Session, environment_ids: list[int]):
    for env_id in environment_ids:
        if db.query(exists().where(models.Server.environment_id == env_id)).scalar():
            raise HTTPException(status_code=400, detail=f"Environment ID {env_id} is associated with servers.")
    envs_to_delete = db.query(models.Environment).filter(models.Environment.environment_id.in_(environment_ids)).all()
    for env in envs_to_delete:
        db.delete(env)
    db.commit()
    return {"deleted_count": len(envs_to_delete)}



