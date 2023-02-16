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

  Con esto haremos lo mencionado anteriormente, si inputeamos el numero 3 veces de forma erronea el bucle terminaría.

  <!-- Cambio en el README -->
