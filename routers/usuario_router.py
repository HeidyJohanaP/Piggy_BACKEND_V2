from fastapi import Depends, APIRouter, HTTPException
import datetime
import db.movimientos_db
import db.usuario_db
from db.movimientos_db import database_movs
from db.usuario_db import database_usuario
from models.usuario_models import UserIn

router = APIRouter()

#Peticiones para la entidad Usuario
@router.get("/usuario/{user}")
async def detalles_de_usuario(user: str):
    if user in database_usuario:
        return database_usuario[user]    
    raise HTTPException(status_code = 404, detail = "Username incorrecto")


@router.post("/usuario/autenticar")
async def autenticacion_de_usuario(user_in: UserIn):
    if user_in.username in database_usuario:
        user_in_db = database_usuario[user_in.username]
        

        if user_in_db != None:        
            if user_in.password == (database_usuario[user_in.username].contrasena):
                return user_in_db.username
            raise HTTPException(status_code = 404, detail = "Contraseña incorrecta")
    raise HTTPException(status_code = 404, detail = "Usuario no registrado")
    

