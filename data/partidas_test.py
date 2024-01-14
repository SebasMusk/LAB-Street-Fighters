from partidas import *

def test_lee_partidas(datos):
    print("#######################################")
    print("1. Test de lee_peliculas:")
    print(f'Total registros leídos:{len(datos)}')
    print("Mostrando los tres primeros registros:")
    print(datos[:3])
    print("#######################################")

def test_victora_mas_rapida(datos):
    print("2. Test victora_mas_rapida")
    print(f'La partida más rápida fue una entre {victora_mas_rapida(datos)[0][0]} y {victora_mas_rapida(datos)[0][1]} que duró {victora_mas_rapida(datos)[1]} segundos')
    print("#######################################")
    
def test_top_ratio_medio_personajes(datos):
    print("3. Test de top_ratio_medio_personajes")
    print(f'el top 3 de ratios medios es {top_ratio_medio_personajes(datos, n=3)}')
    print("#######################################")

def test_enemigos_mas_debiles(datos):
    print("4. Test de enemigo_mas_debil")
    print(f'Los enemigos mas debiles de Ken son : {enemigos_mas_debiles(datos, personaje= "Ken")}')
    print("#######################################")
    
def test_movimientos_comunes(datos):
    print("5. Test de movimientos_comunes")
    print(f'Los movimientos repetidos entre Ryu y Ken son:{movimientos_comunes(datos, personaje1="Ryu" , personaje2= "Ken")}')
    print("#######################################")
    

def test_dia_mas_combo_finish(datos):
    print("6. Test de dia_mas_combo_finish")
    print(f' El día que más Ultra Combo Finish ha habido es el {dia_mas_combo_finish(datos)}')
    print("#######################################")























if __name__ == '__main__':
    datos = lee_partidas('data/games.csv')
    test_lee_partidas(datos)
    test_victora_mas_rapida(datos)
    test_top_ratio_medio_personajes(datos)
    test_enemigos_mas_debiles(datos)
    test_movimientos_comunes(datos)
    test_dia_mas_combo_finish(datos)