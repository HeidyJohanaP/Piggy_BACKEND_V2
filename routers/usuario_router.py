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
        #return user_in_db

        if user_in_db != None:        
            if user_in.password == (database_usuario[user_in.username].contrasena):
                return user_in_db.username
            raise HTTPException(status_code = 404, detail = "Contraseña incorrecta")
    raise HTTPException(status_code = 404, detail = "Usuario no registrado")
    
    
   


"""  if db.usuario_db.get_username(user) in database_usuario:
        if db.usuario_db.get_contrasena(user) in database_usuario[str(db.usuario_db.get_username(user)) ]:
            return True
        raise HTTPException(status_code = 404, detail = "Contraseña incorrecta")
    raise HTTPException(status_code = 404, detail = "Usuario incorrecta")"""

"""async def auth_user(user_in: UserIn, db: Session = Depends(get_db)):
    
    user_in_db = db.query(UserInDB).get(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=403, detail="Error de autenticacion")

    return  {"Autenticado": True}"""

"""@router.post("/mov/nuevo")
async def crear_movimiento(movimiento: db.movimientos_db.Movimiento):
    new_id = db.movimientos_db.generar_id()
    movimiento.id = new_id
    orden_creada = db.movimientos_db.crear_movimiento(movimiento)
    if orden_creada:
        return {"message" : "Movimiento creado exitosamente."}
    else:
        raise HTTPException(status_code=400, detail="Ya existe un movimiento con el ID especificado.")

"""

