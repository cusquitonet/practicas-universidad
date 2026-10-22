#!/bin/bash
# suma todos los numeros del 1 al 100 y los muestra

contador=1
suma=0

while [ $contador -le 100 ]; do
    suma=$((suma + contador))
    contador=$((contador + 1))
done

echo "La suma de los números del 1 al 100 es: $suma"
