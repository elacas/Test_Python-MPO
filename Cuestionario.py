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
