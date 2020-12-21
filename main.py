from fastapi import FastAPI, Depends, HTTPException

from routers.usuario_router     import router as router_usuario  
from routers.movimientos_router import router as router_movimiento

import datetime
import db.movimientos_db
import db.usuario_db
from db.movimientos_db import database_movs
from db.usuario_db import database_usuario

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
"http://localhost", 
"http://localhost:8080",
"https://piggy-grow-frontend.herokuapp.com/",
]
app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True, 
allow_methods=["*"], 
allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Bienvenido a Piggy Grow"}
