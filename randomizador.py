import json
import random
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
        with open(self.jsonPath) as json_file:
            self.preguntas = json.load(json_file)
        print("Preguntas cargadas:", self.preguntas)

            
    def mostar_pregunta(self, id_pregunta) -> None:
        print(f"Pregunta: {self.preguntas['preguntas'][id_pregunta]['pregunta']}")
    
    def mostrar_respuesta(self, id_pregunta) -> None:
        print(f"Respuesta: {self.preguntas['preguntas'][id_pregunta]['respuesta']}")

def limpiar_pantalla():
    print("\033[H\033[J")
    
if __name__ == "__main__":
    print("Bienvenido al randomizador de preguntas")
    
    randomizador = Randomizador("preguntasRCR.json")
    randomizador.cargar_preguntas()
    
    print("Presione Ctrl+C para salir del programa")
    
    sleep(2)
    
    limpiar_pantalla()
    
    while True:
        id_pregunta = randomizador.sortear()
        if id_pregunta == -1:
            break
        randomizador.mostar_pregunta(id_pregunta)
        input("Presione una tecla para ver la respuesta")
        randomizador.mostrar_respuesta(id_pregunta)
        print()

