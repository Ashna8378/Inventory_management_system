from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, index=True)
    server_name = Column(String(255), nullable=False)
    server_cpu = Column(Integer)
    server_memory_in_gb = Column(Integer)
    location_id = Column(Integer, nullable=False)
    os_id = Column(Integer, nullable=False)
    type_id = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False)
    environment_id = Column(Integer)
    peak_memory_usage = Column(Text)
    peak_cpu_usage = Column(Text)


class Location(Base):
    __tablename__ = "location"

    location_id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String(255), nullable=False)
    location_city = Column(String(100), nullable=False)



class OS(Base):
    __tablename__ = "os"

    os_id = Column(Integer, primary_key=True, index=True)
    os_name = Column(String(255), nullable=False)
    os_version = Column(String(100), nullable=False)

    

class Type(Base):
    __tablename__ = "type"

    type_id = Column(Integer, primary_key=True, index=True)
    type_name = Column(String(255), nullable=False)



class Category(Base):
    __tablename__ = "category"

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(255), nullable=False)


class Environment(Base):
    __tablename__ = "environment"

    environment_id = Column(Integer, primary_key=True, index=True)
    environment_name = Column(String(255), nullable=False)




# from sqlalchemy import Column, Integer, String, Text, ForeignKey
# from app.database import Base

# class Server(Base):
#     __tablename__ = "servers"

#     id = Column(Integer, primary_key=True, index=True)
#     server_name = Column(String(255), nullable=False)
#     server_cpu = Column(Integer)
#     server_memory_in_gb = Column(Integer)
#     location_id = Column(Integer, ForeignKey("location.location_id"), nullable=False)
#     os_id = Column(Integer, ForeignKey("os.os_id"), nullable=False)
#     type_id = Column(Integer, ForeignKey("type.type_id"), nullable=False)
#     category_id = Column(Integer, ForeignKey("category.category_id"), nullable=False)
#     environment_id = Column(Integer, ForeignKey("environment.environment_id"))
#     peak_memory_usage = Column(Text)
#     peak_cpu_usage = Column(Text)