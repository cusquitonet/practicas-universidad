#!/bin/bash
# Script que define 2 variables numericas y muestra las 4 operaciones matematicas

num1=10
num2=5

suma=$((num1 + num2))
resta=$((num1 - num2))
multiplicacion=$((num1 * num2))
division=$((num1 / num2))

echo "Número 1: $num1"
echo "Número 2: $num2"
echo "-------------------"
echo "Suma: $suma"
echo "Resta: $resta"
echo "Multiplicación: $multiplicacion"
echo "División: $division"
