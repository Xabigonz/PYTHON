# PYTHON

### TABLA DE TESTEO  "Minireto" --> Calculadora de IVA.

|PRUEBA|Input|Output Esperado|Output Recibido|PASS/FAIL|
|------|------|------|------|------|
|1|IVA: %21 Precio:300€ |IVA: 63€ PrecioIVA: 363€|IVA: 63€ PrecioIVA: 363€|PASS|
|2|IVA: %10 Precio:12€ |IVA: 63€ PrecioIVA: 363€|IVA: 13.20€ PrecioIVA: 1.20€|PASS|
|3|IVA: %4 Precio:1735.45€ |IVA: 69.42€ PrecioIVA: 1804.87€|IVA: 1804.868€ PrecioIVA: 69.418€|PASS|

###  TESTEO  programa de "Pag39.py" numeros aleatorios del uno al 100:

  > En primer lugar utilizamos el "while":
  > Al haber utilizado -->  
  > 
  > ```bash
  > while True:
  >   "el código utilizado"
  > ```
  
  Con esto haremos que la variable pregunta creada se lea constantemente de forma que se introduzca el resultado correcto para terminar el bucle.
  
  > Por otro lado con el "for":
  > Utilizamos una variable range la cuál funcionaría como un contador de vidas --->
  >  ```bash 
  >  vidas = range(0,3) #Cuando realizes tres inputs erroneos se termina el bucle
  >  for i in vidas:
  >  "el codigo utilizado"
  >  ```

  Con esto haremos lo mencionado anteriormente, si hacemo input del numero 3 veces de forma erronea el bucle terminaría.

<!-- Cambio en el README
El cambio es de ejemplo; lo importante es 
que hemos cambiado el url de enlace a nuestro repositorio
y nos ha llevado a un visualStudio web que está vinculado
a nuestro repositorio.
-->









# Ejercicio de página 78:

### Breve descripción:

>Es un pequeño programa que calcula las nominas de los distintos trabajadores creados en el propio programa,   
>con distintos metodos que mejoran el salario.

### Diagrama del programa:

|| Sistema de nominas  | Empleado(Sistema de Nominas) | Programador(Empleado) | Analista(Empleado) |
| --- | --- | --- | --- | --- |
|Atributos|  | nombre
| |salario|  lenguaje_de_programación  |
|Metodos| calcular_nominas() | boostear_salario() |  |  |
