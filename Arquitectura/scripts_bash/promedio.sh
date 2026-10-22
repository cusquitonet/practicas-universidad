#!/bin/bash
# Script que suma 5 numeros y calcula su promedio

suma=0
cantidad=5

echo "Por favor, ingresa $cantidad números:"

for (( i=1; i<=cantidad; i++ )); do
    read -p "Número $i: " num
    suma=$((suma + num))
done

promedio=$((suma / cantidad))

echo "------------------------------"
echo "El promedio es: $promedio"
