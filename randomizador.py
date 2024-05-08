# -*- coding: utf-8 -*-

import json
import random
import sys
from time import sleep

class Randomizador:
    def __init__(self, jsonPath):
        self.jsonPath = jsonPath
        self.preguntas = []
        print("Elegido el archivo de preguntas: ", jsonPath)

    def sortear(self) -> int:
        if len(self.preguntas['preguntas']) == 0:
            print("No hay suficientes preguntas para sortear.")
            return -1
        else:
            id_pregunta_aleatoria = random.randint(0, len(self.preguntas['preguntas']) - 1)
            return id_pregunta_aleatoria


    def cargar_preguntas(self) -> None:
        with open(self.jsonPath, encoding='utf-8') as json_file:
            self.preguntas = json.load(json_file)
        print("Preguntas cargadas correctamente")

            
    def mostar_pregunta(self, id_pregunta) -> None:
        print(f"Pregunta: {self.preguntas['preguntas'][id_pregunta]['pregunta']}")
    
    def mostrar_respuesta(self, id_pregunta) -> None:
        print(f"Respuesta: {self.preguntas['preguntas'][id_pregunta]['respuesta']}")
        
    def eliminar_pregunta(self, id_pregunta) -> None:
        self.preguntas['preguntas'].pop(id_pregunta)
        

def limpiar_pantalla():
    print("\033[H\033[J")
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python randomizador.py <archivo_json>")
        sys.exit(1)
    
    print("Bienvenido al randomizador de preguntas")
    
    json_file_path = sys.argv[1]
    
    randomizador = Randomizador(json_file_path)
    randomizador.cargar_preguntas()
    
    print("Presione Ctrl+C para salir del programa")
    
    sleep(2)
    
    limpiar_pantalla()
    
    while True:
        id_pregunta = randomizador.sortear()
        if id_pregunta == -1:
            break
        
        print("\nPresione una tecla para ver la respuesta\n")
        randomizador.mostar_pregunta(id_pregunta)
        input()
        randomizador.mostrar_respuesta(id_pregunta)
        randomizador.eliminar_pregunta(id_pregunta)
        print()

