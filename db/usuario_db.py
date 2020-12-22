from typing import Dict
from pydantic import BaseModel
import datetime

class Usuario(BaseModel):
    username: str
    nombre: str
    apellido: str
    email: str
    telefono: int
    contrasena: str

database_usuario = {  
    "heidy": Usuario(username="heidy",
                    nombre="Heidy Johana",
                    apellido="Parada Gómez",
                    email="hjparada@gmail.com",
                    telefono=3135264710,
                    contrasena = "heidy123"),

    "sofi": Usuario(username="sofi",
                    nombre="Sofi Yanina",
                    apellido="Chilatra Tapiero",
                    email="sychilatra@gmail.com",
                    telefono=3012501431,
                    contrasena = "sofi123"),

    "julian": Usuario(username="julian",
                    nombre="Julián David",
                    apellido="Rojas Delgado",
                    email="jdrojas@gmail.com",
                    telefono=3104785511,
                    contrasena = "julian123"),

    "carlos": Usuario(username="carlos",
                    nombre="Carlos Alexander",
                    apellido="Castillo Salamanca",
                    email="cacastillo@gmail.com",
                    telefono=3005114636,
                    contrasena = "carlos123"),
                    
    "mao": Usuario(username="mao",
                    nombre="Mauricio",
                    apellido="Pineda Angel",
                    email="mpineda@gmail.com",
                    telefono=3042160804,
                    contrasena = "mao123")                
}
