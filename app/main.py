from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud

# from app import models, schemas

from app.database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/servers", response_model=list[schemas.Server])
def read_servers(db: Session = Depends(get_db)):
    return crud.get_servers(db)

@app.get("/servers/{server_id}", response_model=schemas.Server)
def read_server(server_id: int, db: Session = Depends(get_db)):
    server = crud.get_server_by_id(db, server_id)
    if server is None:
        raise HTTPException(status_code=404, detail="Server not found")
    return server

@app.post("/servers", response_model=schemas.Server)
def create_server(server: schemas.ServerCreate, db: Session = Depends(get_db)):
    return crud.create_server(db, server)

@app.put("/servers/{server_id}", response_model=schemas.Server)
def update_server(server_id: int, updated: schemas.ServerCreate, db: Session = Depends(get_db)):
    server = crud.update_server(db, server_id, updated)
    if server is None:
        raise HTTPException(status_code=404, detail="Server not found")
    return server

@app.delete("/servers/{server_id}")
def delete_server(server_id: int, db: Session = Depends(get_db)):
    server = crud.delete_server(db, server_id)
    if server is None:
        raise HTTPException(status_code=404, detail="Server not found")
    return { "message": "Server deleted successfully" }


########################################################################################################################################
########################################################################################################################################


@app.get("/locations", response_model=list[schemas.Location])
def read_locations(db: Session = Depends(get_db)):
    return crud.get_locations(db)

@app.get("/locations/{location_id}", response_model=schemas.Location)
def read_location(location_id: int, db: Session = Depends(get_db)):
    return crud.get_location(db, location_id)

@app.post("/locations", response_model=schemas.Location)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.create_location(db, location)

@app.put("/locations/{location_id}", response_model=schemas.Location)
def update_location(location_id: int, updated_location: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.update_location(db, location_id, updated_location)

@app.delete("/locations/{location_id}")
def delete_location(location_id: int, db: Session = Depends(get_db)):
    return crud.delete_location(db, location_id)


#############################################################################################################################################
##########################################################################################################################################

@app.get("/os", response_model=list[schemas.OS])
def read_oses(db: Session = Depends(get_db)):
    return crud.get_oses(db)

@app.get("/os/{os_id}", response_model=schemas.OS)
def read_os(os_id: int, db: Session = Depends(get_db)):
    return crud.get_os(db, os_id)

@app.post("/os", response_model=schemas.OS)
def create_os(os: schemas.OSCreate, db: Session = Depends(get_db)):
    return crud.create_os(db, os)

@app.put("/os/{os_id}", response_model=schemas.OS)
def update_os(os_id: int, updated_os: schemas.OSCreate, db: Session = Depends(get_db)):
    return crud.update_os(db, os_id, updated_os)

@app.delete("/os/{os_id}")
def delete_os(os_id: int, db: Session = Depends(get_db)):
    return crud.delete_os(db, os_id)


############################################################################################################################################3333
###########################################################################################################################################3


@app.get("/types", response_model=list[schemas.Type])
def read_types(db: Session = Depends(get_db)):
    return crud.get_types(db)

@app.get("/types/{type_id}", response_model=schemas.Type)
def read_type(type_id: int, db: Session = Depends(get_db)):
    return crud.get_type(db, type_id)

@app.post("/types", response_model=schemas.Type)
def create_type(type_obj: schemas.TypeCreate, db: Session = Depends(get_db)):
    return crud.create_type(db, type_obj)

@app.put("/types/{type_id}", response_model=schemas.Type)
def update_type(type_id: int, updated_type: schemas.TypeCreate, db: Session = Depends(get_db)):
    return crud.update_type(db, type_id, updated_type)

@app.delete("/types/{type_id}")
def delete_type(type_id: int, db: Session = Depends(get_db)):
    return crud.delete_type(db, type_id)

############################################################################################################################################33
###########################################################################################################################################

@app.get("/categories", response_model=list[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@app.get("/categories/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    return crud.get_category(db, category_id)

@app.post("/categories", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@app.put("/categories/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, updated_category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.update_category(db, category_id, updated_category)

@app.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return crud.delete_category(db, category_id)

##############################################################################################################################################333
##################################################################################################################################################3

@app.get("/environments", response_model=list[schemas.Environment])
def read_environments(db: Session = Depends(get_db)):
    return crud.get_environments(db)

@app.get("/environments/{environment_id}", response_model=schemas.Environment)
def read_environment(environment_id: int, db: Session = Depends(get_db)):
    return crud.get_environment(db, environment_id)

@app.post("/environments", response_model=schemas.Environment)
def create_environment(environment: schemas.EnvironmentCreate, db: Session = Depends(get_db)):
    return crud.create_environment(db, environment)

@app.put("/environments/{environment_id}", response_model=schemas.Environment)
def update_environment(environment_id: int, updated_environment: schemas.EnvironmentCreate, db: Session = Depends(get_db)):
    return crud.update_environment(db, environment_id, updated_environment)

@app.delete("/environments/{environment_id}")
def delete_environment(environment_id: int, db: Session = Depends(get_db)):
    return crud.delete_environment(db, environment_id)

# ===================== BULK ROUTES =====================

@app.post("/servers/bulk")
def bulk_create_servers(servers: list[schemas.ServerCreate], db: Session = Depends(get_db)):
    return crud.bulk_create_servers(db, servers)

@app.delete("/servers/bulk")
def bulk_delete_servers(server_ids: list[int], db: Session = Depends(get_db)):
    return crud.bulk_delete_servers(db, server_ids)


@app.post("/locations/bulk")
def bulk_create_locations(locations: list[schemas.LocationCreate], db: Session = Depends(get_db)):
    return crud.bulk_create_locations(db, locations)

@app.delete("/locations/bulk")
def bulk_delete_locations(location_ids: list[int], db: Session = Depends(get_db)):
    return crud.bulk_delete_locations(db, location_ids)


@app.post("/os/bulk")
def bulk_create_oses(os_list: list[schemas.OSCreate], db: Session = Depends(get_db)):
    return crud.bulk_create_oses(db, os_list)

@app.delete("/os/bulk")
def bulk_delete_oses(os_ids: list[int], db: Session = Depends(get_db)):
    return crud.bulk_delete_oses(db, os_ids)


@app.post("/types/bulk")
def bulk_create_types(types: list[schemas.TypeCreate], db: Session = Depends(get_db)):
    return crud.bulk_create_types(db, types)

@app.delete("/types/bulk")
def bulk_delete_types(type_ids: list[int], db: Session = Depends(get_db)):
    return crud.bulk_delete_types(db, type_ids)


@app.post("/categories/bulk")
def bulk_create_categories(categories: list[schemas.CategoryCreate], db: Session = Depends(get_db)):
    return crud.bulk_create_categories(db, categories)

@app.delete("/categories/bulk")
def bulk_delete_categories(category_ids: list[int], db: Session = Depends(get_db)):
    return crud.bulk_delete_categories(db, category_ids)


@app.post("/environments/bulk")
def bulk_create_environments(environments: list[schemas.EnvironmentCreate], db: Session = Depends(get_db)):
    return crud.bulk_create_environments(db, environments)

@app.delete("/environments/bulk")
def bulk_delete_environments(environment_ids: list[int], db: Session = Depends(get_db)):
    return crud.bulk_delete_environments(db, environment_ids)





