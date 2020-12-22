from fastapi import Depends, APIRouter, HTTPException
import datetime
import db.movimientos_db
import db.usuario_db
from db.movimientos_db import database_movs
from db.usuario_db import database_usuario

router = APIRouter()

#Peticiones para la entidad Movimiento
@router.get("/mov")
async def movimientos():
    return db.movimientos_db.consulta_movs()

@router.get("/mov/ord")
async def mov_ordenar():
    return db.movimientos_db.ordenar_por_fecha(db.movimientos_db.consulta_movs())    

@router.get("/mov/{id}")
async def movimientos_por_id(id: int):
    if id in database_movs:
        return database_movs[id]    
    raise HTTPException(status_code = 404, detail = "No se registra el movimiento.")

#http://127.0.0.1:8000/usuario_mov?user=heidy
@router.get("/usuario_mov")
async def movimientos_por_usuario(user: str):
    return db.movimientos_db.ordenar_por_fecha(db.movimientos_db.filtrar_por_usuario(user))

#http://127.0.0.1:8000/categoria?categoria=Alimentos
@router.get("/categoria")
async def movimientos_por_categoria(categoria: str):
    return db.movimientos_db.filtrar_por_categoria(categoria)   

#http://127.0.0.1:8000/fecha?dia_inicio=2020-12-01&dia_fin=2020-12-01
@router.get("/fecha")
async def movimientos_por_dia(dia_inicio: datetime.date, dia_fin: datetime.date):
    mi_lista = db.movimientos_db.filtrar_por_fecha(dia_inicio, dia_fin)
    return db.movimientos_db.ordenar_por_fecha(mi_lista)


@router.post("/mov")
async def crear_movimiento(movimiento: db.movimientos_db.Movimiento):
    new_id = db.movimientos_db.generar_id()
    movimiento.id = new_id
    orden_creada = db.movimientos_db.crear_movimiento(movimiento)
    if orden_creada:
        return {"message" : "Movimiento creado exitosamente, id = " + str(movimiento.id)}
    else:
        raise HTTPException(status_code=400, detail="Ya existe un movimiento con el ID especificado.")


