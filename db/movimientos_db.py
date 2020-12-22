from typing import Dict
from pydantic import BaseModel
import datetime

class Movimiento(BaseModel):
    id: int
    fecha: datetime.date
    valor: int
    categoria: str
    descripcion: str
    tipo: str
    usuario: str

#Diccionario
database_movs = Dict[int, Movimiento]

database_movs = {
    1: Movimiento(**{"id":1,
                    "fecha": '2020-12-01',
                    "valor": 50000,
                    "categoria": "Alimentos",
                    "descripcion": "Almuerzo en Leños Steak",
                    "tipo": "Gasto",
		            "usuario": "heidy"	
                    }),

    2: Movimiento(**{"id":2,
                    "fecha": '2020-12-04',
                    "valor": 20000,
                    "categoria": "Transporte",
                    "descripcion": "Taxi al trabajo",
                    "tipo": "Gasto",
                    "usuario": "heidy"
                    }),

    3: Movimiento(**{"id":3,
                    "fecha": '2020-12-01',
                    "valor": 30000,
                    "categoria": "Alimentos",
                    "descripcion": "Hamburguesa",
                    "tipo": "Gasto",
                    "usuario": "sofi"
                    }),

    4: Movimiento(**{"id":4,
                    "fecha": '2020-12-05',
                    "valor": 1000000,
                    "categoria": "Salario",
                    "descripcion": "Quincena",
                    "tipo": "Ingreso",
                    "usuario": "julian"
                    }),

    5: Movimiento(**{"id":5,
                    "fecha": '2020-12-11',
                    "valor": 100000,
                    "categoria": "Facturas",
                    "descripcion": "Servicios públicos",
                    "tipo": "Gasto",
                    "usuario": "carlos"
                    }),     

    6: Movimiento(**{"id":6,
                    "fecha": '2020-12-06',
                    "valor": 35000,
                    "categoria": "Alimentos",
                    "descripcion": "Pizza y gaseosa",
                    "tipo": "Gasto",
		            "usuario": "julian"	
                    }),

    7: Movimiento(**{"id":7,
                    "fecha": '2020-12-04',
                    "valor": 50000,
                    "categoria": "Facturas",
                    "descripcion": "Plan de celular",
                    "tipo": "Gasto",
                    "usuario": "heidy"
                    }),

    8: Movimiento(**{"id":8,
                    "fecha": '2020-12-01',
                    "valor": 300000,
                    "categoria": "Honorarios",
                    "descripcion": "Asesorías",
                    "tipo": "Ingreso",
                    "usuario": "sofi"
                    }),

    9: Movimiento(**{"id":9,
                    "fecha": '2020-12-15',
                    "valor": 1500000,
                    "categoria": "Salario",
                    "descripcion": "Quincena",
                    "tipo": "Ingreso",
                    "usuario": "julian"
                    }),

    10: Movimiento(**{"id":10,
                    "fecha": '2020-12-08',
                    "valor": 6000,
                    "categoria": "Alimentos",
                    "descripcion": "Desayuno",
                    "tipo": "Gasto",
                    "usuario": "carlos"
                    }),  

    11: Movimiento(**{"id":11,
                    "fecha": '2020-12-01',
                    "valor": 45000,
                    "categoria": "Alimentos",
                    "descripcion": "Almuerzo en McDonalds",
                    "tipo": "Gasto",
		            "usuario": "mao"	
                    }),

    12: Movimiento(**{"id":12,
                    "fecha": '2020-12-04',
                    "valor": 40000,
                    "categoria": "Transporte",
                    "descripcion": "Taxis",
                    "tipo": "Gasto",
                    "usuario": "carlos"
                    }),

    13: Movimiento(**{"id":13,
                    "fecha": '2020-12-15',
                    "valor": 20000,
                    "categoria": "Salario",
                    "descripcion": "Quincena",
                    "tipo": "Ingreso",
                    "usuario": "julian"
                    }),

    14: Movimiento(**{"id":14,
                    "fecha": '2020-12-02',
                    "valor": 1000000,
                    "categoria": "Arriendo",
                    "descripcion": "Arrendamiento diciembre",
                    "tipo": "Gasto",
                    "usuario": "sofi"
                    }),

    15: Movimiento(**{"id":15,
                    "fecha": '2020-12-02',
                    "valor": 300000,
                    "categoria": "Mercado",
                    "descripcion": "Compras varias",
                    "tipo": "Gasto",
                    "usuario": "mao"
                    }),                      
}


def filtrar_por_fecha(dia_inicio: datetime.date, dia_fin: datetime.date):
    lista_movs = []
    for m in database_movs:
        if database_movs[m].fecha >= dia_inicio and database_movs[m].fecha <= dia_fin:
            lista_movs.append(database_movs[m])  
    return lista_movs


def filtrar_por_categoria (cat: str):
    lista_movs = []
    for m in database_movs:
        if database_movs[m].categoria == cat:
            lista_movs.append(database_movs[m])  
    return lista_movs


def filtrar_por_usuario (usu: str):
    lista_movs = []
    for m in database_movs:
        if database_movs[m].usuario == usu:
            lista_movs.append(database_movs[m])  
    return lista_movs


def crear_movimiento(movimiento: Movimiento):
    if movimiento.id in database_movs:
        return False
    else:
        database_movs[movimiento.id] = movimiento
        return True

def generar_id():
    nuevo_id = 1
    for m in database_movs:
        if nuevo_id <= m:
            nuevo_id = m
    nuevo_id += 1
    return nuevo_id

def consulta_movs():
    lista_movs = []
    for m in database_movs:
        lista_movs.append(database_movs[m])  
    return lista_movs

def ordenar_por_fecha(lista_movs):
    lista_ordenada = lista_movs.copy()
    if len(lista_ordenada) == 1:
        return lista_ordenada
    else:
        for m in range(1,len(lista_ordenada)):
            if lista_ordenada[0].fecha > lista_ordenada[m].fecha:
                t = lista_ordenada[m]
                lista_ordenada[m] = lista_ordenada[0]
                lista_ordenada[0] = t
        lista_ordenada[1:len(lista_ordenada)] = ordenar_por_fecha(lista_ordenada[1:len(lista_ordenada)]).copy()           
        return lista_ordenada
