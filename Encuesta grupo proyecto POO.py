# Juan Alberto Gutiérrez Rodríguez.

# Encuesta para mínimo 10 personas

def main():

    lista_r = ["nombre", "edad", "proyecto", "pregunta1", "pregunta2"]


    class Encuesta:
        def __init__(self, nombre, edad, proyecto, p1, p2):
            self.nombre = nombre
            self.edad = edad
            self.proyecto = proyecto
            self.p1 = p1
            self.p2 = p2        

        
        def agregar_respuesta(self):
            lista_r[0] = encuesta.nombre
            lista_r[1] = encuesta.edad
            lista_r[2] = encuesta.proyecto
            lista_r[3] = encuesta.p1
            lista_r[4] = encuesta.p2
            print ("Respuestas guardadas exitosamente")


        def mostrar_resultados(self):
            print(f"Datos ingresados: {lista_r}")


    for i in range (10):

        encuesta = Encuesta(input("Nombre: "), input("Edad: "), input("Cuál es su idea de proyecto: "), input("¿Hace cuánto sabe usar Python?: "), input("¿Tiene tiempo disponible para trabajar en grupo?: "))

        encuesta.agregar_respuesta()

        encuesta.mostrar_resultados()


if __name__ == '__main__':
    main()