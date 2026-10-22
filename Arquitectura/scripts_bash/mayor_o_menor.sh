#!/bin/bash
# Script que solicita la edad al usuario y dice si es mayor o menor

read -p "Ingresa tu edad: " edad

if [ "$edad" -ge 18 ]; then
    echo "Eres mayor de edad."
else
    echo "Eres menor de edad."
fi
