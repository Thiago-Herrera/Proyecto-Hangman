# **Proyecto-Hangman**
## **LOGICA DEL JUEGO:**
   1. iniciar juego.
   2. Menu de opciones:
      1. Jugar. (INICIAR JUEGO DEL AHORCADO)
      2. Salir. (SALIR DEL JUEGO)
   3. Reglas:
      1. Tienes de 2 a 6 vidas para adivinar la palabra.(Dependiendo la dificultad)
      2. Si adivinas una letra se añadera.
      3. Si no adivinas una letra, se te restará un intento.
      4. Si adivinas la palabra, ¡ganas!
      5. Si te quedas sin intentos, pierdes
   4. Preguntar Dificultad. (Facil (6 vidas), Normal (4 vidas), Dificil (2 Vidas))
   5. Preguntar Nombre del jugador.
   6. Preguntar Nombre del ahorcado.
   7. Elegir Palabra Secreta.
   8. Inciar ciclo de juego:  (Hasta que acaben las vidas o se adivine la palabra)
      1. Revisar vidas
      2. Colocar dibujo del ahorcado.
      3. Colocar Espacios en blanco.
      4. Preguntar Letra.
      5. Definir si es correcta, incorrecta o si esta usada.
      6. Si es correcta:
         1. escribir "¡Letra correcta =)!"
         2. ecribir la letra en el lugar de los espacios que corresponde
         3. repetir ciclo
      7. si es incorrecta:
         1. escribir "Letra incorrecta =("
         2. -1 vidas
         3. repetir ciclo
      8. si esta usada:
         1. escribir "ya has usado esa letra"
         2. repetir ciclo
   9. si se acabaron las vidas escribir "¡se te han acabado las vidas!"
   10. si adivina la palabra escribir "enhorabuena has adivinado la palabra: (la palabra secreta)"
   11. repetir todo desde el 2


    
## **Atributos:**
  - Palabra secreta
  - Nombre_Jugador 
  - Nombre_Ahorcado 
  - Dificultad
  - vidas
  - letras_usadas
  - letras_adivinadas
  - intentos_maximos
## **Metodos:**
  - Dibujar del Ahorcado
  - Menu de opciones
  - reglas
  - init
  - Estado de la palabra
  - preguntar letra
  - preguntar nombre del ahorcado
  - preguntar nombre del jugador                                 
