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
