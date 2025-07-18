'''
import json (para que el python "lea y convierta el archivo json)
import random (importar la funcion para randomizar preguntas")

'''
import json
import random

'''
Definir cargar peguntas con (with) abrir el json, R read/lectura, "diccionario" utf8 (tiene en cuenta los simbolos como la ñ), se abre como/as archivo (devuelve el json leido como archivo)
'''
def cargar_preguntas():
   with open ("preguntas.json", "r", encoding="utf-8") as archivo:
      return json.load(archivo)

'''
Definir asignaturas diferentes: print= se muestran las variables disponibles, con input se le dice a la persona que escoja asignatura/dificultad o volver al menu. If: si se cumple algo -> haz esto
                                              Elif: sino se cumple lo anterior haz esto
                                              Else: si todo lo demás falla haz esto'''     
def elegir_asignatura():

   print("\nEscoge asignatura")
   print("\n1-Lenguaje de Marcas")
   print("\n2-Fundamentos del Hardware")
   print("\n3-MPO-Python")
   print("\n4-Bases de Datos")
   print("\n5-Itinerario para la Empleabilidad")
   print("\n6-Implantación Sistemas Operativos")
   print("\n7-Planificacion y Administración de Redes")
  
   opcion = input("Escoja asignatura")
   while True:    
     if opcion == "1":
         return "Lenguaje_de_Marcas"
     elif opcion == "2":
         return "Fundamentos_del_Hardware"
     elif opcion == "3":
         return "MOP_Python"
     elif opcion == "4":
         return "Bases_Datos"
     elif opcion == "5":
         return "Itinerario_empleabilidad"
     elif opcion == "6":
         return "Implantacion_Sistemas"
     elif opcion == "7":
         return "Planificacion_de_Redes"
     elif opcion == "8":
         return "main"
     else:
       print("Porfavor, introduzca un umero válido")
       return elegir_asignatura()
     
def elegir_dificultad():
   while True:
      opcion = input("Escoja dificultad")
      if opcion == "1":
         return "Basico"
      elif opcion == "2":
         return "Intermedio"
      elif opcion == "3":
         return "Avanzado"
      elif opcion == "4":
         return elegir_asignatura
      else:
         print("Seleccione una opción válida")
'''
variable datos para acceder a las preguntas
variable asignatura/dificultad para llamar a las funciones anteriores 
'''
'''
variable preguntas esta formada por la variable "datos" que seria el documento json "pasado"a Python, dentro del cual se busca la asignatura y el nivel elegido por el usuario.
Random.shuffle funcion para randomizar preguntas
'''
def hacer_cuestionario():
   
     datos=cargar_preguntas

     asignatura=elegir_asignatura
   
     dificultad=elegir_dificultad

     preguntas=datos[asignatura][dificultad]

     random.shuffle[preguntas]

     preguntas_test=preguntas[:15]



def main():
    print("="*25,"TEST ASIR", "="*25)
    print()
    while True:
         print("1-Empezar cuestionario\n")
         print("2-Ranking\n")
         print("3-Salir\n")
         print("="*59)

         opcion = input("Elige")

         if opcion == "1":
            print("Escoge asignatura\n")
         elif opcion == "2":
            print("Aquí irá el ránking\n")
         elif opcion == "3":
            print("¡Hasta luego!")
            break
         else:
          print("Opción incorrecta, porfavor introduzca 1,2 o 3")
    
if __name__ == "__main__":
    main()
