from pydantic import BaseModel

class ServerBase(BaseModel):
    server_name: str
    server_cpu: int | None = None
    server_memory_in_gb: int | None = None
    location_id: int
    os_id: int
    type_id: int
    category_id: int
    environment_id: int | None = None
    peak_memory_usage: str | None = None
    peak_cpu_usage: str | None = None

class ServerCreate(ServerBase):
    pass

class Server(ServerBase):
    id: int

    class Config:
        from_attributes = True



class LocationBase(BaseModel):
    location_name: str
    location_city: str

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    location_id: int

    class Config:
        from_attributes = True  # for Pydantic v2




class OSBase(BaseModel):
    os_name: str
    os_version: str

class OSCreate(OSBase):
    pass

class OS(OSBase):
    os_id: int

    class Config:
        from_attributes = True



class TypeBase(BaseModel):
    type_name: str

class TypeCreate(TypeBase):
    pass

class Type(TypeBase):
    type_id: int

    class Config:
        from_attributes = True



class CategoryBase(BaseModel):
    category_name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    category_id: int

    class Config:
        from_attributes = True





class EnvironmentBase(BaseModel):
    environment_name: str

class EnvironmentCreate(EnvironmentBase):
    pass

class Environment(EnvironmentBase):
    environment_id: int

    class Config:
        from_attributes = True




