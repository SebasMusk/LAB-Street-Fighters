from typing import NamedTuple, List, Optional,Tuple,Set
from datetime import datetime
from collections import defaultdict , Counter
import csv

 


Partida = NamedTuple("Partida", [
    ("pj1", str),
    ("pj2", str),
    ("puntuacion", int),
    ("tiempo", float),
    ("fecha_hora", datetime),
    ("golpes_pj1", List[str]),
    ("golpes_pj2", List[str]),
    ("movimiento_final", str),
    ("combo_finish", bool),
    ("ganador", str),
    ])


def parsea_bool(cadena:str)->Optional[bool]:
    res = None
    if cadena == "1":
        return True
    elif cadena == "0":
        return False
    return res

def parsea_list(cadena:str)->List[str]:
    return cadena.strip("][").replace("'", "").split(', ')



def lee_partidas(ruta_fichero:str)->List[Partida]:
    res = []
    with open(ruta_fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter= ",")
        next(lector)
        for pj1,pj2,puntuacion,tiempo,fecha_hora,golpes_pj1,golpes_pj2,movimiento_final,combo_finish,ganador in lector:
            puntuacion = int(puntuacion)
            tiempo = float(tiempo)
            fecha_hora = datetime.strptime(fecha_hora,"%Y-%m-%d %H:%M:%S")  
            golpes_pj1 = parsea_list(golpes_pj1)          
            golpes_pj2 = parsea_list(golpes_pj2) 
            combo_finish = parsea_bool(combo_finish)
            res.append(Partida(pj1,pj2,puntuacion,tiempo,fecha_hora,golpes_pj1,golpes_pj2,movimiento_final,combo_finish,ganador))
    return res

def victora_mas_rapida(Game:List[Partida])->Tuple[str,str,float]:
    tiempo_mas_rapido = float('inf')
    personajes_mas_rapidos = None
    for Juego in Game:
        if Juego.tiempo < tiempo_mas_rapido:
            personajes_mas_rapidos = Juego.pj1 , Juego.pj2
            tiempo_mas_rapido = Juego.tiempo
    return personajes_mas_rapidos, tiempo_mas_rapido
        
            
def top_ratio_medio_personajes(Game:List[Partida], n : int)->List[str]:
    puntuaciones_tiempo_por_personaje = {}
    for Juego in Game:
        ganador = Juego.ganador
        puntuacion = Juego.puntuacion
        tiempo = Juego.tiempo
        
        puntuaciones_tiempo_por_personaje[ganador] = {"puntuaciones": [puntuacion], "tiempos": [tiempo]}

    ratios_medias_por_personaje = {}
    for personaje, datos in puntuaciones_tiempo_por_personaje.items():
        puntuaciones = datos["puntuaciones"]
        tiempos = datos["tiempos"]
        ratio_media = sum(puntuacion / tiempo for puntuacion, tiempo in zip(puntuaciones, tiempos)) / len(puntuaciones)
        ratios_medias_por_personaje[personaje] = ratio_media

    personajes_ordenados = sorted(ratios_medias_por_personaje.keys(), key=lambda x: ratios_medias_por_personaje[x])
    top_n_personajes = personajes_ordenados[:n]
    
    return top_n_personajes
    
def enemigos_mas_debiles(Game:List[Partida], personaje: str)->Tuple[List[str],int]:
    recuento_victorias = {}
    for Juego in Game:
        if personaje in [Juego.pj1, Juego.pj2]:
            oponente = Juego.pj1 if Juego.pj2 == personaje else Juego.pj2
            if Juego.ganador == personaje:
                recuento_victorias[oponente] = recuento_victorias.get(oponente,0) +1
    
    max_victorias = max(recuento_victorias.values())
    oponentes_max_victorias = [oponente for oponente, vicotorias in recuento_victorias.items() if vicotorias == max_victorias]
    res = (oponentes_max_victorias, max_victorias)
    return res
    
def movimientos_comunes(Game:List[Partida], personaje1:str, personaje2: str)->List[str]:
    movimientos_por_personaje = {}
    for Juego in Game:
        if personaje1 == Juego.pj1 and personaje2== Juego.pj2:
            movimientos_por_personaje[Juego.pj1] = Juego.golpes_pj1
            movimientos_por_personaje[Juego.pj2] = Juego.golpes_pj2
        if personaje1 == Juego.pj2 and personaje2== Juego.pj1:
            movimientos_por_personaje[Juego.pj1] = Juego.golpes_pj1
            movimientos_por_personaje[Juego.pj2] = Juego.golpes_pj2
        
    res = [movimientos_por_personaje[personaje1],movimientos_por_personaje[personaje2]]
    resultado = []
    for movimientos in res[0]:
        if movimientos in res[1]:
            resultado.append(movimientos)
    return resultado
    
        
        
def parsea_dia_semana(numero:int)->str:
    if numero == 0:
        return "Lunes"
    elif numero == 1:
        return "Martes"
    elif numero == 2:
        return "Miercoles"
    elif numero == 3:
        return "Jueves"
    elif numero == 4:
        return "Viernes"
    elif numero == 5:
        return "Sabado"
    elif numero == 6:
        return "Domingo"

def dia_mas_combo_finish(Game:List[Partida])->str:
    res = defaultdict(int)
    for Juego in Game:
        dia = Juego.fecha_hora.weekday()
        res[dia] += Juego.combo_finish
    
    
    list1 =  sorted(res.items(),key=lambda x:x[1], reverse= True)
    
    
    for dia, victorias in list1:
        numero = list1[0][0]
    return parsea_dia_semana(numero)
        

    
        
    
    


    
    
    
    
    
    

    
    
     
    
    
           
    
        







    




